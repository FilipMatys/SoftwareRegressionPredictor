import { Component, OnInit } from 'angular2/core';
import { ROUTER_DIRECTIVES } from 'angular2/router';

import { Project } from '../models/project';
import { ProjectService } from '../services/project.service';
import { RepositoryService } from '../services/repository.service';

@Component({
    selector: 'project-git-log',
    templateUrl: 'project_git_log',
    directives: [ROUTER_DIRECTIVES]
})

export class ProjectGitLogComponent implements OnInit {
    public project: Project;
    public commits: any[];
    public errors: any[];

    public toolsPanel: {
        show: string
    }
    
    constructor(
        private _projectService: ProjectService,
        private _repositoryService: RepositoryService) {
        this.project = this._projectService.currentProject;
        this.toolsPanel = {
            show: "10 items"
        }
    }

    ngOnInit() {
        this.getLog(Number(this.project.id), 10);
    }

    /**
     * Selected item for show selection
     * @param value
     */
    showToolItem_itemSelected(value: number) {
        this.getLog(Number(this.project.id), value);

        // Set label
        this.toolsPanel.show = value + " items";
    }

    getLog(projectId: number, numberOfCommits: number) {
        this._repositoryService.log(projectId, numberOfCommits).subscribe(
            result => {
                // Check if result is valid
                if (result.isValid) {
                    this.commits = result.data;
                }
                // Something went wrong
                else {
                    this.errors = result.errors;
                }
            },
            errors => this.errors = errors
        );
    }
}