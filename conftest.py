from hypothesis import settings, Verbosity, HealthCheck

settings.register_profile(
    "DEBUG",
    max_examples=10,
    verbosity=Verbosity.verbose,
)

settings.register_profile(
    "CI",
    max_examples=100,
    deadline=None,
    suppress_health_check=[
        HealthCheck.data_too_large,
        HealthCheck.filter_too_much,
        HealthCheck.too_slow,
    ],
)
