(function ($) {

    'use strict';
    $(document).ready(function () {
        Inputmask(
            {
                prefix: '$ ',
                groupSeparator: ',',
                alias: 'numeric',
                rightAlign: false,
                allowMinus: false
            }
        ).mask($('#requested-amount'));

        Inputmask('99-9999999').mask($('#ein'));
    });

    $('.application-form').on('submit', (e) => {
        e.preventDefault();
        const form = e.target;
        let rte = form.querySelector('.tiny_mce'); // rich_text_editor
        if (rte) {
            let req = rte.querySelector('.form__required'); // check if required
            if (req != null && req.attributes.length === 1) {
                let iframe = rte.parentElement.children[1].querySelector('iframe');
                let header = rte.parentElement.children[1].querySelector('.tox-editor-header');
                let text_tag = iframe.contentDocument.querySelector('p');
                let text = iframe.contentDocument.querySelector('p').innerText;
                // remove tooltip
                $(text_tag).on('DOMSubtreeModified', function() {
                    let tooltip = rte.parentElement.children[1].querySelector('.tooltiptext');
                    if (tooltip) {
                        $(tooltip).remove();
                    }
                });
                // show tooltip or submit form
                if (text.length > 0 && text !== '\n') {
                    form.submit();
                }
                else {
                    $(header).addClass('tooltip');
                    $(header).append("<div class='tooltiptext'>This is required field.</div>");
                    header.scrollIntoView();
                }
            }
            else {
                form.submit();
            }
        }
        else {
            form.submit();
        }
    });
    $('.application-form').each(function () {
        var $application_form = $(this);
        var $application_form_button = $application_form.find('button[type="submit"]');

        // set aria-required attribute true for required fields
        $application_form.find('input[required]').each(function (index, input_field) {
            input_field.setAttribute('aria-required', true);
        });

        // add label_id as aria-describedby to help texts
        $application_form.find('.form__group').each(function (index, form_group) {
            var label_id = form_group.querySelector('label').getAttribute('for');
            if (form_group.querySelector('.form__help')) {
                form_group.querySelector('.form__help').setAttribute('aria-describedby', label_id);
            }
        });

        // set aria-invalid for field with errors
        var $error_fields = $application_form.find('.form__error');
        if ($error_fields.length) {
            // set focus to the first error field
            $error_fields[0].querySelector('input').focus();

            $error_fields.each(function (index, error_field) {
                error_field.querySelector('input').setAttribute('aria-invalid', true);
            });
        }

        // Remove the "no javascript" messages
        $('.message-no-js').detach();

        // Wait for a mouse to move, indicating they are human.
        $('body').mousemove(function () {
            // Unlock the form.
            $application_form.attr('action', '');
            $application_form_button.attr('disabled', false);
        });

        // Wait for a touch move event, indicating that they are human.
        $('body').on('touchmove', function () {
            // Unlock the form.
            $application_form.attr('action', '');
            $application_form_button.attr('disabled', false);
        });

        // A tab or enter key pressed can also indicate they are human.
        $('body').keydown(function (e) {
            if ((e.keyCode === 9) || (e.keyCode === 13)) {
                // Unlock the form.
                $application_form.attr('action', '');
                $application_form_button.attr('disabled', false);
            }
        });
    });

})(jQuery);
