import { Pipe } from 'angular2/core';

@Pipe({ name: 'modelSearch' })
export class ModelSearchPipe {
    transform(value, [term]) {
        return value.filter((item) => item.name.toLowerCase().indexOf(term) >= 0);
    }
}