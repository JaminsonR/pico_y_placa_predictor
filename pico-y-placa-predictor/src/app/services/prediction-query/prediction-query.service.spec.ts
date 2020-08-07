import { TestBed } from '@angular/core/testing';

import { PredictionQueryService } from './perdiction-query.service';

describe('PredictionQueryService', () => {
  let service: PredictionQueryService;

  beforeEach(() => {
    TestBed.configureTestingModule({});
    service = TestBed.inject(PredictionQueryService);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });
});
