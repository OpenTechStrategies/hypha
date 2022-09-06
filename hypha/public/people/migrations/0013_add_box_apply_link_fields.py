# Generated by Django 2.2.9 on 2020-01-21 20:17

from django.db import migrations
import wagtail.blocks
import wagtail.fields
import wagtail.documents.blocks
import wagtail.embeds.blocks
import wagtail.images.blocks
import wagtail.snippets.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('people', '0012_personindexpage_introduction'),
    ]

    operations = [
        migrations.AlterField(
            model_name='personpage',
            name='biography',
            field=wagtail.fields.StreamField([('heading', wagtail.blocks.CharBlock(classname='full title', icon='title')), ('paragraph', wagtail.blocks.RichTextBlock()), ('box', wagtail.blocks.StructBlock([('box_content', wagtail.blocks.RichTextBlock()), ('box_class', wagtail.blocks.CharBlock(required=False))])), ('apply_link', wagtail.blocks.StructBlock([('application', wagtail.blocks.PageChooserBlock())])), ('image', wagtail.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock()), ('caption', wagtail.blocks.CharBlock(required=False))])), ('quote', wagtail.blocks.StructBlock([('quote', wagtail.blocks.CharBlock(classname='title')), ('attribution', wagtail.blocks.CharBlock(required=False)), ('job_title', wagtail.blocks.CharBlock(required=False))])), ('embed', wagtail.embeds.blocks.EmbedBlock()), ('call_to_action', wagtail.snippets.blocks.SnippetChooserBlock('utils.CallToActionSnippet', template='blocks/call_to_action_block.html')), ('document', wagtail.blocks.StructBlock([('document', wagtail.documents.blocks.DocumentChooserBlock()), ('title', wagtail.blocks.CharBlock(required=False))]))], blank=True),
        ),
    ]
