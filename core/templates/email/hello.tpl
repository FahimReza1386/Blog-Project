{% extends "mail_templated/base.tpl" %}


{% block subject %}
    Account Activation
{% endblock %}


{% block html %}


This is a <strong>{{ token }}</strong> of the my account  .

{% endblock %}