from django.dispatch import receiver, Signal

my_signal = Signal()
@receiver(my_signal)
def my_signal_handler(sender, **kwargs):
    print(kwargs['msg'])

