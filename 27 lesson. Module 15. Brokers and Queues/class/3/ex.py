import sentry_sdk

sentry_sdk.init(
    "link",
    # Set traces_sample_rate to 1.0 to capture 100%
    # of transactions for performance monitoring.
    # We recommend adjusting this value in production.
    traces_sample_rate=1.0,
)
division_by_zero = 1 / 0
# https://docs.sentry.io/product/sentry-basics/
# try:
#     2/0
# except Exception as err:
#     sentry_sdk.capture_exception(err)
#     print(err)
# sentry_sdk.capture_message("Message")
