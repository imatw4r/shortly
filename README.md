# shortly
URL shortener project

The goal of this project is to implement URL shortener while following best practices, and DDD approach from the very start, and automating all that can be automated, including autoformatters, linters, static type checking, import sorting, etc.

Main technologies/libraries:
* Python 3.10
* FastAPI
* SQLAlchemy
* Pytest
* [dependency injector](https://python-dependency-injector.ets-labs.org/index.html)

Tools to enforce code guidelines:
* [black](https://github.com/psf/black)
* [flakeheaven](https://github.com/flakeheaven/flakeheaven)
* [mypy](https://github.com/python/mypy)
* [isort](https://github.com/PyCQA/isort)

Knowledge sources:
* https://herbertograca.com/2017/11/16/explicit-architecture-01-ddd-hexagonal-onion-clean-cqrs-how-i-put-it-all-together/?fbclid=IwAR3bHfAbO-i6bfDCxAK2KvpBH1wr_BXl3eXyT5WWra79k57bjiGOQoRAcPY
* https://enterprisecraftsmanship.com/posts/specification-pattern-always-valid-domain-model/?fbclid=IwAR0ysg-jfUOaYRuQ8GYprkGKVOYP1b2zqzXSMivsMFbfIjFHWWxlpIRu-Rs
* https://github.com/Enforcer/clean-architecture
