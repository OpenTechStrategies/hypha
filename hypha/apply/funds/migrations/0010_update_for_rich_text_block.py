# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-01-24 15:00
from __future__ import unicode_literals

from django.db import migrations
import hypha.apply.categories.blocks
import wagtail.blocks
import wagtail.blocks.static_block
import wagtail.fields


class Migration(migrations.Migration):

    dependencies = [
        ('funds', '0009_update_date_fields'),
    ]

    operations = [
        migrations.AlterField(
            model_name='applicationform',
            name='form_fields',
            field=wagtail.fields.StreamField((('text_markup', wagtail.blocks.RichTextBlock(group='Other', label='Paragraph')), ('char', wagtail.blocks.StructBlock((('field_label', wagtail.blocks.CharBlock(label='Label')), ('help_text', wagtail.blocks.TextBlock(label='Help text', required=False)), ('required', wagtail.blocks.BooleanBlock(label='Required', required=False)), ('format', wagtail.blocks.ChoiceBlock(choices=[('email', 'Email'), ('url', 'URL')], label='Format', required=False)), ('default_value', wagtail.blocks.CharBlock(label='Default value', required=False))), group='Fields')), ('text', wagtail.blocks.StructBlock((('field_label', wagtail.blocks.CharBlock(label='Label')), ('help_text', wagtail.blocks.TextBlock(label='Help text', required=False)), ('required', wagtail.blocks.BooleanBlock(label='Required', required=False)), ('default_value', wagtail.blocks.TextBlock(label='Default value', required=False))), group='Fields')), ('number', wagtail.blocks.StructBlock((('field_label', wagtail.blocks.CharBlock(label='Label')), ('help_text', wagtail.blocks.TextBlock(label='Help text', required=False)), ('required', wagtail.blocks.BooleanBlock(label='Required', required=False)), ('default_value', wagtail.blocks.CharBlock(label='Default value', required=False))), group='Fields')), ('checkbox', wagtail.blocks.StructBlock((('field_label', wagtail.blocks.CharBlock(label='Label')), ('help_text', wagtail.blocks.TextBlock(label='Help text', required=False)), ('default_value', wagtail.blocks.BooleanBlock(required=False))), group='Fields')), ('radios', wagtail.blocks.StructBlock((('field_label', wagtail.blocks.CharBlock(label='Label')), ('help_text', wagtail.blocks.TextBlock(label='Help text', required=False)), ('required', wagtail.blocks.BooleanBlock(label='Required', required=False)), ('choices', wagtail.blocks.ListBlock(wagtail.blocks.CharBlock(label='Choice')))), group='Fields')), ('dropdown', wagtail.blocks.StructBlock((('field_label', wagtail.blocks.CharBlock(label='Label')), ('help_text', wagtail.blocks.TextBlock(label='Help text', required=False)), ('required', wagtail.blocks.BooleanBlock(label='Required', required=False)), ('choices', wagtail.blocks.ListBlock(wagtail.blocks.CharBlock(label='Choice')))), group='Fields')), ('checkboxes', wagtail.blocks.StructBlock((('field_label', wagtail.blocks.CharBlock(label='Label')), ('help_text', wagtail.blocks.TextBlock(label='Help text', required=False)), ('required', wagtail.blocks.BooleanBlock(label='Required', required=False)), ('checkboxes', wagtail.blocks.ListBlock(wagtail.blocks.CharBlock(label='Checkbox')))), group='Fields')), ('date', wagtail.blocks.StructBlock((('field_label', wagtail.blocks.CharBlock(label='Label')), ('help_text', wagtail.blocks.TextBlock(label='Help text', required=False)), ('required', wagtail.blocks.BooleanBlock(label='Required', required=False)), ('default_value', wagtail.blocks.DateBlock(required=False))), group='Fields')), ('time', wagtail.blocks.StructBlock((('field_label', wagtail.blocks.CharBlock(label='Label')), ('help_text', wagtail.blocks.TextBlock(label='Help text', required=False)), ('required', wagtail.blocks.BooleanBlock(label='Required', required=False)), ('default_value', wagtail.blocks.TimeBlock(required=False))), group='Fields')), ('datetime', wagtail.blocks.StructBlock((('field_label', wagtail.blocks.CharBlock(label='Label')), ('help_text', wagtail.blocks.TextBlock(label='Help text', required=False)), ('required', wagtail.blocks.BooleanBlock(label='Required', required=False)), ('default_value', wagtail.blocks.DateTimeBlock(required=False))), group='Fields')), ('image', wagtail.blocks.StructBlock((('field_label', wagtail.blocks.CharBlock(label='Label')), ('help_text', wagtail.blocks.TextBlock(label='Help text', required=False)), ('required', wagtail.blocks.BooleanBlock(label='Required', required=False))), group='Fields')), ('file', wagtail.blocks.StructBlock((('field_label', wagtail.blocks.CharBlock(label='Label')), ('help_text', wagtail.blocks.TextBlock(label='Help text', required=False)), ('required', wagtail.blocks.BooleanBlock(label='Required', required=False))), group='Fields')), ('rich_text', wagtail.blocks.StructBlock((('field_label', wagtail.blocks.CharBlock(label='Label')), ('help_text', wagtail.blocks.TextBlock(label='Help text', required=False)), ('required', wagtail.blocks.BooleanBlock(label='Required', required=False)), ('default_value', wagtail.blocks.TextBlock(label='Default value', required=False))), group='Fields')), ('category', wagtail.blocks.StructBlock((('field_label', wagtail.blocks.CharBlock(help_text='Leave blank to use the default Category label', label='Label', required=False)), ('help_text', wagtail.blocks.TextBlock(label='Leave blank to use the default Category help text', required=False)), ('required', wagtail.blocks.BooleanBlock(label='Required', required=False)), ('category', hypha.apply.categories.blocks.ModelChooserBlock('categories.Category')), ('multi', wagtail.blocks.BooleanBlock(label='Multi select', required=False))), group='Custom')), ('title', wagtail.blocks.StructBlock((('field_label', wagtail.blocks.CharBlock(label='Label')), ('help_text', wagtail.blocks.TextBlock(label='Help text', required=False)), ('info', wagtail.blocks.static_block.StaticBlock())), group='Required')), ('value', wagtail.blocks.StructBlock((('field_label', wagtail.blocks.CharBlock(label='Label')), ('help_text', wagtail.blocks.TextBlock(label='Help text', required=False)), ('info', wagtail.blocks.static_block.StaticBlock())), group='Required')))),
        ),
    ]
