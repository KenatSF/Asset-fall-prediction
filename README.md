# Bitcoin prediction

## Dependencies

* R version 3.6.2
* Python version 3.8.2

## Prediction

The correct prediction of any asset is almost impossible, however, one must try it.

* Making use of google trends data in words such as [Bitcoin, Blockchain, debt, dollar, ...].
* Getting Bitcoin data such as open_time, close_price.
* Getting the returns from close_price.
* Merging both data bases to built the training and testing bases.
* Comparing multiples models to get the best option.

Best model with minimum number of variables.
```
     glm(y ~ banking.system + bce + bill.gates + bitcoin.alert + 
                    bitcoin.bubble + bitcoin.dump + bitcoin.hack + bitcoin.whales + 
                    bitcoin + blockchain + coingecko + cryptonews + debt.jubilee + 
                    financial.independence + housing.market + jerome.powell + 
                    microsoft + ray.dalio + real.economy + real.estate + satoshi.nakamoto + 
                    vitalik.buterin + volatility + amazon + apple + bitcoin.twitter + 
                    ethereum + smart.contracts + sec + facebook + fed,
                data = db_training, family = "binomial")
```