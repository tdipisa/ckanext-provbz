import ckan.plugins as plugins
import ckan.plugins.toolkit as toolkit

import ckanext.provbz.helpers as helpers

class PBZThemePlugin(plugins.SingletonPlugin):
    '''An example theme plugin.
    '''

    # Declare that this class implements IConfigurer.
    plugins.implements(plugins.IConfigurer)
    plugins.implements(plugins.ITemplateHelpers)
    plugins.implements(plugins.IRoutes)

    def update_config(self, config):
        # Add this plugin's templates dir to CKAN's extra_template_paths, so
        # that CKAN will use this plugin's custom templates.
        toolkit.add_template_directory(config, 'templates')

        # Add this plugin's public dir to CKAN's extra_public_paths, so
        # that CKAN will use this plugin's custom static files.
        toolkit.add_public_directory(config, 'public')

    # see the ITemplateHelpers plugin interface.
    def get_helpers(self):
        return {
            'recent_updates': helpers.recent_updates,
            'get_default_locale': helpers.get_default_locale,
            'get_locale': helpers.get_locale,
            'getLocalizedPageLink': helpers.getLocalizedPageLink
            #'get_custom_categories_list': helpers.get_custom_categories_list
        }

    def before_map(self, map):
        map.connect('/privacy', controller='ckanext.provbz.controllers.provbz:PROVBZController', action='provbzprivacy')
        map.connect('/legal', controller='ckanext.provbz.controllers.provbz:PROVBZController', action='provbzlegal')
        map.connect('/faq', controller='ckanext.provbz.controllers.provbz:PROVBZController', action='provbzfaq')
        map.connect('/info', controller='ckanext.provbz.controllers.provbz:PROVBZController', action='provbzinfo')
        map.connect('/acknowledgements', controller='ckanext.provbz.controllers.provbz:PROVBZController', action='provbzacknowledgements')
        return map
        
    def after_map(self, route_map):
        return route_map