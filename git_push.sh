#!/bin/bash
# Deploy to via pushing to a remote git repository.
#
# Add the following environment variables to your project configuration and make
# sure the public SSH key from your projects General settings page is allowed to
# push to the remote repository as well.
# * REMOTE_REPOSITORY, e.g. "git@github.com:codeship/documentation.git"
# * REMOTE_BRANCH, e.g. "production"
#
# Include in your builds via
# \curl -sSL https://raw.githubusercontent.com/codeship/scripts/master/deployments/git_push.sh | bash -s
REMOTE_REPOSITORY=${REMOTE_REPOSITORY:"https://github.com/guaigua/mi-buildout"}
REMOTE_BRANCH=${REMOTE_BRANCH:"master"}

set -e

git fetch --unshallow || true
git push "${REMOTE_REPOSITORY}" "${CI_COMMIT_ID}:${REMOTE_BRANCH}"

