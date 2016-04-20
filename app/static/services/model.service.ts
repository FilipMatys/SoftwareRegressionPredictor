import {Injectable} from 'angular2/core';
import {Http, Response} from 'angular2/http';

import { ValidationResult } from '../models/validationResult';
import {Observable}     from 'rxjs/Observable';

@Injectable()
export class ModelService {

    constructor(private http: Http) { }

    private _modelURL = 'api/model';

    // Get URL for prediction over file
    getFilePredictionUrl(projectId: number): string {
        return this._modelURL + "/" + projectId + "/predict/file";
    }

    // Create model for project
    create(projectId: number) {
        return this.http.get(this._modelURL + "/" + projectId + "/create")
            .map(res => <ValidationResult>res.json())
            .catch(this.handleError);
    }

    // Make prediction
    predict(projectId: number, revision: string) {
        return this.http.get(this._modelURL + "/" + projectId + "/predict/" + revision)
            .map(res => <ValidationResult>res.json())
            .catch(this.handleError);
    }

    // Load model for project
    load(projectId: number) {
        return this.http.get(this._modelURL + "/" + projectId + "/load")
            .map(res => <ValidationResult>res.json())
            .catch(this.handleError);
    }

    // Handle error
    private handleError(error: Response) {
        return Observable.throw(error.json().error || 'Server error');
    }
}