properties([parameters([string(defaultValue: 'noam', description: 'what is your name?', name: 'NAME')]), pipelineTriggers([pollSCM('* * * * *')])])
node {
    stage("clone"){
        git "https://github.com/Noam-Zaidman/DevOps1004.git"
    }
    stage("show files"){
        bat "dir"
    }
}
