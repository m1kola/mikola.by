from django.utils.safestring import mark_safe
from django.utils.translation import ugettext_lazy as _
from pygments import highlight
from pygments.formatters import get_formatter_by_name
from pygments.lexers import get_lexer_by_name
from wagtail.wagtailcore import blocks
from wagtail.wagtailembeds.blocks import EmbedBlock


class CodeBlock(blocks.StructBlock):
    """
    Code Highlighting Block
    """
    LANGUAGE_CHOICES = (
        ('python', _("Python")),
        ('php', _("PHP")),
        ('bash', _("Bash/Shell")),
        ('html', _("HTML")),
        ('js', _("JavaScript")),
        ('django', _("Django templating language")),
        ('css', _("CSS")),
        ('scss', _("SCSS")),
    )

    language = blocks.ChoiceBlock(choices=LANGUAGE_CHOICES, required=False)
    code = blocks.TextBlock()

    class Meta:
        icon = 'code'

    def render(self, value, context=None):
        src = value['code'].strip('\n')
        lang = value['language']

        lexer = get_lexer_by_name(lang)
        formatter = get_formatter_by_name('html', linenos=None, noclasses=False)

        return mark_safe(highlight(src, lexer, formatter))


class StoryBlock(blocks.StreamBlock):
    paragraph = blocks.RichTextBlock()
    embed = EmbedBlock()
    code = CodeBlock()
