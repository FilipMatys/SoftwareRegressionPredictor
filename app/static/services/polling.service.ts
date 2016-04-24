import { Injectable } from 'angular2/core';
import { Http, Response } from 'angular2/http';

import { ValidationResult } from '../models/validationResult';
import { Observable }     from 'rxjs/Observable';

@Injectable()
export class PollingService {

    constructor(private http: Http) {
    }

    private _pollingURL = 'api/poll';

    // Create model for project
    poll() {
        return Observable.interval(1000)
            .flatMap(() => {
                return this.http.get(this._pollingURL)
                    .map(res => <ValidationResult>res.json())
                    .catch(this.handleError);
            });
    }

    // Handle error
    private handleError(error: Response) {
        return Observable.throw(error.json().error || 'Server error');
    }
}