(function ($) {
    'use strict';
    const field_blocks_ids = JSON.parse(document.getElementById('block-ids').textContent);

    let DeterminationCopy = class {
        static selector() {
            return ('#id_' + field_blocks_ids['determination']);
        }

        constructor(node) {
            this.node = node[0];
            this.bindEventListeners();
            this.actions = ['rejected', 'more_info', 'accepted'];
        }

        bindEventListeners() {

            const that = this;
            $(window).on('load', function () {
                const action = that.getActionFromLocation(window.location);
                const actionIndex = that.actions.indexOf(action);
                if (actionIndex > -1) {
                    that.node.value = actionIndex;
                }

                const newContent = that.getMatchingCopy(that.node.value);
                that.updateTextArea(newContent);
            });

            this.node.addEventListener('change', (e) => {
                /*
                 * Every time there is a change to the value
                 * in the dropdown, update the message's code
                 * with the template message.
                 */
                const newContent = this.getMatchingCopy(e.target.value);
                this.updateTextArea(newContent);
            }, false);
        }

        getActionFromLocation(location) {
            const searchParams = new URLSearchParams(location.search);
            if (searchParams.has('action')) {
                return searchParams.get('action');
            }
            return null;
        }

        getMatchingCopy(value) {
            const actionIndex = parseInt(value);
            if (actionIndex > this.actions.length - 1) {
                return '';
            }
            const action = this.actions[actionIndex];
            return document.querySelector('div[data-type="' + action + '"]').innerHTML;
        }

        updateTextArea(text) {
            window.tinyMCE.activeEditor.setContent(text, {format: 'html'});
        }
    };

    $(DeterminationCopy.selector()).each((index, el) => {
        new DeterminationCopy($(el));
    });

})(jQuery);
