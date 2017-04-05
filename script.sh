git filter-branch --commit-filter '
        if [ "$GIT_COMMITTER_EMAIL" = "razavi@inside.sahab.ir" ];
        then
                GIT_COMMITTER_NAME="Mostafa Razavi";
                GIT_AUTHOR_NAME="Mostafa Razavi";
                GIT_COMMITTER_EMAIL="mostafa@sepent.com";
                GIT_AUTHOR_EMAIL="mostafa@sepent.com";
                git commit-tree "$@";
        else
                git commit-tree "$@";
        fi' HEAD
