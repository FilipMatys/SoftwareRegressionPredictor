import { Component } from 'angular2/core';
import { RouteParams, RouteConfig, Router, ROUTER_DIRECTIVES, ROUTER_PROVIDERS } from 'angular2/router';

import { ProjectGitLogComponent } from './project-git-log.component';
import { ProjectGitCommitComponent } from './project-git-commit.component';

@Component({
    selector: 'project-git',
    templateUrl: 'project_git',
    directives: [ROUTER_DIRECTIVES]
})

@RouteConfig([
    {
        path: '/',
        name: 'ProjectGitLog',
        component: ProjectGitLogComponent,
        useAsDefault: true
    },
    {
        path: '/commit/:hash',
        name: 'ProjectGitCommit',
        component: ProjectGitCommitComponent
    }
])

export class ProjectGitComponent {

}

