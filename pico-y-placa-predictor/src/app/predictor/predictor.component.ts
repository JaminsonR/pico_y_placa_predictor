import { Component, OnInit } from '@angular/core';
import { PredictionQuery } from '../models/prediction_query';
import { PredictionResponse } from '../models/prediction_reponse';
import { PredictionQueryService } from '../services/prediction-query/prediction-query.service';
import { MatDatepickerModule } from '@angular/material/datepicker';

@Component({
  selector: 'app-predictor',
  templateUrl: './predictor.component.html',
  styleUrls: ['./predictor.component.css'],
})
export class PredictorComponent implements OnInit {
  query: PredictionQuery = {
    license_plate: '',
    date: '',
    time: '',
  };
  show: boolean = false;
  prediction: PredictionResponse;

  constructor(private PredictionQueryService: PredictionQueryService) {}

  predict(): any {
    this.PredictionQueryService.getPrediction(
      this.query.license_plate,
      this.query.date,
      this.query.time
    ).subscribe((prediction: PredictionResponse) => {
      this.prediction = prediction;
      this.show = true;
    });
  }

  ngOnInit(): void {}
  updateDate(dateObject) {
    const stringified = JSON.stringify(dateObject.value);
    const dob = stringified.substring(1, 11);
    this.query.date = dob;
  }
}
