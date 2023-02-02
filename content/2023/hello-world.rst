hello, world!
=============

:date: 2023-01-21 12:39
:description: first post, check rendering

Technical
---------

I like minimal themes. I like static websites. I like the tufte layout. So I
cloned [1], removed 90% of it, et voilà.

Now on to the last chore, how does it render code?

.. code-block:: python3

    #!/usr/bin/env/python3

    def run(arg: str):
        print(f"hello, world! - {arg}")

    if __name__ == "__main__":
        run("arg")

[1] https://github.com/Eiriksmal/lawler-dot-io-template/
