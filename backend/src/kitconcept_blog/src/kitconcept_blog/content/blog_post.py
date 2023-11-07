from kitconcept_blog import _
from plone.autoform import directives
from plone.dexterity.content import Container
from plone.supermodel.model import Schema
from z3c.relationfield.schema import RelationChoice
from z3c.relationfield.schema import RelationList
from zope import schema
from zope.interface import implementer


class IBlogPost(Schema):
    """A Blog post."""

    title = schema.TextLine(
        title=_("Title"),
        description=_("Blog post title"),
        required=True,
    )

    description = schema.TextLine(
        title=_("Description"),
        description=_("Blog post description"),
        required=False,
    )

    authors = RelationList(
        title=_("Authors"),
        description=_("Blog post authors"),
        required=False,
        value_type=RelationChoice(
            vocabulary="plone.app.vocabularies.Catalog",
        ),
    )
    directives.widget(
        "authors",
        frontendOptions={
            "widget": "object_browser",
            "widgetProps": {
                "selectableTypes": ["Author"],
            },
        },
    )


@implementer(IBlogPost)
class BlogPost(Container):
    """A Blog post."""
