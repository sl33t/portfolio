#!/bin/bash -e

eval "$(ssh-agent -s)"
chmod 600 $TRAVIS_BUILD_DIR/deploy_rsa
mv $TRAVIS_BUILD_DIR/deploy_rsa ~/.ssh/id_rsa
repo_temp=$(mktemp -d)
git clone "https://github.com/sl33t/portfolio" "$repo_temp"
cd "$repo_temp"
git remote add deploy ssh://sl33t@web518.webfaction.com:/home/sl33t/webapps/portfolio/myproject
git push deploy