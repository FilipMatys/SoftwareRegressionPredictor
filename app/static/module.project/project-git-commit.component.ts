import { Component, OnInit } from 'angular2/core';
import { RouteParams } from 'angular2/router';

import { Project } from '../models/project';
import { ProjectService } from '../services/project.service';
import { RepositoryService } from '../services/repository.service';

@Component({
    selector: 'project-git-commit',
    templateUrl: 'project_git_commit'
})


export class ProjectGitCommitComponent implements OnInit {
    public project: Project;
    public commit: any;
    public errors: string[];

    public toolsPanel: {
        show: string
    }
    public showLinesOfCode = true;
    public showCodeAnalysis = true;

    constructor(
        private _routeParams: RouteParams,
        private _projectService: ProjectService,
        private _repositoryService: RepositoryService) {
        this.project = this._projectService.currentProject;
        this.toolsPanel = {
            show: 'All'
        }
    }

    ngOnInit() {
        this.getLog(Number(this.project.id), this._routeParams.get('hash'));
    }

    /**
     * Show items based on selected value
     * @param state Selected state
     * @param label Label of selected state
     */
    showToolItem_itemSelected(state: string, label: string) {
        switch (state) {
            case 'changes':
                this.showLinesOfCode = true;
                this.showCodeAnalysis = false;
                console.log('Changes');
                break;
            case 'analysis':
                this.showLinesOfCode = false;
                this.showCodeAnalysis = true;
                console.log("Analysis");
                break;
            case 'all':
                this.showLinesOfCode = true;
                this.showCodeAnalysis = true;
                console.log("All");
                break;
        }

        // Set label
        this.toolsPanel.show = label;
    }

    getLog(projectId: number, hash: string) {
        this._repositoryService.getCommit(projectId, hash).subscribe(
            result => {
                // Check if result is valid
                if (result.isValid) {
                    this.commit = result.data;

                    // Map changes object into list
                    for (var index = 0; index < this.commit.diff.files.length; index++) {
                        this.commit.diff.files[index].added.changes = this.mapObjectToList(this.commit.diff.files[index].added.changes);
                        this.commit.diff.files[index].removed.changes = this.mapObjectToList(this.commit.diff.files[index].removed.changes);
                    }
                }
                // Something went wrong
                else {
                    this.errors = result.errors;
                }
            },
            errors => this.errors = errors
        );
    }

    /**
     * Map object into array
     * @param object
     */
    private mapObjectToList(object: any): any[] {
        var array = [];

        // Iterate through each key
        for (var key in object) {
            array.push({
                name: key,
                value: object[key] 
            });
        }

        return array;
    }
}