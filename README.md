![web-series-quotes-title](web-series-quotes-title.png)

# Web-Series-Quotes-Api

Api for Quotes of various web-series

## Available Web-Series

- [Breaking Bad](https://web-series-quotes.herokuapp.com/breakingbad)
- [Dark](https://web-series-quotes.herokuapp.com/dark)
- [Game Of Thrones](https://web-series-quotes.herokuapp.com/gameofthrones)
- [Money Heist](https://web-series-quotes.herokuapp.com/moneyheist)

## URI

```https://web-series-quotes.herokuapp.com```

## API

### All Quotes

```/breakingbad```

```/dark/```

```/gameofthrones```

```/moneyheist/```

### Random Quotes

```/random/breakingbad/```

```/random/breakingbad/{number_of_quotes}```

```/random/dark/```

```/random/dark/10```

```/random/gameofthrones/```

```/random/moneyheist```

### Quote Id

```/breakingbad/{id}/```

```/dark/23```

```/gameofthrones/{id}```

```/moneyheist/4/```

### Contributing

- Add other your favourite webseries quotes in ```data``` folder
- Add route path in ```routes.py```
- Make PR

### Credits

Inspired from [shevabam](https://github.com/shevabam/breaking-bad-quotes)
