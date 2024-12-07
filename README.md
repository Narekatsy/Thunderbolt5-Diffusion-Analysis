# Market Adoption of Beats Studio Buds+

## Overview
This project applies the Bass diffusion model to the adoption curve of Beats Studio Buds+, in comparison with that of Apple AirPods, including historical sales data, estimation of the parameters of the diffusion model, and predictions of future adoptions.

## Contents
- `data/`: Contains the dataset used for analysis.
- `airpods_bass_model.py`: Code for estimating the Bass model parameters.
- `beats_bass_model.py`: Code for simulating the adoption of Beats Studio Buds+.
- `annual_airpods_sales`: Code for showing annual sales of AirPods.
- `beats_projected_adoption.png`: Graph of the projected adoption curve.
- `report_source.md`: The report in Markdown format.
- `report.pdf`: The report in PDF format.

## How to Use
Clone the repository:
   ```bash
   git clone https://github.com/narekatsy/beats-studio-buds-diffusion-analysis
   cd beats-studio-buds-diffusion-analysis
   ```

## Data Sources
- https://headphonesaddict.com/airpods-facts-revenue/#How-many-AirPods-are-sold-each-year
- https://www.canalys.com/newsroom/worldwide-tws-shipments-Q4-2022

## Report Overview
The report provides:

- A comparative analysis of Beats Studio Buds+ and Apple AirPods.
- Estimation of Bass model parameters (*p*, *q*, M) using AirPods sales data.
- Forecasted adoption curve of Beats Studio Buds+.

The report is available in:

- **Markdown format**: `report/report_source.md`
- **PDF format**: `report/report.pdf`
