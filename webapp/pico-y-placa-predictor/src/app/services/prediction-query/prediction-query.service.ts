import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Observable, of } from 'rxjs';
import { catchError, retry } from 'rxjs/operators';
import { PredictionQuery } from '../../models/prediction_query';
import { PredictionResponse } from '../../models/prediction_reponse';

@Injectable({
  providedIn: 'root',
})
export class PredictionQueryService {
  private predictionUrl = 'http://localhost:5000/api/circulate';

  httpOptions = {
    headers: new HttpHeaders({ 'Content-Type': 'text/plain' }),
  };

  constructor(private http: HttpClient) {}

  getPrediction(
    license_plate: string,
    date: string,
    time: string
  ): Observable<PredictionResponse> {
    const query: PredictionQuery = {
      license_plate: license_plate,
      date: date,
      time: time,
    };
    return this.http.post<PredictionResponse>(
      this.predictionUrl,
      query,
      this.httpOptions
    );
  }
}
