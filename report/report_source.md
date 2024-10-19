# Marketing Analytics Project

**Date:** 18.10.2024

**Class Name:** DS223 Marketing Analytics

**Project Name:** Beats Studio Buds+ Diffusion Analysis

**Student Name:** Narek Hakobyan 

---

## Introduction  
The report focuses on the market adoption of Beats by Dre's newest studio wireless earbuds, the Beats Studio Buds+. These earbuds have features such as advanced ANC, transparency mode, and multi-device compatibility, making them competitive in the growing wireless audio market.
It positions Beats Studio Buds+ in comparison with older products such as Apple AirPods and uses the Bass Diffusion Model to predict the probable adoption of the earbuds by people. The report focuses on recent market trends and what consumers are looking for.

---

## Reflection on Similar Innovation  
**Chosen Innovation:** Beats Studio Buds+  
**Similar Innovation:** Apple AirPods 

Beats Studio Buds+ follow the path of the AirPods offering the users a compact and wireless approach. While the AirPods revolutionized the market thanks to seamless integration with the Apple ecosystem, Beats Studio Buds+ is more about active noice cancellation (ANC) and cross-platform compatibility on iOS and Android. The Studio Buds+ focus is on onactive noice cancellation technology, even better transparency modes, and increased battery life. Both products reflect the main trends of wireless convenience and high audio quality, but the Beats Studio Buds+ expand the circle of accessibility further than Apple's ecosystem towards a more general market.

---

## Historical Data Collection
### AirPods Sales Data
The historical sales data for Apple AirPods from 2017 to 2022 is as follows:

| Year | Units Sold (millions) |
|------|-----------------------|
| 2017 | 10                    |
| 2018 | 20                    |
| 2019 | 35                    |
| 2020 | 50                    |
| 2021 | 58                    |
| 2022 | 57                    |

The values for 2021 and 2022 have been adjusted to exclude Beats sales to give a better indication of the performance of AirPods as a standalone product. The figures reflect remarkable growth since their launch with heavy year-on-year increases, reaching an estimated 58 million units in 2021 and 57 million in 2022.

The graph below shows the annual sales of AirPods from 2017 to 2022.
![Annual sales of AirPods (2017-2022)](https://github.com/Narekatsy/Beats-Studio-Buds-Diffusion-Analysis/blob/main/img/airpods_annual_sales.png)

#### Sources:
- [Headphones Addict - AirPods Sales](https://headphonesaddict.com/airpods-facts-revenue/#How-many-AirPods-are-sold-each-year?)
- [Canalys - Worldwide TWS Shipments Q4 2022](https://www.canalys.com/newsroom/worldwide-tws-shipments-Q4-2022)

---

## Estimating Bass Model parameters
### Estimation Process
Using the discrete-time Bass diffusion model, I estimated the parameters ***p***, ***q***, and **M** using the code found in **`airpods_bass_model.py`**.

### Estimated Parameters
- **p (Coefficient of Innovation)**: 0.0381
- **q (Coefficient of Imitation)**: 0.6433
- **M (Market Potential)**: 350 million

---

## Predicting the Diffusion of Beats Studio Buds+
### Simulation of Adoption
Using the estimated parameters, we can simulate the adoption of Beats Studio Buds+ over the next 10 years.
The code **`beats_bass_model.py`** simulates the adoption using the Bass model with derived estimated parameters.

### Adoption Curve
The following graph illustrates the projected adoption of Beats Studio Buds+ over the next 10 years.
![Projected Adoption of Beats Studio Buds+](https://github.com/Narekatsy/Beats-Studio-Buds-Diffusion-Analysis/blob/main/img/beats_projected_adoption.png)

This graph represents the accumulated number of Beats Studio Buds+ adopters over a 10-year period. Initially, the rate of diffusion or adoption will be slow, but with more and more people being made aware of the product, it will increase gradually. Finally, due to the snowballing effect of social influence-particularly because of recommendations by current users-a sharp upward curve should be expected.

### Market Size Consideration
First, a Beats Studio Buds+ market size was estimated considering the market size of AirPods, which are already well-settled in the wireless earbuds market. In addition, the global market is considered, not the regional one, because the reference data show worldwide sales figures.

---

## Conclusion 
While it is unlikely that the Beats Studio Buds+ will surpass AirPods in sales, they hold substantial potential for success within the competitive wireless earbuds market. The insights derived from the Bass diffusion model suggest that with effective marketing strategies and leveraging existing user recommendations, Beats Studio Buds+ can achieve significant market penetration and acceptance.
