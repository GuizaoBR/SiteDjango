from django import forms
from core.models import Contato
from django.core.mail import send_mail, EmailMessage
from django.core import mail



class ContatoForm(forms.ModelForm):
    class Meta:
        model = Contato
        fields = "__all__"
    nome = forms.CharField(label='Nome')
    email = forms.EmailField(label='Email')
    mensagem = forms.Field(label = 'Mensagem', widget=forms.Textarea(attrs={'class' : 'materialize-textarea'}))
    def enviar(self):
        titulo = 'Mensagem de %(nome)s'%self.cleaned_data
        destino = 'gui.germano.silva@gmail.com'
        texto = """
        Nome: %(nome)s
        E-mail: %(email)s
        Mensagem:
        %(mensagem)s
        """ % self.cleaned_data
        
        send_mail(
            subject=titulo,
            message=texto,
            from_email=destino,
            recipient_list=[destino],
            )
    '''
    class Meta:
        model = Contato
        fields = "__all__"
        
        def send_email(self, request):
            subject = 'Contato'
            message = Contato.mensagem
            from_email = Contato.email
            if subject and message and from_email:
                try:
                    send_mail(subject, message, from_email, ['djangonoreplay@gmail.com'])
                except BadHeaderError:
                    return HttpResponse('Invalid header found.')
            else:
            # In reality we'd use a form class
            # to get proper validation errors.
                return HttpResponse('Make sure all fields are entered and valid.')


    
'''
    
    
'''   
    def envia_email(self):
        print(
            'Email para você: \n'+
            'Nome: ' + self. cleaned_data['nome'] + '\n'+
            'Email: '+ self.cleaned_data['email'] + '\n' +
            'Mensagem: ' + self.cleaned_data['mensagem']
        )
   '''