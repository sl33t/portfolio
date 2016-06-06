#!/bin/bash -e

if [ "$TRAVIS_BRANCH" == "dev" ]; then
    export GIT_COMMITTER_EMAIL='travis@travis'
    export GIT_COMMITTER_NAME='Travis CI'

    git config --global user.email "$GIT_COMMITTER_EMAIL"
    git config --global user.name "$GIT_COMMITTER_NAME"

    # Since Travis does a partial checkout, we need to get the whole thing
    repo_temp=$(mktemp -d)
    git clone "https://github.com/sl33t/portfolio" "$repo_temp"
    push_uri="https://$GITHUB_SECRET_TOKEN@github.com/sl33t/portfolio"

    # shellcheck disable=SC2164
    cd "$repo_temp"

    printf 'Checking out dev\n' >&2
    git checkout dev

    # Run pep8 and autoflake tests
    printf 'Running pep8 and pyflakes fixes\n' >&2
    autoflake --in-place --recursive --imports=django .

    if [ -z "$(git status --porcelain)" ]; then
        printf 'There are no changes\n' >&2
    else
        printf 'Changes are being commited\n' >&2
        git commit -am "Pep8 and PyFlake corrections"  >&2
        git push "$push_uri" dev >/dev/null 2>&1
    fi

    printf 'Checking out master\n' >&2
    git checkout master

    printf 'Merging dev\n' >&2
    git merge dev

    printf 'Pushing to master\n' >&2
    git push "$push_uri" master >/dev/null 2>&1
fi

if [ "$TRAVIS_BRANCH" == "master" ]; then
    eval "$(ssh-agent -s)"
    chmod 600 $TRAVIS_BUILD_DIR/deploy_rsa
    mv $TRAVIS_BUILD_DIR/deploy_rsa ~/.ssh/id_rsa
    git remote add deploy ssh://sl33t@web518.webfaction.com:/home/sl33t/webapps/portfolio/myproject
    git push deploy
fi