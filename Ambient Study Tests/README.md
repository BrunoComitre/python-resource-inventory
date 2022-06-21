# Environment variables, dotenv, constants and settings

By: [Variáveis de ambiente, dotenv, constantes e configurações | Live de Python #207](https://www.youtube.com/watch?v=DiiKff1z2Yw&t=1372s)

## Environment Variables

Python has two native ways to access environment variables:
- **os.environ:** A dictionary with all environment variables
- **os.getenv():** a way to get a single variable and with a more error-proof system

## Note

**THE CORRECT IS TO USE .ENV AS A VARIABLE TEMPLATE**

1. The environment variables that we create or modify within our system, they are valid only for our process.

2. Remember that there are different hierarchical levels where variables are defined: per user, per shell, or per system

3. One of the great advantages of using environment variables is that you do not change the code to a new version just because of a value that may vary!

## Other Environments Packages

- [henriquebastos/python-decouple](https://github.com/henriquebastos/python-decouple/)
- [rochacbruno/dynaconf](https://github.com/rochacbruno/dynaconf)

## References

- [sloria/environs](https://github.com/sloria/environs)
- [The Twelve-Factor APP](https://12factor.net/pt_br/) [PT-BR]
- [The Twelve-Factor APP](https://12factor.net/) [EN-US]

***
