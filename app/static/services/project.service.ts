import {Injectable} from 'angular2/core';
import {Http, Response} from 'angular2/http';

import { ValidationResult } from '../models/validationResult';
import { Project } from '../models/project';
import {Observable}     from 'rxjs/Observable';

@Injectable()
export class ProjectService {

    constructor(private http: Http) { }

    private _projectsUrl = 'api/projects';

    public currentProject: Project;

    // Get all projects
    getProjects() {
        return this.http.get(this._projectsUrl)
            .map(res => <ValidationResult>res.json())
            .catch(this.handleError);        
    }

    // Get project by id
    getProject(projectId: number) {
        return this.http.get(this._projectsUrl + "/" + projectId)
            .map(res => <ValidationResult>res.json())
            .catch(this.handleError); 
    }

    // Handle error
    private handleError(error: Response) {
        return Observable.throw(error.json().error || 'Server error');
    }
}