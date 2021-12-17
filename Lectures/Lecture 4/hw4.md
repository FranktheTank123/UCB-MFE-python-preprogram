# HW3
Please do the following in a jupyter notebook and using the data from `data/data.db`

1. Create a jupyter notebook template to do the following - for a given token and date range:
    - calculate the hourly return by timestamp
    - calculate the hourly volatility (you can use the formula we went over in class)
    - calculate maximum drawdown up to that hour for each hour
    - then plot in a 2x2 grid:
        - hourly return
        - hourly vol
        - maximum drawdown
        - close prices
        - color each day on the graph
2. Create a runner notebook using papermill to run the template notebook across all tokens in the database and the last 2 complete weeks in the database.  Summarize the following in a single DataFrame in the runner notebook
    - avg hourly return by run
    - avg volatility by run
    - maximum drawdown over the entire period of each run
    - range of last close price - first close price
