#!/bin/bash -e

if [ "$TRAVIS_BRANCH" == "dev" ]; then
    export GIT_COMMITTER_EMAIL='travis@travis'
    export GIT_COMMITTER_NAME='Travis CI'

    # Since Travis does a partial checkout, we need to get the whole thing
    repo_temp=$(mktemp -d)
    git clone "https://github.com/sl33t/portfolio" "$repo_temp"

    # shellcheck disable=SC2164
    cd "$repo_temp"

    printf 'Checking out master\n' >&2
    git checkout master

    printf 'Merging dev\n' >&2
    git merge dev

    printf 'Pushing to master' >&2

    push_uri="https://$GITHUB_SECRET_TOKEN@github.com/sl33t/portfolio"

    # Redirect to /dev/null to avoid secret leakage
    git push "$push_uri" master >/dev/null 2>&1
fi