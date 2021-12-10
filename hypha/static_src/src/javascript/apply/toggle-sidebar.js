(function ($) {

    'use strict';

    function getSidebarToggle() {
        return $('.js-sidebar-toggle');
    }

    function getCurrentTab() {
        return $('.tabs__content--current');
    }

    function containsSidebar($tab) {
        return $tab.find('.sidebar').length > 0;
    }

    function showToggle($sidebarToggle) {
        return $sidebarToggle.css('visibility', 'visible');
    }

    function hideToggle($sidebarToggle) {
        return $sidebarToggle.css('visibility', 'hidden');
    }

    function showOrHideSidebarToggle() {
        var $sidebarToggle = getSidebarToggle();
        if (containsSidebar(getCurrentTab())) {
            return showToggle($sidebarToggle);
        }
        else {
            return hideToggle($sidebarToggle);
        }
    }

    var $sidebar = $('.sidebar');
    $('.tabs__container').append('<a class="tab__item tab__item--right js-sidebar-toggle" href="#">Toggle sidebar</a>');
    $('.js-sidebar-toggle').click(function (e) {
        e.preventDefault();
        $sidebar.toggleClass('hidden');
    });
    $(window).on('hashchange', showOrHideSidebarToggle);
    showOrHideSidebarToggle();

})(jQuery);

