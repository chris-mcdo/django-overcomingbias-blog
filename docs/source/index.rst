django-overcomingbias-api: an API to Robin Hanson's content
===========================================================

``django-overcomingbias-api`` is a standalone `Django <https://www.djangoproject.com/>`_
app which lets you create and manage an API to (some of) Robin Hanson's content.

It scrapes the `overcomingbias <https://www.overcomingbias.com/>`_ blog (and other
sites) and presents the data in a structured form via a
`REST <https://en.wikipedia.org/wiki/Representational_state_transfer>`_ API.
(I may add a GraphQL API later, too.)

Basic Usage
-----------

A graphical user interface is provided through the
`Django admin site <https://docs.djangoproject.com/en/dev/ref/contrib/admin/>`_.

To initialise a database of all overcomingbias posts, use the "pull" button:

.. image:: _static/pull-and-sync.png
   :align: center
   :alt: Create and update overcomingbias posts from the admin site

Add new posts with "pull", and update modified posts with "sync".
(You can also add content from YouTube and Spotify.)

Categorise content according to the "ideas" and "topics" it contains, or by generic
"tags".
Use the admin site and custom
`Admin Actions <https://docs.djangoproject.com/en/dev/ref/contrib/admin/actions/>`_
to manage content.

Link the app in your URL config to access the REST API:

.. code-block:: python

    # urls.py

    urlpatterns = [
        ...
        path("", include("obapi.urls")),
        ...
    ]


You should then be able to access the automatic API documentation at URL ``/api/docs``.

.. image:: _static/api-docs.png
   :align: center
   :alt: View the API docs

Alternatively, provide your own views for each post:

.. code-block:: python

    # urls.py
    from django.urls import path, register_converter
    from obapi.converters import OBPostNameConverter
    from myapp.views import ob_detail_view

    register_converter(OBPostNameConverter, "ob_name")
    urlpatterns = [
        ...
        path(
            "content/overcomingbias/<ob_name:item_id>",
            ob_detail_view, # custom view
            name="obcontentitem_detail",
        ),
        ...
    ]

For more on how to use the package, see :doc:`Getting Started <getting-started>`.

Features
--------

Currently, content can be scraped from the following sources:

- The `overcomingbias <https://www.overcomingbias.com/>`_ blog (added automatically)

- Robin Hanson's `home page <https://mason.gmu.edu/~rhanson/>`_

- YouTube videos (add videos manually using their URLs)

- Spotify podcast episodes (add episodes manually using their URLs)

Documentation
-------------

See :doc:`Getting Started <getting-started>` for an introduction to the package. 

For the full details, check out the
`code on GitHub <https://github.com/chris-mcdo/django-overcomingbias-api>`_.


Bugs/Requests
-------------

Please use the
`GitHub issue tracker <https://github.com/chris-mcdo/django-overcomingbias-api/issues>`_
to submit bugs or request features.

Changelog
---------

See the :doc:`Changelog <changelog>` for a list of fixes and enhancements of each
version.

License
-------

Copyright (c) 2022 Christopher McDonald

Distributed under the terms of the
`MIT <https://github.com/chris-mcdo/django-overcomingbias-api/blob/main/LICENSE>`_
license.

All overcomingbias posts are copyright the original authors.
