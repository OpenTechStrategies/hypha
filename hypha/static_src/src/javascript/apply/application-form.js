
(function ($) {

    'use strict';

    const ein_input = $('#ein');
    ein_input.on('input', function () {
        let formattedValue = ein_input[0].value.replace(/\D/g, '').substring(0, 9);
        formattedValue = formattedValue.replace(/(\d{2})(\d{0,7})/, '$1-$2');
        ein_input[0].value = formattedValue;
    });

    $(ein_input).on('keydown', function (event) {
        if (event.key === 'Backspace') {
            let value = $(this).val();
            if (value.endsWith('-')) {
                value = value.slice(0, -1);
                $(this).val(value);
            }
        }
    });

    let draftBtn = false;
    let submitBtn = false;
    $('#draft').click(function () {
        draftBtn = true;
    });
    $('#submitBtn').click(function () {
        submitBtn = true;
    });
    $('#draft, #submitBtn').click(function () {
        let check = false;
        const req_msg = "<div class='tooltip tooltiptext'>*Please fill out this field.</div>";
        // inputs required error
        const req = $('input').filter('[required]');
        req.each(function (index, element) {
            if (element.value === '') {
                check = true;
                $(element.parentElement).append(req_msg);
            }
        });
        const $application_form = $('.application-form');
        const rte = $application_form.find('.tiny_mce');
        // rich text field reuiqred
        if (rte) {
            let req_rte = rte.find('.form__required');
            if (req_rte != null && req_rte.length === 1) {
                let iframe = rte[0].parentElement.querySelector('iframe');
                let header = rte[0].parentElement.querySelector('.form__item');
                let text = iframe.contentDocument.querySelector('p').innerText;
                if (text.length === 0 || text === '\n') {
                    $(header).append(req_msg);
                    check = true;
                }
            }
        }
        if (check) {
            // scroll to first error
            const $error_fields = $application_form.find('.tooltip');
            if ($error_fields.length) {
                $error_fields[0].scrollIntoView();
            }
        }
        else {
            if (submitBtn) {
                togglePopUp();
            }
            else if (draftBtn) {
                $application_form.submit();
            }
        }
    });

    $('#confirm,#return').click(function () {
        togglePopUp();
    });

    $('#confirm').click(function () {
        $('#draft').removeAttr('name');
        $('#draft').removeAttr('value');
        const form = $('.application-form');
        form.submit();
    });

    function togglePopUp() {
        $('header').toggleClass('dim');
        $('footer').toggleClass('dim');
        $('.application-form').toggleClass('dim');
        $('#submission-confirmation').toggleClass('hidden');
    }

    $('.application-form').each(function () {
        var $application_form = $(this);
        var $application_form_button = $application_form.find('#submitBtn');

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
