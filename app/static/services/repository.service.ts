import {Injectable} from 'angular2/core';
import {Http, Response} from 'angular2/http';

import { ValidationResult } from '../models/validationResult';
import { Observable }     from 'rxjs/Observable';

@Injectable()
export class RepositoryService {

    constructor(private http: Http) { }

    private _repositoriesUrl = 'api/repository';


    // Get last commits
    log(projectId: number, numberOfCommits: number) {
        return this.http.get(this._repositoriesUrl + "/" + projectId + "/log/" + numberOfCommits)
            .map(res => <ValidationResult>res.json())
            .catch(this.handleError);
    }

    // Get commit
    getCommit(projectId: number, hash: string) {
        return this.http.get(this.getCommitUrl(projectId, hash))
            .map(res => <ValidationResult>res.json())
            .catch(this.handleError);
    }

    // Handle error
    private handleError(error: Response) {
        return Observable.throw(error.json().error || 'Server error');
    }

    private getCommitUrl(projectId: number, hash: string): string {
        return this._repositoriesUrl + "/" + projectId + "/commit/" + hash;
    }
}