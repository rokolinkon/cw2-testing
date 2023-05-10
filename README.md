# Software Testing
## Welcome to the solutions branch!
Since you're only here because you either did or are doing the TDD section, I've removed all of the rest of the fluff—you can find the solutions you desire in the `currency_converter` branch!
## Test-Driven Development (TDD)
Using TDD, tests are developed either before or in tandem with code that is to be written. For our purposes and for this lab, we will be developing tests before writing any code and using them as a specification for the code we are to write. Here, we'll be developing a small module that converts a few different currencies around the world. This converter should support converting from USD into three different currencies: `"JPY"` (USD × 135), `"EGP"` (USD × 30.85), and `"ARS"` (USD × 227.60). Anything else should raise a `LookupError`, and negative currency provided should raise a `ValueError`. The default value for the amount of currency if not provided should be 1 USD.<br>
With this specification, we can write some unit tests to serve as a more concrete specification for exactly how every part of this module works, and an easily-runnable progress report as to what we've got done and what we still need to do.

### Unit tests
Begin by making a folder in the root of this repository called `currency_converter`. Inside, make two files: `test_currency_converter.py` and `currency_converter.py`. We'll start in the `test_currency_converter.py` file.

* Import `TestCase` and `main` from `unittest`
* Import `convert` from `currency_converter`
* Create a class `TestCurrencyConverter` that extends from the `TestCase` class you just imported

Now, we can begin writing tests. First, the regular functionality. To ensure that more than just one number converts correctly, we'll write multiple tests for each possible currency—one for converting $1 USD (using the default value for the argument if none is passed), and one for converting $50 USD, as two random examples. Thus, we will have six tests for "normal functionality." After that, we'll need to have two tests for the errors that can be raised—asserting that passing a negative number raises a `ValueError`, and asserting that passing an unsupported currency raises a `LookupError`. All of these will be done by calling the `convert` method we imported from `currency_converter` and passing it first a string, consisting of one of `["JPY", "EGP", "ARS"]` (case-insensitive), representing the currency into which to convert, and next an integer value representing the amount in USD to convert. Thus, we'll end up with eight tests:
* `test_JPY_1` (135)
* `test_EGP_1` (30.85)
* `test_ARS_1` (227.6)
* `test_JPY_50` (6750)
* `test_EGP_50` (1542.5)
* `test_ARS_50` (11380)
* `test_negative_value` (ValueError)
* `test_unsupported_currency` (LookupError)

> Suggested code for these tests can be found in the `solutions` branch, along with three possible solutions to the actual code of the module.

Running these tests right now, they should fail. That's fine! Create a `convert` function in the `currency_converter.py` file with two parameters: `currency: str` and `amt_usd: float = 1`. Now, we can implement the method! First, let's implement the functionality. We'll need to somehow check the currency that the user wants to convert into against our known currencies, and depending on the one they select, return the right multiplication of their `amt_usd` input value. One way we can implement this is using a simple match-case block, just like a switch-case in other languages.

```py
def convert(currency: str, amt_usd: float = 1) -> float:
    match currency.upper():
        case "ARS": return amt_usd * 227.6
        case "JPY": return amt_usd * 135
        case "EGP": return amt_usd * 30.85
```

That should cover the basic functionality! Now, if we run our tests, six of them should pass, and two should fail, assuming we've done everything right thus far. Thus, we need to implement the exceptions! Fail fast, and add the check if `amt_usd` is negative to the top of the function call, raising a `ValueError`. Then, add a default case that raises a `LookupError`, and run the tests again… to find that they pass! The final code should look something like this:

```py
def convert(currency: str, amt_usd: float = 1) -> float:
    if amt_usd < 0: raise ValueError("Cannot have negative money")
    match currency.upper():
        case "ARS": return amt_usd * 227.6
        case "JPY": return amt_usd * 135
        case "EGP": return amt_usd * 30.85
        case _: raise LookupError(f"Unknown currency: {currency} (expected one of 'ARS', 'JPY', 'EGP')")
```

And you're done! You've successfully developed a module using Test-Driven Development! You can see code for the tests in the `solutions` branch if something is still awry, as well as two other ways you could've implemented the `convert` method—but until then, congratulations!