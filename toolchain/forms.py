from django import forms


class HeuristicForm(forms.Form):
    tempmin = forms.IntegerField(label='Min', initial=0)
    tempmax = forms.IntegerField(label='Max', initial=1600)

    partialpressuremin = forms.IntegerField(label='Min', initial=0)
    partialpressuremax = forms.IntegerField(label='Max', initial=100)

    absolutepressuremin = forms.IntegerField(label='Min', initial=0)
    absolutepressuremax = forms.IntegerField(label='Max', initial=1)

    flowmin = forms.IntegerField(label='Min', initial=0)
    flowmax = forms.IntegerField(label='Max', initial=2500)

    def cleaned_data(self):
        return


class DatabaseForm(forms.Form):

    hostname = forms.CharField(label='Host')
    database_name = forms.CharField(label='Database')
    username = forms.CharField(label='Username')
    password = forms.CharField(label='Password')
    port = forms.CharField(label='Port')

    def cleaned_data(self):
        return
