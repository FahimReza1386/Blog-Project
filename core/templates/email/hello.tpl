{% extends "mail_templated/base.tpl" %}


{% block subject %}
Hello {{ name }}
{% endblock %}


{% block html %}

<img alt="hi" src="https://img.freepik.com/premium-photo/person-coding-project-laptop_1079150-36836.jpg?semt=ais_hybrid">

This is An <strong>html</strong> message .

{% endblock %}