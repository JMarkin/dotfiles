VERSION = "2.19.1"
from decimal import Decimal
from fastjsonschema import JsonSchemaValueException

NoneType = type(None)

def validate(data, custom_formats={}, name_prefix=None):
 validate_div_json(data, custom_formats, (name_prefix or "data") + "")
 return data

def validate_div_json(data, custom_formats={}, name_prefix=None):
 data_any_of_count1 = 0
 if not data_any_of_count1:
  try:
   validate_div_image_json(data, custom_formats, (name_prefix or "data") + "")
   data_any_of_count1 += 1
  except JsonSchemaValueException: pass
 if not data_any_of_count1:
  try:
   validate_div_gif_image_json(data, custom_formats, (name_prefix or "data") + "")
   data_any_of_count1 += 1
  except JsonSchemaValueException: pass
 if not data_any_of_count1:
  try:
   validate_div_text_json(data, custom_formats, (name_prefix or "data") + "")
   data_any_of_count1 += 1
  except JsonSchemaValueException: pass
 if not data_any_of_count1:
  try:
   validate_div_separator_json(data, custom_formats, (name_prefix or "data") + "")
   data_any_of_count1 += 1
  except JsonSchemaValueException: pass
 if not data_any_of_count1:
  try:
   validate_div_container_json(data, custom_formats, (name_prefix or "data") + "")
   data_any_of_count1 += 1
  except JsonSchemaValueException: pass
 if not data_any_of_count1:
  try:
   validate_div_grid_json(data, custom_formats, (name_prefix or "data") + "")
   data_any_of_count1 += 1
  except JsonSchemaValueException: pass
 if not data_any_of_count1:
  try:
   validate_div_gallery_json(data, custom_formats, (name_prefix or "data") + "")
   data_any_of_count1 += 1
  except JsonSchemaValueException: pass
 if not data_any_of_count1:
  try:
   validate_div_pager_json(data, custom_formats, (name_prefix or "data") + "")
   data_any_of_count1 += 1
  except JsonSchemaValueException: pass
 if not data_any_of_count1:
  try:
   validate_div_tabs_json(data, custom_formats, (name_prefix or "data") + "")
   data_any_of_count1 += 1
  except JsonSchemaValueException: pass
 if not data_any_of_count1:
  try:
   validate_div_state_json(data, custom_formats, (name_prefix or "data") + "")
   data_any_of_count1 += 1
  except JsonSchemaValueException: pass
 if not data_any_of_count1:
  try:
   validate_div_custom_json(data, custom_formats, (name_prefix or "data") + "")
   data_any_of_count1 += 1
  except JsonSchemaValueException: pass
 if not data_any_of_count1:
  try:
   validate_div_indicator_json(data, custom_formats, (name_prefix or "data") + "")
   data_any_of_count1 += 1
  except JsonSchemaValueException: pass
 if not data_any_of_count1:
  try:
   validate_div_slider_json(data, custom_formats, (name_prefix or "data") + "")
   data_any_of_count1 += 1
  except JsonSchemaValueException: pass
 if not data_any_of_count1:
  try:
   validate_div_input_json(data, custom_formats, (name_prefix or "data") + "")
   data_any_of_count1 += 1
  except JsonSchemaValueException: pass
 if not data_any_of_count1:
  try:
   validate_div_select_json(data, custom_formats, (name_prefix or "data") + "")
   data_any_of_count1 += 1
  except JsonSchemaValueException: pass
 if not data_any_of_count1:
  try:
   validate_div_video_json(data, custom_formats, (name_prefix or "data") + "")
   data_any_of_count1 += 1
  except JsonSchemaValueException: pass
 if not data_any_of_count1:
  if not (isinstance(data, str) and '@' in data):
   raise JsonSchemaValueException("" + (name_prefix or "data") + " cannot be validated by any definition", value=data, name="" + (name_prefix or "data") + "", definition={'generate_case_for_templates_kotlinDsl': True, 'generate_case_for_templates_typescript': True, 'anyOf': [{'java_extends': 'DivBlockWithId', '$description': 'translations.json#/div_image', 'codegen': {'divan': {'forced_properties_order': ['image_url']}}, 'allOf': [{'$ref': 'div-base.json'}, {'$ref': 'div-actionable.json'}, {'$ref': 'div-image-base.json'}, {'properties': {'image_url': {'$ref': 'common.json#/url', '$description': 'translations.json#/div_image_image_url'}, 'high_priority_preview_show': {'$ref': 'common.json#/boolean_int', 'default_value': 'false', '$description': 'translations.json#/div_image_high_priority_preview_show', 'platforms': ['android', 'ios']}, 'type': {'type': 'string', 'enum': ['image']}, 'tint_mode': {'$ref': 'div-blend-mode.json', 'default_value': 'source_in', '$description': 'translations.json#/div_image_tint_mode'}, 'tint_color': {'$ref': 'common.json#/color', '$description': 'translations.json#/div_image_tint_color'}, 'appearance_animation': {'$ref': 'div-fade-transition.json', '$description': 'translations.json#/div_image_appearance_animation'}, 'filters': {'type': 'array', 'items': {'$ref': 'div-filter.json'}, 'minItems': 1, '$description': 'translations.json#/div_filter'}}}], 'required': ['image_url', 'type'], '$schema': 'http://json-schema.org/draft-07/schema'}, {'java_extends': 'DivBlockWithId', '$description': 'translations.json#/div_gif_image', 'allOf': [{'$ref': 'div-base.json'}, {'$ref': 'div-actionable.json'}, {'$ref': 'div-image-base.json'}, {'properties': {'gif_url': {'$ref': 'common.json#/url', '$description': 'translations.json#/div_gif_image_gif_url'}, 'type': {'type': 'string', 'enum': ['gif']}}}], 'required': ['gif_url', 'type'], '$schema': 'http://json-schema.org/draft-07/schema'}, {'java_extends': 'DivBlockWithId', '$description': 'translations.json#/div_text', 'codegen': {'divan': {'forced_properties_order': ['text']}}, 'definitions': {'range': {'type': 'object', 'properties': {'start': {'$ref': 'common.json#/non_negative_integer', '$description': 'translations.json#/div_text_range_start'}, 'end': {'$ref': 'common.json#/positive_integer', '$description': 'translations.json#/div_text_range_end'}, 'font_size': {'$ref': 'common.json#/non_negative_integer', '$description': 'translations.json#/div_font_size'}, 'font_family': {'$ref': 'common.json#/non_empty_string', '$description': 'translations.json#/div_font_family'}, 'font_size_unit': {'$ref': 'div-size-unit.json', 'default_value': 'sp', '$description': 'translations.json#/div_font_size_unit', 'platforms': ['android', 'ios']}, 'letter_spacing': {'type': 'number', '$description': 'translations.json#/div_text_range_letter_spacing'}, 'font_weight': {'$ref': 'div-font-weight.json', '$description': 'translations.json#/div_font_weight'}, 'text_color': {'$ref': 'common.json#/color', '$description': 'translations.json#/div_text_color'}, 'underline': {'$ref': 'div-line-style.json', '$description': 'translations.json#/div_text_range_underline'}, 'strike': {'$ref': 'div-line-style.json', '$description': 'translations.json#/div_text_range_strike'}, 'actions': {'type': 'array', 'items': {'$ref': 'div-action.json'}, 'minItems': 1, '$description': 'translations.json#/div_text_range_actions'}, 'line_height': {'$ref': 'common.json#/non_negative_integer', '$description': 'translations.json#/div_text_range_line_height'}, 'top_offset': {'$ref': 'common.json#/non_negative_integer', '$description': 'translations.json#/div_text_range_top_offset'}, 'border': {'$ref': 'div-text-range-border.json', '$description': 'translations.json#/div_text_range_border'}, 'background': {'$ref': 'div-text-range-background.json', '$description': 'translations.json#/div_text_range_background'}, 'text_shadow': {'$ref': 'div-shadow.json', '$description': 'translations.json#/div_text_range_shadow', 'platforms': ['android']}}, 'required': ['start', 'end'], '$description': 'translations.json#/div_text_range'}, 'image': {'type': 'object', 'properties': {'start': {'$ref': 'common.json#/non_negative_integer', '$description': 'translations.json#/div_text_image_start'}, 'url': {'$ref': 'common.json#/url', '$description': 'translations.json#/div_text_image_url'}, 'width': {'$ref': 'div-fixed-size.json', 'default_value': '{"type": "fixed","value":20}', '$description': 'translations.json#/div_text_image_width'}, 'height': {'$ref': 'div-fixed-size.json', 'default_value': '{"type": "fixed","value":20}', '$description': 'translations.json#/div_text_image_height'}, 'tint_color': {'$ref': 'common.json#/color', '$description': 'translations.json#/div_text_image_tint_color'}, 'tint_mode': {'$ref': 'div-blend-mode.json', 'default_value': 'source_in', '$description': 'translations.json#/div_text_image_tint_mode', 'platforms': ['android', 'web']}}, 'required': ['url', 'start'], '$description': 'translations.json#/div_text_image'}, 'ellipsis': {'type': 'object', 'properties': {'text': {'$ref': 'common.json#/non_empty_string', '$description': 'translations.json#/div_text_ellipsis_text'}, 'actions': {'type': 'array', 'items': {'$ref': 'div-action.json'}, 'minItems': 1, '$description': 'translations.json#/div_text_ellipsis_actions'}, 'ranges': {'type': 'array', 'items': {'$ref': '#/definitions/range'}, 'minItems': 1, '$description': 'translations.json#/div_text_ellipsis_ranges'}, 'images': {'type': 'array', 'items': {'$ref': '#/definitions/image'}, 'minItems': 1, '$description': 'translations.json#/div_text_ellipsis_images'}}, 'required': ['text'], '$description': 'translations.json#/div_text_ellipsis', 'platforms': ['android', 'ios']}}, 'allOf': [{'$ref': 'div-base.json'}, {'$ref': 'div-actionable.json'}, {'properties': {'type': {'type': 'string', 'enum': ['text']}, 'font_size': {'$ref': 'common.json#/non_negative_integer', 'default_value': '12', '$description': 'translations.json#/div_font_size'}, 'font_family': {'$ref': 'common.json#/non_empty_string', '$description': 'translations.json#/div_font_family'}, 'font_size_unit': {'$ref': 'div-size-unit.json', 'default_value': 'sp', 'platforms': ['android', 'ios']}, 'line_height': {'$ref': 'common.json#/non_negative_integer', '$description': 'translations.json#/div_text_line_height'}, 'max_lines': {'$ref': 'common.json#/non_negative_integer', '$description': 'translations.json#/div_text_max_lines'}, 'min_hidden_lines': {'$ref': 'common.json#/non_negative_integer', '$description': 'translations.json#/div_text_min_hidden_lines', 'platforms': ['android', 'ios']}, 'auto_ellipsize': {'$ref': 'common.json#/boolean_int', '$description': 'translations.json#/div_text_auto_ellipsize', 'platforms': ['android']}, 'letter_spacing': {'type': 'number', 'default_value': '0', '$description': 'translations.json#/div_text_letter_spacing'}, 'font_weight': {'$ref': 'div-font-weight.json', 'default_value': 'regular', '$description': 'translations.json#/div_font_weight'}, 'text_alignment_horizontal': {'$ref': 'div-alignment-horizontal.json', 'default_value': 'start', '$description': 'translations.json#/div_text_text_alignment_horizontal'}, 'text_alignment_vertical': {'$ref': 'div-alignment-vertical.json', 'default_value': 'top', '$description': 'translations.json#/div_text_text_alignment_vertical'}, 'text_color': {'$ref': 'common.json#/color', 'default_value': '#FF000000', '$description': 'translations.json#/div_text_text_color'}, 'focused_text_color': {'$ref': 'common.json#/color', '$description': 'translations.json#/div_text_focused_text_color', 'platforms': ['android', 'web']}, 'text_gradient': {'$ref': 'div-text-gradient.json', '$description': 'translations.json#/div_text_text_gradient'}, 'text': {'$ref': 'common.json#/non_empty_string', 'client_optimized': True, '$description': 'translations.json#/div_text_text'}, 'underline': {'$ref': 'div-line-style.json', 'default_value': 'none', '$description': 'translations.json#/div_text_underline'}, 'strike': {'$ref': 'div-line-style.json', 'default_value': 'none', '$description': 'translations.json#/div_text_strike'}, 'ranges': {'type': 'array', 'items': {'$ref': '#/definitions/range'}, 'minItems': 1, '$description': 'translations.json#/div_text_ranges'}, 'images': {'type': 'array', 'items': {'$ref': '#/definitions/image'}, 'minItems': 1, '$description': 'translations.json#/div_text_images'}, 'ellipsis': {'$ref': '#/definitions/ellipsis'}, 'selectable': {'$ref': 'common.json#/boolean_int', 'default_value': 'false', '$description': 'translations.json#/div_text_selectable'}, 'truncate': {'type': 'string', 'enum': ['none', 'start', 'end', 'middle'], 'default_value': 'end', '$description': 'translations.json#/div_text_truncate', 'deprecated': True, 'code_generation_disabled_kotlin': True, 'code_generation_disabled_swift': True}, 'text_shadow': {'$ref': 'div-shadow.json', '$description': 'translations.json#/div_text_shadow', 'platforms': ['android']}}}], 'required': ['type', 'text'], '$schema': 'http://json-schema.org/draft-07/schema'}, {'java_extends': 'DivBlockWithId', '$description': 'translations.json#/div_separator', 'definitions': {'style': {'type': 'object', 'properties': {'color': {'$ref': 'common.json#/color', 'default_value': '#14000000', '$description': 'translations.json#/div_separator_style_color'}, 'orientation': {'type': 'string', 'enum': ['vertical', 'horizontal'], 'default_value': 'horizontal', '$description': 'translations.json#/div_separator_style_orientation'}}}}, 'allOf': [{'$ref': 'div-base.json'}, {'$ref': 'div-actionable.json'}, {'properties': {'delimiter_style': {'$ref': '#/definitions/style', '$description': 'translations.json#/div_separator_delimiter_style'}, 'type': {'type': 'string', 'enum': ['separator']}}, 'required': ['type']}], '$schema': 'http://json-schema.org/draft-07/schema'}, {'java_extends': 'DivBlockWithId', '$description': 'translations.json#/div_container', 'codegen': {'divan': {'forced_properties_order': ['orientation'], 'factories': {'row': {'vararg_property': 'items', 'inlines': {'orientation': 'horizontal'}}, 'column': {'vararg_property': 'items', 'inlines': {'orientation': 'vertical'}}, 'stack': {'vararg_property': 'items', 'inlines': {'orientation': 'overlap'}}}}, 'swift': {'generate_optional_arguments': False}}, 'definitions': {'separator': {'type': 'object', 'properties': {'show_at_start': {'$ref': 'common.json#/boolean_int', '$description': 'translations.json#/div_container_separator_show_at_start', 'default_value': 'false'}, 'show_between': {'$ref': 'common.json#/boolean_int', '$description': 'translations.json#/div_container_separator_show_between', 'default_value': 'true'}, 'show_at_end': {'$ref': 'common.json#/boolean_int', '$description': 'translations.json#/div_container_separator_show_at_end', 'default_value': 'false'}, 'style': {'$ref': 'div-drawable.json', '$description': 'translations.json#/div_container_separator_style'}, 'margins': {'$ref': 'div-edge-insets.json', '$description': 'translations.json#/div_base_margins'}}, 'required': ['style']}}, 'allOf': [{'$ref': 'div-base.json'}, {'$ref': 'div-actionable.json'}, {'properties': {'type': {'type': 'string', 'enum': ['container']}, 'content_alignment_vertical': {'$ref': 'div-content-alignment-vertical.json', 'default_value': 'top', '$description': 'translations.json#/div_container_content_alignment_vertical'}, 'content_alignment_horizontal': {'$ref': 'div-content-alignment-horizontal.json', 'default_value': 'start', '$description': 'translations.json#/div_container_content_alignment_horizontal'}, 'orientation': {'type': 'string', 'enum': ['vertical', 'horizontal', 'overlap'], 'default_value': 'vertical', '$description': 'translations.json#/div_container_orientation'}, 'layout_mode': {'type': 'string', 'enum': ['no_wrap', 'wrap'], 'default_value': 'no_wrap', '$description': 'translations.json#/div_container_layout_mode'}, 'separator': {'$ref': '#/definitions/separator', '$description': 'translations.json#/div_container_separator'}, 'line_separator': {'$ref': '#/definitions/separator', '$description': 'translations.json#/div_container_line_separator'}, 'items': {'type': 'array', 'items': {'$ref': 'div.json'}, 'minItems': 1, '$description': 'translations.json#/div_container_items'}, 'aspect': {'$ref': 'div-aspect.json', '$description': 'translations.json#/div_container_aspect'}}}], 'required': ['type', 'items'], '$schema': 'http://json-schema.org/draft-07/schema'}, {'java_extends': 'DivBlockWithId', '$description': 'translations.json#/div_grid', 'codegen': {'swift': {'generate_optional_arguments': False}}, 'allOf': [{'$ref': 'div-base.json'}, {'$ref': 'div-actionable.json'}, {'properties': {'content_alignment_vertical': {'$ref': 'div-alignment-vertical.json', 'default_value': 'top', '$description': 'translations.json#/div_grid_content_alignment_vertical'}, 'content_alignment_horizontal': {'$ref': 'div-alignment-horizontal.json', 'default_value': 'start', '$description': 'translations.json#/div_grid_content_alignment_horizontal'}, 'items': {'type': 'array', 'items': {'$ref': 'div.json'}, 'minItems': 1, 'strictParsing': True, '$description': 'translations.json#/div_grid_items'}, 'column_count': {'$ref': 'common.json#/non_negative_integer', '$description': 'translations.json#/div_grid_column_count'}, 'type': {'type': 'string', 'enum': ['grid']}}}], 'required': ['items', 'column_count', 'type'], '$schema': 'http://json-schema.org/draft-07/schema'}, {'java_extends': 'DivBlockWithId', '$description': 'translations.json#/div_gallery', 'codegen': {'swift': {'generate_optional_arguments': False}}, 'allOf': [{'$ref': 'div-base.json'}, {'properties': {'type': {'type': 'string', 'enum': ['gallery']}, 'cross_content_alignment': {'$description': 'translations.json#/div_gallery_cross_content_alignment', 'version': '2.1', 'type': 'string', 'enum': ['start', 'center', 'end'], 'default_value': 'start'}, 'column_count': {'$ref': 'common.json#/positive_integer', '$description': 'translations.json#/div_gallery_column_count'}, 'item_spacing': {'$ref': 'common.json#/non_negative_integer', 'default_value': '8', '$description': 'translations.json#/div_gallery_item_spacing'}, 'cross_spacing': {'$ref': 'common.json#/non_negative_integer', '$description': 'translations.json#/div_gallery_cross_spacing'}, 'scroll_mode': {'type': 'string', 'default_value': 'default', 'enum': ['paging', 'default'], '$description': 'translations.json#/div_gallery_scroll_mode'}, 'items': {'type': 'array', 'items': {'$ref': 'div.json'}, 'minItems': 1, '$description': 'translations.json#/div_gallery_items'}, 'orientation': {'type': 'string', 'default_value': 'horizontal', 'enum': ['horizontal', 'vertical'], '$description': 'translations.json#/div_gallery_orientation'}, 'restrict_parent_scroll': {'$ref': 'common.json#/boolean_int', 'default_value': 'false', '$description': 'translations.json#/div_gallery_restrict_parent_scroll', 'platforms': ['android', 'web']}, 'default_item': {'$ref': 'common.json#/non_negative_integer', 'default_value': '0', '$description': 'translations.json#/div_gallery_default_item'}}}], 'required': ['type', 'items'], '$schema': 'http://json-schema.org/draft-07/schema'}, {'java_extends': 'DivBlockWithId', '$description': 'translations.json#/div_pager', 'codegen': {'swift': {'generate_optional_arguments': False}}, 'allOf': [{'$ref': 'div-base.json'}, {'properties': {'type': {'type': 'string', 'enum': ['pager']}, 'layout_mode': {'$ref': 'div-pager-layout-mode.json', '$description': 'translations.json#/div_pager_layout_mode'}, 'item_spacing': {'$ref': 'div-fixed-size.json', 'default_value': '{"type": "fixed","value":0}', '$description': 'translations.json#/div_pager_item_spacing'}, 'items': {'type': 'array', 'items': {'$ref': 'div.json'}, 'minItems': 1, '$description': 'translations.json#/div_pager_items'}, 'orientation': {'type': 'string', 'default_value': 'horizontal', 'enum': ['horizontal', 'vertical'], '$description': 'translations.json#/div_pager_orientation'}, 'restrict_parent_scroll': {'$ref': 'common.json#/boolean_int', 'default_value': 'false', '$description': 'translations.json#/div_pager_restrict_parent_scroll', 'platforms': ['android', 'web']}, 'default_item': {'$ref': 'common.json#/non_negative_integer', 'default_value': '0', '$description': 'translations.json#/div_pager_default_item'}, 'infinite_scroll': {'$ref': 'common.json#/boolean_int', 'default_value': 'false', '$description': 'translations.json#/div_pager_infinite_scroll', 'platforms': []}}}], 'required': ['type', 'items', 'layout_mode'], '$schema': 'http://json-schema.org/draft-07/schema'}, {'java_extends': 'DivBlockWithId', '$description': 'translations.json#/div_tabs', 'codegen': {'swift': {'generate_optional_arguments': False}}, 'definitions': {'item': {'type': 'object', 'codegen': {'swift': {'generate_optional_arguments': False}}, 'properties': {'title': {'$ref': 'common.json#/non_empty_string', '$description': 'translations.json#/div_tabs_item_title'}, 'title_click_action': {'$ref': 'div-action.json', '$description': 'translations.json#/div_tabs_item_title_click_action'}, 'div': {'$ref': 'div.json', '$description': 'translations.json#/div_tabs_item_div'}}, 'required': ['title', 'div'], '$description': 'translations.json#/div_tabs_item'}}, 'allOf': [{'$ref': 'div-base.json'}, {'properties': {'type': {'type': 'string', 'enum': ['tabs']}, 'title_paddings': {'$ref': 'div-edge-insets.json', 'default_value': '{"left": 12,"right": 12,"top": 0,"bottom": 8}', '$description': 'translations.json#/div_tabs_title_paddings'}, 'separator_paddings': {'$ref': 'div-edge-insets.json', 'default_value': '{"left": 12,"right": 12,"top": 0,"bottom": 0}', '$description': 'translations.json#/div_tabs_separator_paddings'}, 'tab_title_style': {'type': 'object', 'properties': {'font_size': {'$ref': 'common.json#/non_negative_integer', 'default_value': '12', '$description': 'translations.json#/div_tabs_tab_title_style_font_size'}, 'font_size_unit': {'$ref': 'div-size-unit.json', 'default_value': 'sp', '$description': 'translations.json#/div_tabs_tab_title_style_font_size_unit', 'platforms': ['android', 'ios']}, 'paddings': {'$ref': 'div-edge-insets.json', 'default_value': '{"left": 8,"right": 8,"top": 6,"bottom": 6}', '$description': 'translations.json#/div_tabs_tab_title_style_paddings'}, 'item_spacing': {'$ref': 'common.json#/non_negative_integer', 'default_value': '0', '$description': 'translations.json#/div_tabs_tab_title_style_item_spacing'}, 'line_height': {'$ref': 'common.json#/non_negative_integer', '$description': 'translations.json#/div_tabs_tab_title_style_line_height'}, 'letter_spacing': {'type': 'number', 'default_value': '0', '$description': 'translations.json#/div_tabs_tab_title_style_letter_spacing'}, 'font_weight': {'$ref': 'div-font-weight.json', 'default_value': 'regular', '$description': 'translations.json#/div_tabs_tab_title_style_font_weight', 'deprecated': True}, 'active_font_weight': {'$ref': 'div-font-weight.json', '$description': 'translations.json#/div_tabs_tab_title_style_active_font_weight'}, 'inactive_font_weight': {'$ref': 'div-font-weight.json', '$description': 'translations.json#/div_tabs_tab_title_style_inactive_font_weight'}, 'font_family': {'$ref': 'common.json#/non_empty_string', '$description': 'translations.json#/div_font_family'}, 'active_text_color': {'$ref': 'common.json#/color', 'default_value': '#CC000000', '$description': 'translations.json#/div_tabs_tab_title_style_active_text_color'}, 'inactive_text_color': {'$ref': 'common.json#/color', 'default_value': '#80000000', '$description': 'translations.json#/div_tabs_tab_title_style_inactive_text_color'}, 'active_background_color': {'$ref': 'common.json#/color', 'default_value': '#FFFFDC60', '$description': 'translations.json#/div_tabs_tab_title_style_active_background_color'}, 'inactive_background_color': {'$ref': 'common.json#/color', '$description': 'translations.json#/div_tabs_tab_title_style_inactive_background_color'}, 'corner_radius': {'$ref': 'common.json#/non_negative_integer', '$description': 'translations.json#/div_tabs_tab_title_style_corner_radius'}, 'corners_radius': {'$ref': 'div-corners-radius.json', '$description': 'translations.json#/div_tabs_tab_title_style_corners_radius'}, 'animation_type': {'type': 'string', 'enum': ['slide', 'fade', 'none'], 'default_value': 'slide', '$description': 'translations.json#/div_tabs_tab_title_style_animation_type', 'platforms': ['android', 'ios']}, 'animation_duration': {'$ref': 'common.json#/non_negative_integer', 'default_value': '300', '$description': 'translations.json#/div_tabs_tab_title_style_animation_duration'}}, '$description': 'translations.json#/div_tabs_tab_title_style'}, 'selected_tab': {'$ref': 'common.json#/non_negative_integer', 'default_value': '0', '$description': 'translations.json#/div_tabs_selected_tab'}, 'has_separator': {'$ref': 'common.json#/boolean_int', 'default_value': 'false', '$description': 'translations.json#/div_tabs_has_separator'}, 'switch_tabs_by_content_swipe_enabled': {'$ref': 'common.json#/boolean_int', 'default_value': 'true', '$description': 'translations.json#/div_tabs_switch_tabs_by_content_swipe_enabled'}, 'separator_color': {'$ref': 'common.json#/color', 'default_value': '#14000000', '$description': 'translations.json#/div_tabs_separator_color'}, 'items': {'type': 'array', 'items': {'$ref': '#/definitions/item'}, 'minItems': 1, '$description': 'translations.json#/div_tabs_items'}, 'dynamic_height': {'$ref': 'common.json#/boolean_int', 'default_value': 'false', '$description': 'translations.json#/div_tabs_dynamic_height', 'platforms': ['android', 'ios']}, 'restrict_parent_scroll': {'$ref': 'common.json#/boolean_int', 'default_value': 'false', '$description': 'translations.json#/div_tabs_restrict_parent_scroll', 'platforms': ['android', 'web']}}}], 'required': ['type', 'items'], '$schema': 'http://json-schema.org/draft-07/schema'}, {'java_extends': 'DivBlockWithId', '$description': 'translations.json#/div_state', 'codegen': {'swift': {'generate_optional_arguments': False}}, 'definitions': {'div_state': {'type': 'object', 'alias_divan': 'item', 'codegen': {'swift': {'generate_optional_arguments': False}}, 'properties': {'state_id': {'type': 'string', 'supports_expressions': False, '$description': 'translations.json#/div_state_div_state_state_id'}, 'div': {'$ref': 'div.json', '$description': 'translations.json#/div_state_div_state_div'}, 'animation_in': {'$ref': 'div-animation.json', '$description': 'translations.json#/div_state_div_state_animation_in', 'platforms': ['android', 'ios'], 'deprecated': True}, 'animation_out': {'$ref': 'div-animation.json', '$description': 'translations.json#/div_state_div_state_animation_out', 'platforms': ['android', 'ios'], 'deprecated': True}, 'swipe_out_actions': {'type': 'array', 'items': {'$ref': 'div-action.json'}, 'minItems': 1, '$description': 'translations.json#/div_state_div_state_swipe_out_actions', 'platforms': ['android'], 'deprecated': True}}, 'required': ['state_id']}}, 'allOf': [{'$ref': 'div-base.json'}, {'properties': {'type': {'type': 'string', 'enum': ['state']}, 'states': {'type': 'array', 'items': {'$ref': '#/definitions/div_state'}, 'minItems': 1, '$description': 'translations.json#/div_state_states'}, 'state_id_variable': {'$ref': 'div-variable-name.json', '$description': 'translations.json#/div_state_state_id_variable', 'platforms': ['web', 'android']}, 'div_id': {'type': 'string', 'supports_expressions': False, '$description': 'translations.json#/div_state_div_id', 'deprecated': True}, 'default_state_id': {'type': 'string', '$description': 'translations.json#/div_state_default_state_id'}, 'transition_animation_selector': {'$ref': 'div-transition-selector.json', 'default_value': 'state_change', '$description': 'translations.json#/div_state_transition_animation_selector', 'deprecated': True}}, 'required': ['type', 'states']}], '$schema': 'http://json-schema.org/draft-07/schema'}, {'java_extends': 'DivBlockWithId', '$description': 'translations.json#/div_custom', 'allOf': [{'$ref': 'div-base.json'}, {'properties': {'type': {'type': 'string', 'enum': ['custom']}, 'items': {'type': 'array', 'items': {'$ref': 'div.json'}, 'minItems': 1, '$description': 'translations.json#/div_custom_items'}, 'custom_type': {'type': 'string', 'supports_expressions': False, '$description': 'translations.json#/div_custom_custom_type'}, 'custom_props': {'type': 'object', 'additionalProperties': True, '$description': 'translations.json#/div_custom_custom_props'}}}], 'required': ['type', 'custom_type'], '$schema': 'http://json-schema.org/draft-07/schema'}, {'java_extends': 'DivBlockWithId', '$description': 'translations.json#/div_indicator', 'allOf': [{'$ref': 'div-base.json'}, {'properties': {'type': {'type': 'string', 'enum': ['indicator']}, 'pager_id': {'type': 'string', 'supports_expressions': False, '$description': 'translations.json#/div_indicator_pager_id'}, 'items_placement': {'$ref': 'div-indicator-item-placement.json', '$description': 'translations.json#/div_indicator_item_placement'}, 'space_between_centers': {'$ref': 'div-fixed-size.json', 'default_value': '{"type": "fixed","value":15}', '$description': 'translations.json#/div_indicator_space_between_centers', 'deprecated': True}, 'inactive_item_color': {'$ref': 'common.json#/color', 'default_value': '#33919cb5', '$description': 'translations.json#/div_indicator_inactive_item_color', 'deprecated': True}, 'active_item_color': {'$ref': 'common.json#/color', 'default_value': '#ffdc60', '$description': 'translations.json#/div_indicator_active_item_color', 'deprecated': True}, 'shape': {'$ref': 'div-shape.json', 'default_value': '{"type":"rounded_rectangle"}', '$description': 'translations.json#/div_indicator_shape', 'deprecated': True}, 'active_item_size': {'$ref': 'common.json#/positive_number', 'default_value': '1.3', '$description': 'translations.json#/div_indicator_active_item_size', 'deprecated': True}, 'minimum_item_size': {'$ref': 'common.json#/positive_number', 'default_value': '0.5', '$description': 'translations.json#/div_indicator_minimum_item_size', 'platforms': ['android', 'ios'], 'deprecated': True}, 'active_shape': {'$ref': 'div-rounded-rectangle-shape.json', '$description': 'translations.json#/div_indicator_active_shape'}, 'inactive_shape': {'$ref': 'div-rounded-rectangle-shape.json', '$description': 'translations.json#/div_indicator_inactive_shape'}, 'inactive_minimum_shape': {'$ref': 'div-rounded-rectangle-shape.json', '$description': 'translations.json#/div_indicator_inactive_minimum_shape', 'platforms': ['android', 'ios']}, 'animation': {'type': 'string', 'enum': ['scale', 'worm', 'slider'], 'default_value': 'scale', '$description': 'translations.json#/div_indicator_animation', 'platforms': ['android', 'ios']}}}], 'required': ['type'], '$schema': 'http://json-schema.org/draft-07/schema'}, {'java_extends': 'DivBlockWithId', '$description': 'translations.json#/div_slider', 'definitions': {'text_style': {'type': 'object', 'properties': {'font_size': {'$ref': 'common.json#/non_negative_integer', '$description': 'translations.json#/div_font_size'}, 'font_size_unit': {'$ref': 'div-size-unit.json', 'default_value': 'sp', 'platforms': ['android']}, 'font_weight': {'$ref': 'div-font-weight.json', 'default_value': 'regular', '$description': 'translations.json#/div_font_weight'}, 'text_color': {'$ref': 'common.json#/color', 'default_value': '#FF000000', '$description': 'translations.json#/div_text_color'}, 'offset': {'$ref': 'div-point.json', '$description': 'translations.json#/div_slider_text_style_offset'}}, 'required': ['font_size']}, 'range': {'type': 'object', 'properties': {'start': {'type': 'integer', '$description': 'translations.json#/div_slider_range_start'}, 'end': {'type': 'integer', '$description': 'translations.json#/div_slider_range_end'}, 'track_active_style': {'$ref': 'div-drawable.json', '$description': 'translations.json#/div_slider_track_active_style'}, 'track_inactive_style': {'$ref': 'div-drawable.json', '$description': 'translations.json#/div_slider_track_inactive_style'}, 'margins': {'$ref': 'div-edge-insets.json', '$description': 'translations.json#/div_slider_range_margins'}}}}, 'allOf': [{'$ref': 'div-base.json'}, {'properties': {'type': {'type': 'string', 'enum': ['slider']}, 'min_value': {'type': 'integer', 'default_value': '0', '$description': 'translations.json#/div_slider_min_value'}, 'max_value': {'type': 'integer', 'default_value': '100', '$description': 'translations.json#/div_slider_max_value'}, 'thumb_value_variable': {'$ref': 'div-variable-name.json', '$description': 'translations.json#/div_slider_thumb_value_variable'}, 'thumb_secondary_value_variable': {'$ref': 'div-variable-name.json', '$description': 'translations.json#/div_slider_thumb_secondary_value_variable'}, 'thumb_style': {'$ref': 'div-drawable.json', '$description': 'translations.json#/div_slider_thumb_style'}, 'thumb_secondary_style': {'$ref': 'div-drawable.json', '$description': 'translations.json#/div_slider_thumb_secondary_style'}, 'thumb_text_style': {'$ref': '#/definitions/text_style', '$description': 'translations.json#/div_slider_thumb_text_style'}, 'thumb_secondary_text_style': {'$ref': '#/definitions/text_style', '$description': 'translations.json#/div_slider_thumb_secondary_text_style'}, 'track_active_style': {'$ref': 'div-drawable.json', '$description': 'translations.json#/div_slider_track_active_style'}, 'tick_mark_active_style': {'$ref': 'div-drawable.json', '$description': 'translations.json#/div_slider_tick_mark_active_style'}, 'track_inactive_style': {'$ref': 'div-drawable.json', '$description': 'translations.json#/div_slider_track_inactive_style'}, 'tick_mark_inactive_style': {'$ref': 'div-drawable.json', '$description': 'translations.json#/div_slider_tick_mark_inactive_style'}, 'ranges': {'type': 'array', 'items': {'$ref': '#/definitions/range'}, 'minItems': 1, '$description': 'translations.json#/div_slider_ranges', 'platforms': ['android', 'ios']}, 'secondary_value_accessibility': {'$ref': 'div-accessibility.json', '$description': 'translations.json#/div_slider_secondary_value_accessibility', 'platforms': ['web']}}}], 'required': ['type', 'thumb_style', 'track_active_style', 'track_inactive_style'], '$schema': 'http://json-schema.org/draft-07/schema'}, {'java_extends': 'DivBlockWithId', '$description': 'translations.json#/div_input', 'definitions': {'native_interface': {'type': 'object', 'properties': {'color': {'$ref': 'common.json#/color', '$description': 'translations.json#/div_input_native_interface_color'}}, 'required': ['color']}}, 'allOf': [{'$ref': 'div-base.json'}, {'properties': {'type': {'type': 'string', 'enum': ['input']}, 'font_size': {'$ref': 'common.json#/non_negative_integer', 'default_value': '12', '$description': 'translations.json#/div_font_size'}, 'font_size_unit': {'$ref': 'div-size-unit.json', 'default_value': 'sp', '$description': 'translations.json#/div_font_size_unit'}, 'font_family': {'$ref': 'common.json#/non_empty_string', '$description': 'translations.json#/div_font_family'}, 'font_weight': {'$ref': 'div-font-weight.json', 'default_value': 'regular', '$description': 'translations.json#/div_font_weight'}, 'text_color': {'$ref': 'common.json#/color', 'default_value': '#FF000000', '$description': 'translations.json#/div_text_color'}, 'text_variable': {'$ref': 'div-variable-name.json', '$description': 'translations.json#/div_input_text_variable'}, 'text_alignment_horizontal': {'$ref': 'div-alignment-horizontal.json', 'default_value': 'start', '$description': 'translations.json#/div_text_text_alignment_horizontal', 'platforms': ['android', 'web']}, 'text_alignment_vertical': {'$ref': 'div-alignment-vertical.json', 'default_value': 'center', '$description': 'translations.json#/div_text_text_alignment_vertical', 'platforms': ['android', 'web']}, 'line_height': {'$ref': 'common.json#/non_negative_integer', '$description': 'translations.json#/div_input_line_height'}, 'max_visible_lines': {'$ref': 'common.json#/positive_integer', '$description': 'translations.json#/div_input_max_visible_lines'}, 'letter_spacing': {'type': 'number', 'default_value': '0', '$description': 'translations.json#/div_input_letter_spacing'}, 'hint_text': {'$ref': 'common.json#/non_empty_string', '$description': 'translations.json#/div_input_hint_text'}, 'hint_color': {'$ref': 'common.json#/color', 'default_value': '#73000000', '$description': 'translations.json#/div_input_hint_color'}, 'highlight_color': {'$ref': 'common.json#/color', '$description': 'translations.json#/div_input_highlight_color'}, 'native_interface': {'$ref': '#/definitions/native_interface', '$description': 'translations.json#/div_input_native_interface', 'platforms': ['android']}, 'keyboard_type': {'type': 'string', 'enum': ['single_line_text', 'multi_line_text', 'phone', 'number', 'email', 'uri'], 'default_value': 'multi_line_text', '$description': 'translations.json#/div_input_keyboard_type'}, 'select_all_on_focus': {'$ref': 'common.json#/boolean_int', 'default_value': 'false', '$description': 'translations.json#/div_input_select_all_on_focus'}, 'mask': {'$ref': 'div-input-mask.json', '$description': 'translations.json#/div_input_mask'}, 'validators': {'type': 'array', '$description': 'translations.json#/div_input_validators', 'platforms': ['android', 'ios'], 'items': {'$ref': 'div-input-validator.json'}}}}], 'required': ['type', 'text_variable'], '$schema': 'http://json-schema.org/draft-07/schema'}, {'java_extends': 'DivBlockWithId', '$description': 'translations.json#/div_select', 'definitions': {'option': {'type': 'object', 'properties': {'text': {'type': 'string', '$description': 'translations.json#/div_select_option_text'}, 'value': {'type': 'string', '$description': 'translations.json#/div_select_option_value'}}, 'required': ['value']}}, 'allOf': [{'$ref': 'div-base.json'}, {'properties': {'type': {'type': 'string', 'enum': ['select']}, 'options': {'type': 'array', 'items': {'$ref': '#/definitions/option', '$description': 'translations.json#/div_select_option'}, 'minItems': 1}, 'value_variable': {'$ref': 'div-variable-name.json', '$description': 'translations.json#/div_select_value_variable'}, 'font_size': {'$ref': 'common.json#/non_negative_integer', 'default_value': '12', '$description': 'translations.json#/div_font_size'}, 'font_size_unit': {'$ref': 'div-size-unit.json', 'default_value': 'sp', '$description': 'translations.json#/div_font_size_unit', 'platforms': ['android', 'ios']}, 'font_family': {'$ref': 'common.json#/non_empty_string', '$description': 'translations.json#/div_font_family'}, 'font_weight': {'$ref': 'div-font-weight.json', 'default_value': 'regular', '$description': 'translations.json#/div_font_weight'}, 'hint_text': {'$ref': 'common.json#/non_empty_string', '$description': 'translations.json#/div_select_hint_text'}, 'hint_color': {'$ref': 'common.json#/color', 'default_value': '#73000000', '$description': 'translations.json#/div_select_hint_color'}, 'line_height': {'$ref': 'common.json#/non_negative_integer', '$description': 'translations.json#/div_select_line_height'}, 'text_color': {'$ref': 'common.json#/color', 'default_value': '#FF000000', '$description': 'translations.json#/div_text_color'}, 'letter_spacing': {'type': 'number', 'default_value': '0', '$description': 'translations.json#/div_select_letter_spacing'}}}], 'required': ['type', 'options', 'value_variable'], '$schema': 'http://json-schema.org/draft-07/schema'}, {'java_extends': 'DivBlockWithId', '$description': 'translations.json#/div_video', 'allOf': [{'$ref': 'div-base.json'}, {'properties': {'type': {'type': 'string', 'enum': ['video']}, 'video_sources': {'type': 'array', 'items': {'$ref': 'div-video-source.json', '$description': 'translations.json#/div_video_source'}, 'minItems': 1}, 'repeatable': {'$ref': 'common.json#/boolean_int', 'default_value': 'false', '$description': 'translations.json#/div_video_repeatable'}, 'autostart': {'$ref': 'common.json#/boolean_int', 'default_value': 'false', '$description': 'translations.json#/div_video_autostart'}, 'muted': {'$ref': 'common.json#/boolean_int', 'default_value': 'false', '$description': 'translations.json#/div_video_muted'}, 'preview': {'$ref': 'common.json#/non_empty_string', '$description': 'translations.json#/div_video_preview'}, 'elapsed_time_variable': {'$ref': 'div-variable-name.json', '$description': 'translations.json#/div_video_elapsed_time_variable'}, 'resume_actions': {'type': 'array', 'items': {'$ref': 'div-action.json'}, 'minItems': 1, '$description': 'translations.json#/div_video_resume_actions'}, 'pause_actions': {'type': 'array', 'items': {'$ref': 'div-action.json'}, 'minItems': 1, '$description': 'translations.json#/div_video_pause_actions'}, 'end_actions': {'type': 'array', 'items': {'$ref': 'div-action.json'}, 'minItems': 1, '$description': 'translations.json#/div_video_end_actions'}, 'buffering_actions': {'type': 'array', 'items': {'$ref': 'div-action.json'}, 'minItems': 1, '$description': 'translations.json#/div_video_buffering_actions'}, 'fatal_actions': {'type': 'array', 'items': {'$ref': 'div-action.json'}, 'minItems': 1, '$description': 'translations.json#/div_video_fatal_actions'}, 'player_settings_payload': {'type': 'object', 'additionalProperties': True, '$description': 'translations.json#/div_video_player_settings_payload', 'platforms': ['android', 'ios']}, 'aspect': {'$ref': 'div-aspect.json', '$description': 'translations.json#/div_aspect', 'platforms': []}, 'scale': {'$ref': 'div-video-scale.json', 'default_value': 'fit', '$description': 'translations.json#/div_video_scale', 'platforms': ['web']}}}], 'required': ['type', 'video_sources'], '$schema': 'http://json-schema.org/draft-07/schema'}], '$schema': 'http://json-schema.org/draft-07/schema'}, rule='anyOf')
 return data

def validate_div_video_json(data, custom_formats={}, name_prefix=None):
 validate_div_base_json(data, custom_formats, (name_prefix or "data") + "")
 data_is_dict = isinstance(data, dict)
 if data_is_dict:
  data_keys = set(data.keys())
  if "type" in data_keys:
   data_keys.remove("type")
   data__type = data["type"]
   if not isinstance(data__type, (str)):
    if not (isinstance(data__type, str) and '@' in data__type):
     raise JsonSchemaValueException("" + (name_prefix or "data") + ".type must be string", value=data__type, name="" + (name_prefix or "data") + ".type", definition={'type': 'string', 'enum': ['video']}, rule='type')
   if data__type not in ['video']:
    if not (isinstance(data__type, str) and '@' in data__type):
     raise JsonSchemaValueException("" + (name_prefix or "data") + ".type must be one of ['video']", value=data__type, name="" + (name_prefix or "data") + ".type", definition={'type': 'string', 'enum': ['video']}, rule='enum')
  if "video_sources" in data_keys:
   data_keys.remove("video_sources")
   data__videosources = data["video_sources"]
   if not isinstance(data__videosources, (list, tuple)):
    if not (isinstance(data__videosources, str) and '@' in data__videosources):
     raise JsonSchemaValueException("" + (name_prefix or "data") + ".video_sources must be array", value=data__videosources, name="" + (name_prefix or "data") + ".video_sources", definition={'type': 'array', 'items': {'definitions': {'resolution': {'type': 'object', 'properties': {'type': {'type': 'string', 'enum': ['resolution']}, 'width': {'$ref': 'common.json#/positive_integer', '$description': 'translations.json#/div_video_source_resolution_width'}, 'height': {'$ref': 'common.json#/positive_integer', '$description': 'translations.json#/div_video_source_resolution_height'}}, 'required': ['type', 'width', 'height']}}, 'type': 'object', 'properties': {'type': {'type': 'string', 'enum': ['video_source']}, 'url': {'$ref': 'common.json#/url', '$description': 'translations.json#/div_video_source_url'}, 'resolution': {'$ref': '#/definitions/resolution', '$description': 'translations.json#/div_video_source_resolution'}, 'mime_type': {'type': 'string', '$description': 'translations.json#/div_video_source_mime_type'}, 'bitrate': {'type': 'integer', '$description': 'translations.json#/div_video_source_bitrate'}}, 'required': ['type', 'url', 'mime_type'], '$schema': 'http://json-schema.org/draft-07/schema'}, 'minItems': 1}, rule='type')
   data__videosources_is_list = isinstance(data__videosources, (list, tuple))
   if data__videosources_is_list:
    data__videosources_len = len(data__videosources)
    if data__videosources_len < 1:
     if not (isinstance(data__videosources, str) and '@' in data__videosources):
      raise JsonSchemaValueException("" + (name_prefix or "data") + ".video_sources must contain at least 1 items", value=data__videosources, name="" + (name_prefix or "data") + ".video_sources", definition={'type': 'array', 'items': {'definitions': {'resolution': {'type': 'object', 'properties': {'type': {'type': 'string', 'enum': ['resolution']}, 'width': {'$ref': 'common.json#/positive_integer', '$description': 'translations.json#/div_video_source_resolution_width'}, 'height': {'$ref': 'common.json#/positive_integer', '$description': 'translations.json#/div_video_source_resolution_height'}}, 'required': ['type', 'width', 'height']}}, 'type': 'object', 'properties': {'type': {'type': 'string', 'enum': ['video_source']}, 'url': {'$ref': 'common.json#/url', '$description': 'translations.json#/div_video_source_url'}, 'resolution': {'$ref': '#/definitions/resolution', '$description': 'translations.json#/div_video_source_resolution'}, 'mime_type': {'type': 'string', '$description': 'translations.json#/div_video_source_mime_type'}, 'bitrate': {'type': 'integer', '$description': 'translations.json#/div_video_source_bitrate'}}, 'required': ['type', 'url', 'mime_type'], '$schema': 'http://json-schema.org/draft-07/schema'}, 'minItems': 1}, rule='minItems')
    for data__videosources_x, data__videosources_item in enumerate(data__videosources):
     validate_div_video_source_json(data__videosources_item, custom_formats, (name_prefix or "data") + ".video_sources[{data__videosources_x}]".format(**locals()))
  if "repeatable" in data_keys:
   data_keys.remove("repeatable")
   data__repeatable = data["repeatable"]
   validate_common_json__boolean_int(data__repeatable, custom_formats, (name_prefix or "data") + ".repeatable")
  if "autostart" in data_keys:
   data_keys.remove("autostart")
   data__autostart = data["autostart"]
   validate_common_json__boolean_int(data__autostart, custom_formats, (name_prefix or "data") + ".autostart")
  if "muted" in data_keys:
   data_keys.remove("muted")
   data__muted = data["muted"]
   validate_common_json__boolean_int(data__muted, custom_formats, (name_prefix or "data") + ".muted")
  if "preview" in data_keys:
   data_keys.remove("preview")
   data__preview = data["preview"]
   validate_common_json__non_empty_string(data__preview, custom_formats, (name_prefix or "data") + ".preview")
  if "elapsed_time_variable" in data_keys:
   data_keys.remove("elapsed_time_variable")
   data__elapsedtimevariable = data["elapsed_time_variable"]
   validate_div_variable_name_json(data__elapsedtimevariable, custom_formats, (name_prefix or "data") + ".elapsed_time_variable")
  if "resume_actions" in data_keys:
   data_keys.remove("resume_actions")
   data__resumeactions = data["resume_actions"]
   if not isinstance(data__resumeactions, (list, tuple)):
    if not (isinstance(data__resumeactions, str) and '@' in data__resumeactions):
     raise JsonSchemaValueException("" + (name_prefix or "data") + ".resume_actions must be array", value=data__resumeactions, name="" + (name_prefix or "data") + ".resume_actions", definition={'type': 'array', 'items': {'definitions': {'menu_item': {'type': 'object', 'properties': {'text': {'$ref': 'common.json#/non_empty_string', '$description': 'translations.json#/div_action_menu_item_text'}, 'action': {'$ref': 'div-action.json', '$description': 'translations.json#/div_action_menu_item_action'}, 'actions': {'type': 'array', 'items': {'$ref': 'div-action.json'}, 'minItems': 1, '$description': 'translations.json#/div_action_menu_item_actions'}}, 'required': ['text']}}, 'allOf': [{'$ref': 'div-action-base.json'}, {'type': 'object', '$description': 'translations.json#/div_action', 'properties': {'menu_items': {'type': 'array', 'items': {'$ref': '#/definitions/menu_item'}, '$description': 'translations.json#/div_action_menu_items', 'platforms': ['android', 'ios']}, 'log_url': {'$ref': 'common.json#/url', '$description': 'translations.json#/div_action_log_url'}, 'target': {'type': 'string', 'enum': ['_self', '_blank'], 'force_enum_field': True, '$description': 'translations.json#/div_action_target', 'platforms': ['web'], 'code_generation_disabled_swift': True}}, 'required': ['log_id']}], '$schema': 'http://json-schema.org/draft-07/schema'}, 'minItems': 1, '$description': 'translations.json#/div_video_resume_actions'}, rule='type')
   data__resumeactions_is_list = isinstance(data__resumeactions, (list, tuple))
   if data__resumeactions_is_list:
    data__resumeactions_len = len(data__resumeactions)
    if data__resumeactions_len < 1:
     if not (isinstance(data__resumeactions, str) and '@' in data__resumeactions):
      raise JsonSchemaValueException("" + (name_prefix or "data") + ".resume_actions must contain at least 1 items", value=data__resumeactions, name="" + (name_prefix or "data") + ".resume_actions", definition={'type': 'array', 'items': {'definitions': {'menu_item': {'type': 'object', 'properties': {'text': {'$ref': 'common.json#/non_empty_string', '$description': 'translations.json#/div_action_menu_item_text'}, 'action': {'$ref': 'div-action.json', '$description': 'translations.json#/div_action_menu_item_action'}, 'actions': {'type': 'array', 'items': {'$ref': 'div-action.json'}, 'minItems': 1, '$description': 'translations.json#/div_action_menu_item_actions'}}, 'required': ['text']}}, 'allOf': [{'$ref': 'div-action-base.json'}, {'type': 'object', '$description': 'translations.json#/div_action', 'properties': {'menu_items': {'type': 'array', 'items': {'$ref': '#/definitions/menu_item'}, '$description': 'translations.json#/div_action_menu_items', 'platforms': ['android', 'ios']}, 'log_url': {'$ref': 'common.json#/url', '$description': 'translations.json#/div_action_log_url'}, 'target': {'type': 'string', 'enum': ['_self', '_blank'], 'force_enum_field': True, '$description': 'translations.json#/div_action_target', 'platforms': ['web'], 'code_generation_disabled_swift': True}}, 'required': ['log_id']}], '$schema': 'http://json-schema.org/draft-07/schema'}, 'minItems': 1, '$description': 'translations.json#/div_video_resume_actions'}, rule='minItems')
    for data__resumeactions_x, data__resumeactions_item in enumerate(data__resumeactions):
     validate_div_action_json(data__resumeactions_item, custom_formats, (name_prefix or "data") + ".resume_actions[{data__resumeactions_x}]".format(**locals()))
  if "pause_actions" in data_keys:
   data_keys.remove("pause_actions")
   data__pauseactions = data["pause_actions"]
   if not isinstance(data__pauseactions, (list, tuple)):
    if not (isinstance(data__pauseactions, str) and '@' in data__pauseactions):
     raise JsonSchemaValueException("" + (name_prefix or "data") + ".pause_actions must be array", value=data__pauseactions, name="" + (name_prefix or "data") + ".pause_actions", definition={'type': 'array', 'items': {'definitions': {'menu_item': {'type': 'object', 'properties': {'text': {'$ref': 'common.json#/non_empty_string', '$description': 'translations.json#/div_action_menu_item_text'}, 'action': {'$ref': 'div-action.json', '$description': 'translations.json#/div_action_menu_item_action'}, 'actions': {'type': 'array', 'items': {'$ref': 'div-action.json'}, 'minItems': 1, '$description': 'translations.json#/div_action_menu_item_actions'}}, 'required': ['text']}}, 'allOf': [{'$ref': 'div-action-base.json'}, {'type': 'object', '$description': 'translations.json#/div_action', 'properties': {'menu_items': {'type': 'array', 'items': {'$ref': '#/definitions/menu_item'}, '$description': 'translations.json#/div_action_menu_items', 'platforms': ['android', 'ios']}, 'log_url': {'$ref': 'common.json#/url', '$description': 'translations.json#/div_action_log_url'}, 'target': {'type': 'string', 'enum': ['_self', '_blank'], 'force_enum_field': True, '$description': 'translations.json#/div_action_target', 'platforms': ['web'], 'code_generation_disabled_swift': True}}, 'required': ['log_id']}], '$schema': 'http://json-schema.org/draft-07/schema'}, 'minItems': 1, '$description': 'translations.json#/div_video_pause_actions'}, rule='type')
   data__pauseactions_is_list = isinstance(data__pauseactions, (list, tuple))
   if data__pauseactions_is_list:
    data__pauseactions_len = len(data__pauseactions)
    if data__pauseactions_len < 1:
     if not (isinstance(data__pauseactions, str) and '@' in data__pauseactions):
      raise JsonSchemaValueException("" + (name_prefix or "data") + ".pause_actions must contain at least 1 items", value=data__pauseactions, name="" + (name_prefix or "data") + ".pause_actions", definition={'type': 'array', 'items': {'definitions': {'menu_item': {'type': 'object', 'properties': {'text': {'$ref': 'common.json#/non_empty_string', '$description': 'translations.json#/div_action_menu_item_text'}, 'action': {'$ref': 'div-action.json', '$description': 'translations.json#/div_action_menu_item_action'}, 'actions': {'type': 'array', 'items': {'$ref': 'div-action.json'}, 'minItems': 1, '$description': 'translations.json#/div_action_menu_item_actions'}}, 'required': ['text']}}, 'allOf': [{'$ref': 'div-action-base.json'}, {'type': 'object', '$description': 'translations.json#/div_action', 'properties': {'menu_items': {'type': 'array', 'items': {'$ref': '#/definitions/menu_item'}, '$description': 'translations.json#/div_action_menu_items', 'platforms': ['android', 'ios']}, 'log_url': {'$ref': 'common.json#/url', '$description': 'translations.json#/div_action_log_url'}, 'target': {'type': 'string', 'enum': ['_self', '_blank'], 'force_enum_field': True, '$description': 'translations.json#/div_action_target', 'platforms': ['web'], 'code_generation_disabled_swift': True}}, 'required': ['log_id']}], '$schema': 'http://json-schema.org/draft-07/schema'}, 'minItems': 1, '$description': 'translations.json#/div_video_pause_actions'}, rule='minItems')
    for data__pauseactions_x, data__pauseactions_item in enumerate(data__pauseactions):
     validate_div_action_json(data__pauseactions_item, custom_formats, (name_prefix or "data") + ".pause_actions[{data__pauseactions_x}]".format(**locals()))
  if "end_actions" in data_keys:
   data_keys.remove("end_actions")
   data__endactions = data["end_actions"]
   if not isinstance(data__endactions, (list, tuple)):
    if not (isinstance(data__endactions, str) and '@' in data__endactions):
     raise JsonSchemaValueException("" + (name_prefix or "data") + ".end_actions must be array", value=data__endactions, name="" + (name_prefix or "data") + ".end_actions", definition={'type': 'array', 'items': {'definitions': {'menu_item': {'type': 'object', 'properties': {'text': {'$ref': 'common.json#/non_empty_string', '$description': 'translations.json#/div_action_menu_item_text'}, 'action': {'$ref': 'div-action.json', '$description': 'translations.json#/div_action_menu_item_action'}, 'actions': {'type': 'array', 'items': {'$ref': 'div-action.json'}, 'minItems': 1, '$description': 'translations.json#/div_action_menu_item_actions'}}, 'required': ['text']}}, 'allOf': [{'$ref': 'div-action-base.json'}, {'type': 'object', '$description': 'translations.json#/div_action', 'properties': {'menu_items': {'type': 'array', 'items': {'$ref': '#/definitions/menu_item'}, '$description': 'translations.json#/div_action_menu_items', 'platforms': ['android', 'ios']}, 'log_url': {'$ref': 'common.json#/url', '$description': 'translations.json#/div_action_log_url'}, 'target': {'type': 'string', 'enum': ['_self', '_blank'], 'force_enum_field': True, '$description': 'translations.json#/div_action_target', 'platforms': ['web'], 'code_generation_disabled_swift': True}}, 'required': ['log_id']}], '$schema': 'http://json-schema.org/draft-07/schema'}, 'minItems': 1, '$description': 'translations.json#/div_video_end_actions'}, rule='type')
   data__endactions_is_list = isinstance(data__endactions, (list, tuple))
   if data__endactions_is_list:
    data__endactions_len = len(data__endactions)
    if data__endactions_len < 1:
     if not (isinstance(data__endactions, str) and '@' in data__endactions):
      raise JsonSchemaValueException("" + (name_prefix or "data") + ".end_actions must contain at least 1 items", value=data__endactions, name="" + (name_prefix or "data") + ".end_actions", definition={'type': 'array', 'items': {'definitions': {'menu_item': {'type': 'object', 'properties': {'text': {'$ref': 'common.json#/non_empty_string', '$description': 'translations.json#/div_action_menu_item_text'}, 'action': {'$ref': 'div-action.json', '$description': 'translations.json#/div_action_menu_item_action'}, 'actions': {'type': 'array', 'items': {'$ref': 'div-action.json'}, 'minItems': 1, '$description': 'translations.json#/div_action_menu_item_actions'}}, 'required': ['text']}}, 'allOf': [{'$ref': 'div-action-base.json'}, {'type': 'object', '$description': 'translations.json#/div_action', 'properties': {'menu_items': {'type': 'array', 'items': {'$ref': '#/definitions/menu_item'}, '$description': 'translations.json#/div_action_menu_items', 'platforms': ['android', 'ios']}, 'log_url': {'$ref': 'common.json#/url', '$description': 'translations.json#/div_action_log_url'}, 'target': {'type': 'string', 'enum': ['_self', '_blank'], 'force_enum_field': True, '$description': 'translations.json#/div_action_target', 'platforms': ['web'], 'code_generation_disabled_swift': True}}, 'required': ['log_id']}], '$schema': 'http://json-schema.org/draft-07/schema'}, 'minItems': 1, '$description': 'translations.json#/div_video_end_actions'}, rule='minItems')
    for data__endactions_x, data__endactions_item in enumerate(data__endactions):
     validate_div_action_json(data__endactions_item, custom_formats, (name_prefix or "data") + ".end_actions[{data__endactions_x}]".format(**locals()))
  if "buffering_actions" in data_keys:
   data_keys.remove("buffering_actions")
   data__bufferingactions = data["buffering_actions"]
   if not isinstance(data__bufferingactions, (list, tuple)):
    if not (isinstance(data__bufferingactions, str) and '@' in data__bufferingactions):
     raise JsonSchemaValueException("" + (name_prefix or "data") + ".buffering_actions must be array", value=data__bufferingactions, name="" + (name_prefix or "data") + ".buffering_actions", definition={'type': 'array', 'items': {'definitions': {'menu_item': {'type': 'object', 'properties': {'text': {'$ref': 'common.json#/non_empty_string', '$description': 'translations.json#/div_action_menu_item_text'}, 'action': {'$ref': 'div-action.json', '$description': 'translations.json#/div_action_menu_item_action'}, 'actions': {'type': 'array', 'items': {'$ref': 'div-action.json'}, 'minItems': 1, '$description': 'translations.json#/div_action_menu_item_actions'}}, 'required': ['text']}}, 'allOf': [{'$ref': 'div-action-base.json'}, {'type': 'object', '$description': 'translations.json#/div_action', 'properties': {'menu_items': {'type': 'array', 'items': {'$ref': '#/definitions/menu_item'}, '$description': 'translations.json#/div_action_menu_items', 'platforms': ['android', 'ios']}, 'log_url': {'$ref': 'common.json#/url', '$description': 'translations.json#/div_action_log_url'}, 'target': {'type': 'string', 'enum': ['_self', '_blank'], 'force_enum_field': True, '$description': 'translations.json#/div_action_target', 'platforms': ['web'], 'code_generation_disabled_swift': True}}, 'required': ['log_id']}], '$schema': 'http://json-schema.org/draft-07/schema'}, 'minItems': 1, '$description': 'translations.json#/div_video_buffering_actions'}, rule='type')
   data__bufferingactions_is_list = isinstance(data__bufferingactions, (list, tuple))
   if data__bufferingactions_is_list:
    data__bufferingactions_len = len(data__bufferingactions)
    if data__bufferingactions_len < 1:
     if not (isinstance(data__bufferingactions, str) and '@' in data__bufferingactions):
      raise JsonSchemaValueException("" + (name_prefix or "data") + ".buffering_actions must contain at least 1 items", value=data__bufferingactions, name="" + (name_prefix or "data") + ".buffering_actions", definition={'type': 'array', 'items': {'definitions': {'menu_item': {'type': 'object', 'properties': {'text': {'$ref': 'common.json#/non_empty_string', '$description': 'translations.json#/div_action_menu_item_text'}, 'action': {'$ref': 'div-action.json', '$description': 'translations.json#/div_action_menu_item_action'}, 'actions': {'type': 'array', 'items': {'$ref': 'div-action.json'}, 'minItems': 1, '$description': 'translations.json#/div_action_menu_item_actions'}}, 'required': ['text']}}, 'allOf': [{'$ref': 'div-action-base.json'}, {'type': 'object', '$description': 'translations.json#/div_action', 'properties': {'menu_items': {'type': 'array', 'items': {'$ref': '#/definitions/menu_item'}, '$description': 'translations.json#/div_action_menu_items', 'platforms': ['android', 'ios']}, 'log_url': {'$ref': 'common.json#/url', '$description': 'translations.json#/div_action_log_url'}, 'target': {'type': 'string', 'enum': ['_self', '_blank'], 'force_enum_field': True, '$description': 'translations.json#/div_action_target', 'platforms': ['web'], 'code_generation_disabled_swift': True}}, 'required': ['log_id']}], '$schema': 'http://json-schema.org/draft-07/schema'}, 'minItems': 1, '$description': 'translations.json#/div_video_buffering_actions'}, rule='minItems')
    for data__bufferingactions_x, data__bufferingactions_item in enumerate(data__bufferingactions):
     validate_div_action_json(data__bufferingactions_item, custom_formats, (name_prefix or "data") + ".buffering_actions[{data__bufferingactions_x}]".format(**locals()))
  if "fatal_actions" in data_keys:
   data_keys.remove("fatal_actions")
   data__fatalactions = data["fatal_actions"]
   if not isinstance(data__fatalactions, (list, tuple)):
    if not (isinstance(data__fatalactions, str) and '@' in data__fatalactions):
     raise JsonSchemaValueException("" + (name_prefix or "data") + ".fatal_actions must be array", value=data__fatalactions, name="" + (name_prefix or "data") + ".fatal_actions", definition={'type': 'array', 'items': {'definitions': {'menu_item': {'type': 'object', 'properties': {'text': {'$ref': 'common.json#/non_empty_string', '$description': 'translations.json#/div_action_menu_item_text'}, 'action': {'$ref': 'div-action.json', '$description': 'translations.json#/div_action_menu_item_action'}, 'actions': {'type': 'array', 'items': {'$ref': 'div-action.json'}, 'minItems': 1, '$description': 'translations.json#/div_action_menu_item_actions'}}, 'required': ['text']}}, 'allOf': [{'$ref': 'div-action-base.json'}, {'type': 'object', '$description': 'translations.json#/div_action', 'properties': {'menu_items': {'type': 'array', 'items': {'$ref': '#/definitions/menu_item'}, '$description': 'translations.json#/div_action_menu_items', 'platforms': ['android', 'ios']}, 'log_url': {'$ref': 'common.json#/url', '$description': 'translations.json#/div_action_log_url'}, 'target': {'type': 'string', 'enum': ['_self', '_blank'], 'force_enum_field': True, '$description': 'translations.json#/div_action_target', 'platforms': ['web'], 'code_generation_disabled_swift': True}}, 'required': ['log_id']}], '$schema': 'http://json-schema.org/draft-07/schema'}, 'minItems': 1, '$description': 'translations.json#/div_video_fatal_actions'}, rule='type')
   data__fatalactions_is_list = isinstance(data__fatalactions, (list, tuple))
   if data__fatalactions_is_list:
    data__fatalactions_len = len(data__fatalactions)
    if data__fatalactions_len < 1:
     if not (isinstance(data__fatalactions, str) and '@' in data__fatalactions):
      raise JsonSchemaValueException("" + (name_prefix or "data") + ".fatal_actions must contain at least 1 items", value=data__fatalactions, name="" + (name_prefix or "data") + ".fatal_actions", definition={'type': 'array', 'items': {'definitions': {'menu_item': {'type': 'object', 'properties': {'text': {'$ref': 'common.json#/non_empty_string', '$description': 'translations.json#/div_action_menu_item_text'}, 'action': {'$ref': 'div-action.json', '$description': 'translations.json#/div_action_menu_item_action'}, 'actions': {'type': 'array', 'items': {'$ref': 'div-action.json'}, 'minItems': 1, '$description': 'translations.json#/div_action_menu_item_actions'}}, 'required': ['text']}}, 'allOf': [{'$ref': 'div-action-base.json'}, {'type': 'object', '$description': 'translations.json#/div_action', 'properties': {'menu_items': {'type': 'array', 'items': {'$ref': '#/definitions/menu_item'}, '$description': 'translations.json#/div_action_menu_items', 'platforms': ['android', 'ios']}, 'log_url': {'$ref': 'common.json#/url', '$description': 'translations.json#/div_action_log_url'}, 'target': {'type': 'string', 'enum': ['_self', '_blank'], 'force_enum_field': True, '$description': 'translations.json#/div_action_target', 'platforms': ['web'], 'code_generation_disabled_swift': True}}, 'required': ['log_id']}], '$schema': 'http://json-schema.org/draft-07/schema'}, 'minItems': 1, '$description': 'translations.json#/div_video_fatal_actions'}, rule='minItems')
    for data__fatalactions_x, data__fatalactions_item in enumerate(data__fatalactions):
     validate_div_action_json(data__fatalactions_item, custom_formats, (name_prefix or "data") + ".fatal_actions[{data__fatalactions_x}]".format(**locals()))
  if "player_settings_payload" in data_keys:
   data_keys.remove("player_settings_payload")
   data__playersettingspayload = data["player_settings_payload"]
   if not isinstance(data__playersettingspayload, (dict)):
    if not (isinstance(data__playersettingspayload, str) and '@' in data__playersettingspayload):
     raise JsonSchemaValueException("" + (name_prefix or "data") + ".player_settings_payload must be object", value=data__playersettingspayload, name="" + (name_prefix or "data") + ".player_settings_payload", definition={'type': 'object', 'additionalProperties': True, '$description': 'translations.json#/div_video_player_settings_payload', 'platforms': ['android', 'ios']}, rule='type')
   data__playersettingspayload_is_dict = isinstance(data__playersettingspayload, dict)
   if data__playersettingspayload_is_dict:
    data__playersettingspayload_keys = set(data__playersettingspayload.keys())
  if "aspect" in data_keys:
   data_keys.remove("aspect")
   data__aspect = data["aspect"]
   validate_div_aspect_json(data__aspect, custom_formats, (name_prefix or "data") + ".aspect")
  if "scale" in data_keys:
   data_keys.remove("scale")
   data__scale = data["scale"]
   validate_div_video_scale_json(data__scale, custom_formats, (name_prefix or "data") + ".scale")
 data_is_dict = isinstance(data, dict)
 if data_is_dict:
  data__missing_keys = set(['type', 'video_sources']) - data.keys()
  if data__missing_keys:
   if not (isinstance(data, str) and '@' in data):
    raise JsonSchemaValueException("" + (name_prefix or "data") + " must contain " + (str(sorted(data__missing_keys)) + " properties"), value=data, name="" + (name_prefix or "data") + "", definition={'java_extends': 'DivBlockWithId', '$description': 'translations.json#/div_video', 'allOf': [{'protocol_name': 'div-base', 'codegen': {'swift': {'super_protocol': 'DivBlockModeling'}, 'documentation': {'include_in_toc': True}}, 'type': 'object', 'properties': {'id': {'$ref': 'common.json#/non_empty_string', 'supports_expressions': False, '$description': 'translations.json#/div_base_id'}, 'border': {'$ref': 'div-border.json', '$description': 'translations.json#/div_base_border'}, 'width': {'$ref': 'div-size.json', 'default_value': '{"type": "match_parent"}', '$description': 'translations.json#/div_base_width'}, 'height': {'$ref': 'div-size.json', 'default_value': '{"type": "wrap_content"}', '$description': 'translations.json#/div_base_height'}, 'background': {'type': 'array', 'items': {'$ref': 'div-background.json'}, 'minItems': 1, '$description': 'translations.json#/div_base_background'}, 'paddings': {'$ref': 'div-edge-insets.json', '$description': 'translations.json#/div_base_paddings'}, 'margins': {'$ref': 'div-edge-insets.json', '$description': 'translations.json#/div_base_margins'}, 'alpha': {'type': 'number', 'default_value': '1.0', 'constraint': 'number >= 0.0 && number <= 1.0', '$description': 'translations.json#/div_base_alpha'}, 'alignment_vertical': {'$ref': 'div-alignment-vertical.json', '$description': 'translations.json#/div_base_alignment_vertical'}, 'alignment_horizontal': {'$ref': 'div-alignment-horizontal.json', '$description': 'translations.json#/div_base_alignment_horizontal'}, 'row_span': {'$ref': 'common.json#/non_negative_integer', '$description': 'translations.json#/div_base_row_span'}, 'column_span': {'$ref': 'common.json#/non_negative_integer', '$description': 'translations.json#/div_base_column_span'}, 'visibility_action': {'$ref': 'div-visibility-action.json', '$description': 'translations.json#/div_base_visibility_action'}, 'visibility_actions': {'type': 'array', 'items': {'$ref': 'div-visibility-action.json'}, 'minItems': 1, '$description': 'translations.json#/div_base_visibility_actions'}, 'disappear_actions': {'type': 'array', 'items': {'$ref': 'div-disappear-action.json'}, 'minItems': 1, '$description': 'translations.json#/div_base_disappear_actions'}, 'tooltips': {'type': 'array', 'items': {'$ref': 'div-tooltip.json'}, 'minItems': 1, '$description': 'translations.json#/div_base_tooltips'}, 'accessibility': {'$ref': 'div-accessibility.json', '$description': 'translations.json#/div_base_accessibility'}, 'extensions': {'type': 'array', 'items': {'$ref': 'div-extension.json'}, 'minItems': 1, '$description': 'translations.json#/div_base_extensions'}, 'transition_triggers': {'type': 'array', 'items': {'$ref': 'div-transition-trigger.json'}, 'minItems': 1, 'supports_expressions': False, '$description': 'translations.json#/div_base_transition_triggers'}, 'transition_in': {'$ref': 'div-appearance-transition.json', '$description': 'translations.json#/div_base_transition_in'}, 'transition_change': {'$ref': 'div-change-transition.json', '$description': 'translations.json#/div_base_transition_change'}, 'transition_out': {'$ref': 'div-appearance-transition.json', '$description': 'translations.json#/div_base_transition_out'}, 'selected_actions': {'type': 'array', 'items': {'$ref': 'div-action.json'}, 'minItems': 1, '$description': 'translations.json#/div_base_selected_actions'}, 'focus': {'$ref': 'div-focus.json', '$description': 'translations.json#/div_base_focus', 'platforms': ['android', 'ios']}, 'visibility': {'$ref': 'div-visibility.json', '$description': 'translations.json#/div_base_visibility', 'default_value': 'visible'}, 'transform': {'$ref': 'div-transform.json', '$description': 'translations.json#/div_base_transform'}}, '$schema': 'http://json-schema.org/draft-07/schema'}, {'properties': {'type': {'type': 'string', 'enum': ['video']}, 'video_sources': {'type': 'array', 'items': {'definitions': {'resolution': {'type': 'object', 'properties': {'type': {'type': 'string', 'enum': ['resolution']}, 'width': {'$ref': 'common.json#/positive_integer', '$description': 'translations.json#/div_video_source_resolution_width'}, 'height': {'$ref': 'common.json#/positive_integer', '$description': 'translations.json#/div_video_source_resolution_height'}}, 'required': ['type', 'width', 'height']}}, 'type': 'object', 'properties': {'type': {'type': 'string', 'enum': ['video_source']}, 'url': {'$ref': 'common.json#/url', '$description': 'translations.json#/div_video_source_url'}, 'resolution': {'$ref': '#/definitions/resolution', '$description': 'translations.json#/div_video_source_resolution'}, 'mime_type': {'type': 'string', '$description': 'translations.json#/div_video_source_mime_type'}, 'bitrate': {'type': 'integer', '$description': 'translations.json#/div_video_source_bitrate'}}, 'required': ['type', 'url', 'mime_type'], '$schema': 'http://json-schema.org/draft-07/schema'}, 'minItems': 1}, 'repeatable': {'oneOf': [{'type': 'boolean'}, {'type': 'integer', 'enum': [0, 1]}]}, 'autostart': {'oneOf': [{'type': 'boolean'}, {'type': 'integer', 'enum': [0, 1]}]}, 'muted': {'oneOf': [{'type': 'boolean'}, {'type': 'integer', 'enum': [0, 1]}]}, 'preview': {'type': 'string', 'minLength': 1, 'clientMinLength': 1}, 'elapsed_time_variable': {'supports_expressions': False, '$ref': 'common.json#/non_empty_string', '$schema': 'http://json-schema.org/draft-07/schema'}, 'resume_actions': {'type': 'array', 'items': {'definitions': {'menu_item': {'type': 'object', 'properties': {'text': {'$ref': 'common.json#/non_empty_string', '$description': 'translations.json#/div_action_menu_item_text'}, 'action': {'$ref': 'div-action.json', '$description': 'translations.json#/div_action_menu_item_action'}, 'actions': {'type': 'array', 'items': {'$ref': 'div-action.json'}, 'minItems': 1, '$description': 'translations.json#/div_action_menu_item_actions'}}, 'required': ['text']}}, 'allOf': [{'$ref': 'div-action-base.json'}, {'type': 'object', '$description': 'translations.json#/div_action', 'properties': {'menu_items': {'type': 'array', 'items': {'$ref': '#/definitions/menu_item'}, '$description': 'translations.json#/div_action_menu_items', 'platforms': ['android', 'ios']}, 'log_url': {'$ref': 'common.json#/url', '$description': 'translations.json#/div_action_log_url'}, 'target': {'type': 'string', 'enum': ['_self', '_blank'], 'force_enum_field': True, '$description': 'translations.json#/div_action_target', 'platforms': ['web'], 'code_generation_disabled_swift': True}}, 'required': ['log_id']}], '$schema': 'http://json-schema.org/draft-07/schema'}, 'minItems': 1, '$description': 'translations.json#/div_video_resume_actions'}, 'pause_actions': {'type': 'array', 'items': {'definitions': {'menu_item': {'type': 'object', 'properties': {'text': {'$ref': 'common.json#/non_empty_string', '$description': 'translations.json#/div_action_menu_item_text'}, 'action': {'$ref': 'div-action.json', '$description': 'translations.json#/div_action_menu_item_action'}, 'actions': {'type': 'array', 'items': {'$ref': 'div-action.json'}, 'minItems': 1, '$description': 'translations.json#/div_action_menu_item_actions'}}, 'required': ['text']}}, 'allOf': [{'$ref': 'div-action-base.json'}, {'type': 'object', '$description': 'translations.json#/div_action', 'properties': {'menu_items': {'type': 'array', 'items': {'$ref': '#/definitions/menu_item'}, '$description': 'translations.json#/div_action_menu_items', 'platforms': ['android', 'ios']}, 'log_url': {'$ref': 'common.json#/url', '$description': 'translations.json#/div_action_log_url'}, 'target': {'type': 'string', 'enum': ['_self', '_blank'], 'force_enum_field': True, '$description': 'translations.json#/div_action_target', 'platforms': ['web'], 'code_generation_disabled_swift': True}}, 'required': ['log_id']}], '$schema': 'http://json-schema.org/draft-07/schema'}, 'minItems': 1, '$description': 'translations.json#/div_video_pause_actions'}, 'end_actions': {'type': 'array', 'items': {'definitions': {'menu_item': {'type': 'object', 'properties': {'text': {'$ref': 'common.json#/non_empty_string', '$description': 'translations.json#/div_action_menu_item_text'}, 'action': {'$ref': 'div-action.json', '$description': 'translations.json#/div_action_menu_item_action'}, 'actions': {'type': 'array', 'items': {'$ref': 'div-action.json'}, 'minItems': 1, '$description': 'translations.json#/div_action_menu_item_actions'}}, 'required': ['text']}}, 'allOf': [{'$ref': 'div-action-base.json'}, {'type': 'object', '$description': 'translations.json#/div_action', 'properties': {'menu_items': {'type': 'array', 'items': {'$ref': '#/definitions/menu_item'}, '$description': 'translations.json#/div_action_menu_items', 'platforms': ['android', 'ios']}, 'log_url': {'$ref': 'common.json#/url', '$description': 'translations.json#/div_action_log_url'}, 'target': {'type': 'string', 'enum': ['_self', '_blank'], 'force_enum_field': True, '$description': 'translations.json#/div_action_target', 'platforms': ['web'], 'code_generation_disabled_swift': True}}, 'required': ['log_id']}], '$schema': 'http://json-schema.org/draft-07/schema'}, 'minItems': 1, '$description': 'translations.json#/div_video_end_actions'}, 'buffering_actions': {'type': 'array', 'items': {'definitions': {'menu_item': {'type': 'object', 'properties': {'text': {'$ref': 'common.json#/non_empty_string', '$description': 'translations.json#/div_action_menu_item_text'}, 'action': {'$ref': 'div-action.json', '$description': 'translations.json#/div_action_menu_item_action'}, 'actions': {'type': 'array', 'items': {'$ref': 'div-action.json'}, 'minItems': 1, '$description': 'translations.json#/div_action_menu_item_actions'}}, 'required': ['text']}}, 'allOf': [{'$ref': 'div-action-base.json'}, {'type': 'object', '$description': 'translations.json#/div_action', 'properties': {'menu_items': {'type': 'array', 'items': {'$ref': '#/definitions/menu_item'}, '$description': 'translations.json#/div_action_menu_items', 'platforms': ['android', 'ios']}, 'log_url': {'$ref': 'common.json#/url', '$description': 'translations.json#/div_action_log_url'}, 'target': {'type': 'string', 'enum': ['_self', '_blank'], 'force_enum_field': True, '$description': 'translations.json#/div_action_target', 'platforms': ['web'], 'code_generation_disabled_swift': True}}, 'required': ['log_id']}], '$schema': 'http://json-schema.org/draft-07/schema'}, 'minItems': 1, '$description': 'translations.json#/div_video_buffering_actions'}, 'fatal_actions': {'type': 'array', 'items': {'definitions': {'menu_item': {'type': 'object', 'properties': {'text': {'$ref': 'common.json#/non_empty_string', '$description': 'translations.json#/div_action_menu_item_text'}, 'action': {'$ref': 'div-action.json', '$description': 'translations.json#/div_action_menu_item_action'}, 'actions': {'type': 'array', 'items': {'$ref': 'div-action.json'}, 'minItems': 1, '$description': 'translations.json#/div_action_menu_item_actions'}}, 'required': ['text']}}, 'allOf': [{'$ref': 'div-action-base.json'}, {'type': 'object', '$description': 'translations.json#/div_action', 'properties': {'menu_items': {'type': 'array', 'items': {'$ref': '#/definitions/menu_item'}, '$description': 'translations.json#/div_action_menu_items', 'platforms': ['android', 'ios']}, 'log_url': {'$ref': 'common.json#/url', '$description': 'translations.json#/div_action_log_url'}, 'target': {'type': 'string', 'enum': ['_self', '_blank'], 'force_enum_field': True, '$description': 'translations.json#/div_action_target', 'platforms': ['web'], 'code_generation_disabled_swift': True}}, 'required': ['log_id']}], '$schema': 'http://json-schema.org/draft-07/schema'}, 'minItems': 1, '$description': 'translations.json#/div_video_fatal_actions'}, 'player_settings_payload': {'type': 'object', 'additionalProperties': True, '$description': 'translations.json#/div_video_player_settings_payload', 'platforms': ['android', 'ios']}, 'aspect': {'type': 'object', '$description': 'translations.json#/div_aspect', 'properties': {'ratio': {'$ref': 'common.json#/positive_number', '$description': 'translations.json#/div_aspect_ratio'}}, 'required': ['ratio'], '$schema': 'http://json-schema.org/draft-07/schema'}, 'scale': {'type': 'string', 'enum': ['fill', 'no_scale', 'fit'], '$schema': 'http://json-schema.org/draft-07/schema'}}}], 'required': ['type', 'video_sources'], '$schema': 'http://json-schema.org/draft-07/schema'}, rule='required')
 return data

def validate_div_video_scale_json(data, custom_formats={}, name_prefix=None):
 if not isinstance(data, (str)):
  if not (isinstance(data, str) and '@' in data):
   raise JsonSchemaValueException("" + (name_prefix or "data") + " must be string", value=data, name="" + (name_prefix or "data") + "", definition={'type': 'string', 'enum': ['fill', 'no_scale', 'fit'], '$schema': 'http://json-schema.org/draft-07/schema'}, rule='type')
 if data not in ['fill', 'no_scale', 'fit']:
  if not (isinstance(data, str) and '@' in data):
   raise JsonSchemaValueException("" + (name_prefix or "data") + " must be one of ['fill', 'no_scale', 'fit']", value=data, name="" + (name_prefix or "data") + "", definition={'type': 'string', 'enum': ['fill', 'no_scale', 'fit'], '$schema': 'http://json-schema.org/draft-07/schema'}, rule='enum')
 return data

def validate_div_aspect_json(data, custom_formats={}, name_prefix=None):
 if not isinstance(data, (dict)):
  if not (isinstance(data, str) and '@' in data):
   raise JsonSchemaValueException("" + (name_prefix or "data") + " must be object", value=data, name="" + (name_prefix or "data") + "", definition={'type': 'object', '$description': 'translations.json#/div_aspect', 'properties': {'ratio': {'type': 'number', 'constraint': 'number > 0'}}, 'required': ['ratio'], '$schema': 'http://json-schema.org/draft-07/schema'}, rule='type')
 data_is_dict = isinstance(data, dict)
 if data_is_dict:
  data__missing_keys = set(['ratio']) - data.keys()
  if data__missing_keys:
   if not (isinstance(data, str) and '@' in data):
    raise JsonSchemaValueException("" + (name_prefix or "data") + " must contain " + (str(sorted(data__missing_keys)) + " properties"), value=data, name="" + (name_prefix or "data") + "", definition={'type': 'object', '$description': 'translations.json#/div_aspect', 'properties': {'ratio': {'type': 'number', 'constraint': 'number > 0'}}, 'required': ['ratio'], '$schema': 'http://json-schema.org/draft-07/schema'}, rule='required')
  data_keys = set(data.keys())
  if "ratio" in data_keys:
   data_keys.remove("ratio")
   data__ratio = data["ratio"]
   validate_common_json__positive_number(data__ratio, custom_formats, (name_prefix or "data") + ".ratio")
 return data

def validate_common_json__positive_number(data, custom_formats={}, name_prefix=None):
 if not isinstance(data, (int, float, Decimal)) or isinstance(data, bool):
  if not (isinstance(data, str) and '@' in data):
   raise JsonSchemaValueException("" + (name_prefix or "data") + " must be number", value=data, name="" + (name_prefix or "data") + "", definition={'type': 'number', 'constraint': 'number > 0'}, rule='type')
 return data

def validate_div_action_json(data, custom_formats={}, name_prefix=None):
 validate_div_action_base_json(data, custom_formats, (name_prefix or "data") + "")
 if not isinstance(data, (dict)):
  if not (isinstance(data, str) and '@' in data):
   raise JsonSchemaValueException("" + (name_prefix or "data") + " must be object", value=data, name="" + (name_prefix or "data") + "", definition={'type': 'object', '$description': 'translations.json#/div_action', 'properties': {'menu_items': {'type': 'array', 'items': {'type': 'object', 'properties': {'text': {'$ref': 'common.json#/non_empty_string', '$description': 'translations.json#/div_action_menu_item_text'}, 'action': {'$ref': 'div-action.json', '$description': 'translations.json#/div_action_menu_item_action'}, 'actions': {'type': 'array', 'items': {'$ref': 'div-action.json'}, 'minItems': 1, '$description': 'translations.json#/div_action_menu_item_actions'}}, 'required': ['text']}, '$description': 'translations.json#/div_action_menu_items', 'platforms': ['android', 'ios']}, 'log_url': {'type': 'string', 'format': 'uri'}, 'target': {'type': 'string', 'enum': ['_self', '_blank'], 'force_enum_field': True, '$description': 'translations.json#/div_action_target', 'platforms': ['web'], 'code_generation_disabled_swift': True}}, 'required': ['log_id']}, rule='type')
 data_is_dict = isinstance(data, dict)
 if data_is_dict:
  data__missing_keys = set(['log_id']) - data.keys()
  if data__missing_keys:
   if not (isinstance(data, str) and '@' in data):
    raise JsonSchemaValueException("" + (name_prefix or "data") + " must contain " + (str(sorted(data__missing_keys)) + " properties"), value=data, name="" + (name_prefix or "data") + "", definition={'type': 'object', '$description': 'translations.json#/div_action', 'properties': {'menu_items': {'type': 'array', 'items': {'type': 'object', 'properties': {'text': {'$ref': 'common.json#/non_empty_string', '$description': 'translations.json#/div_action_menu_item_text'}, 'action': {'$ref': 'div-action.json', '$description': 'translations.json#/div_action_menu_item_action'}, 'actions': {'type': 'array', 'items': {'$ref': 'div-action.json'}, 'minItems': 1, '$description': 'translations.json#/div_action_menu_item_actions'}}, 'required': ['text']}, '$description': 'translations.json#/div_action_menu_items', 'platforms': ['android', 'ios']}, 'log_url': {'type': 'string', 'format': 'uri'}, 'target': {'type': 'string', 'enum': ['_self', '_blank'], 'force_enum_field': True, '$description': 'translations.json#/div_action_target', 'platforms': ['web'], 'code_generation_disabled_swift': True}}, 'required': ['log_id']}, rule='required')
  data_keys = set(data.keys())
  if "menu_items" in data_keys:
   data_keys.remove("menu_items")
   data__menuitems = data["menu_items"]
   if not isinstance(data__menuitems, (list, tuple)):
    if not (isinstance(data__menuitems, str) and '@' in data__menuitems):
     raise JsonSchemaValueException("" + (name_prefix or "data") + ".menu_items must be array", value=data__menuitems, name="" + (name_prefix or "data") + ".menu_items", definition={'type': 'array', 'items': {'type': 'object', 'properties': {'text': {'$ref': 'common.json#/non_empty_string', '$description': 'translations.json#/div_action_menu_item_text'}, 'action': {'$ref': 'div-action.json', '$description': 'translations.json#/div_action_menu_item_action'}, 'actions': {'type': 'array', 'items': {'$ref': 'div-action.json'}, 'minItems': 1, '$description': 'translations.json#/div_action_menu_item_actions'}}, 'required': ['text']}, '$description': 'translations.json#/div_action_menu_items', 'platforms': ['android', 'ios']}, rule='type')
   data__menuitems_is_list = isinstance(data__menuitems, (list, tuple))
   if data__menuitems_is_list:
    data__menuitems_len = len(data__menuitems)
    for data__menuitems_x, data__menuitems_item in enumerate(data__menuitems):
     validate_div_action_json__definitions_menu_item(data__menuitems_item, custom_formats, (name_prefix or "data") + ".menu_items[{data__menuitems_x}]".format(**locals()))
  if "log_url" in data_keys:
   data_keys.remove("log_url")
   data__logurl = data["log_url"]
   validate_common_json__url(data__logurl, custom_formats, (name_prefix or "data") + ".log_url")
  if "target" in data_keys:
   data_keys.remove("target")
   data__target = data["target"]
   if not isinstance(data__target, (str)):
    if not (isinstance(data__target, str) and '@' in data__target):
     raise JsonSchemaValueException("" + (name_prefix or "data") + ".target must be string", value=data__target, name="" + (name_prefix or "data") + ".target", definition={'type': 'string', 'enum': ['_self', '_blank'], 'force_enum_field': True, '$description': 'translations.json#/div_action_target', 'platforms': ['web'], 'code_generation_disabled_swift': True}, rule='type')
   if data__target not in ['_self', '_blank']:
    if not (isinstance(data__target, str) and '@' in data__target):
     raise JsonSchemaValueException("" + (name_prefix or "data") + ".target must be one of ['_self', '_blank']", value=data__target, name="" + (name_prefix or "data") + ".target", definition={'type': 'string', 'enum': ['_self', '_blank'], 'force_enum_field': True, '$description': 'translations.json#/div_action_target', 'platforms': ['web'], 'code_generation_disabled_swift': True}, rule='enum')
 return data

def validate_common_json__url(data, custom_formats={}, name_prefix=None):
 if not isinstance(data, (str)):
  if not (isinstance(data, str) and '@' in data):
   raise JsonSchemaValueException("" + (name_prefix or "data") + " must be string", value=data, name="" + (name_prefix or "data") + "", definition={'type': 'string', 'format': 'uri'}, rule='type')
 if isinstance(data, str):
  if not custom_formats["uri"](data):
   if not (isinstance(data, str) and '@' in data):
    raise JsonSchemaValueException("" + (name_prefix or "data") + " must be uri", value=data, name="" + (name_prefix or "data") + "", definition={'type': 'string', 'format': 'uri'}, rule='format')
 return data

def validate_div_action_json__definitions_menu_item(data, custom_formats={}, name_prefix=None):
 if not isinstance(data, (dict)):
  if not (isinstance(data, str) and '@' in data):
   raise JsonSchemaValueException("" + (name_prefix or "data") + " must be object", value=data, name="" + (name_prefix or "data") + "", definition={'type': 'object', 'properties': {'text': {'type': 'string', 'minLength': 1, 'clientMinLength': 1}, 'action': {'definitions': {'menu_item': {'type': 'object', 'properties': {'text': {'$ref': 'common.json#/non_empty_string', '$description': 'translations.json#/div_action_menu_item_text'}, 'action': {'$ref': 'div-action.json', '$description': 'translations.json#/div_action_menu_item_action'}, 'actions': {'type': 'array', 'items': {'$ref': 'div-action.json'}, 'minItems': 1, '$description': 'translations.json#/div_action_menu_item_actions'}}, 'required': ['text']}}, 'allOf': [{'$ref': 'div-action-base.json'}, {'type': 'object', '$description': 'translations.json#/div_action', 'properties': {'menu_items': {'type': 'array', 'items': {'$ref': '#/definitions/menu_item'}, '$description': 'translations.json#/div_action_menu_items', 'platforms': ['android', 'ios']}, 'log_url': {'$ref': 'common.json#/url', '$description': 'translations.json#/div_action_log_url'}, 'target': {'type': 'string', 'enum': ['_self', '_blank'], 'force_enum_field': True, '$description': 'translations.json#/div_action_target', 'platforms': ['web'], 'code_generation_disabled_swift': True}}, 'required': ['log_id']}], '$schema': 'http://json-schema.org/draft-07/schema'}, 'actions': {'type': 'array', 'items': {'definitions': {'menu_item': {'type': 'object', 'properties': {'text': {'$ref': 'common.json#/non_empty_string', '$description': 'translations.json#/div_action_menu_item_text'}, 'action': {'$ref': 'div-action.json', '$description': 'translations.json#/div_action_menu_item_action'}, 'actions': {'type': 'array', 'items': {'$ref': 'div-action.json'}, 'minItems': 1, '$description': 'translations.json#/div_action_menu_item_actions'}}, 'required': ['text']}}, 'allOf': [{'$ref': 'div-action-base.json'}, {'type': 'object', '$description': 'translations.json#/div_action', 'properties': {'menu_items': {'type': 'array', 'items': {'$ref': '#/definitions/menu_item'}, '$description': 'translations.json#/div_action_menu_items', 'platforms': ['android', 'ios']}, 'log_url': {'$ref': 'common.json#/url', '$description': 'translations.json#/div_action_log_url'}, 'target': {'type': 'string', 'enum': ['_self', '_blank'], 'force_enum_field': True, '$description': 'translations.json#/div_action_target', 'platforms': ['web'], 'code_generation_disabled_swift': True}}, 'required': ['log_id']}], '$schema': 'http://json-schema.org/draft-07/schema'}, 'minItems': 1, '$description': 'translations.json#/div_action_menu_item_actions'}}, 'required': ['text']}, rule='type')
 data_is_dict = isinstance(data, dict)
 if data_is_dict:
  data__missing_keys = set(['text']) - data.keys()
  if data__missing_keys:
   if not (isinstance(data, str) and '@' in data):
    raise JsonSchemaValueException("" + (name_prefix or "data") + " must contain " + (str(sorted(data__missing_keys)) + " properties"), value=data, name="" + (name_prefix or "data") + "", definition={'type': 'object', 'properties': {'text': {'type': 'string', 'minLength': 1, 'clientMinLength': 1}, 'action': {'definitions': {'menu_item': {'type': 'object', 'properties': {'text': {'$ref': 'common.json#/non_empty_string', '$description': 'translations.json#/div_action_menu_item_text'}, 'action': {'$ref': 'div-action.json', '$description': 'translations.json#/div_action_menu_item_action'}, 'actions': {'type': 'array', 'items': {'$ref': 'div-action.json'}, 'minItems': 1, '$description': 'translations.json#/div_action_menu_item_actions'}}, 'required': ['text']}}, 'allOf': [{'$ref': 'div-action-base.json'}, {'type': 'object', '$description': 'translations.json#/div_action', 'properties': {'menu_items': {'type': 'array', 'items': {'$ref': '#/definitions/menu_item'}, '$description': 'translations.json#/div_action_menu_items', 'platforms': ['android', 'ios']}, 'log_url': {'$ref': 'common.json#/url', '$description': 'translations.json#/div_action_log_url'}, 'target': {'type': 'string', 'enum': ['_self', '_blank'], 'force_enum_field': True, '$description': 'translations.json#/div_action_target', 'platforms': ['web'], 'code_generation_disabled_swift': True}}, 'required': ['log_id']}], '$schema': 'http://json-schema.org/draft-07/schema'}, 'actions': {'type': 'array', 'items': {'definitions': {'menu_item': {'type': 'object', 'properties': {'text': {'$ref': 'common.json#/non_empty_string', '$description': 'translations.json#/div_action_menu_item_text'}, 'action': {'$ref': 'div-action.json', '$description': 'translations.json#/div_action_menu_item_action'}, 'actions': {'type': 'array', 'items': {'$ref': 'div-action.json'}, 'minItems': 1, '$description': 'translations.json#/div_action_menu_item_actions'}}, 'required': ['text']}}, 'allOf': [{'$ref': 'div-action-base.json'}, {'type': 'object', '$description': 'translations.json#/div_action', 'properties': {'menu_items': {'type': 'array', 'items': {'$ref': '#/definitions/menu_item'}, '$description': 'translations.json#/div_action_menu_items', 'platforms': ['android', 'ios']}, 'log_url': {'$ref': 'common.json#/url', '$description': 'translations.json#/div_action_log_url'}, 'target': {'type': 'string', 'enum': ['_self', '_blank'], 'force_enum_field': True, '$description': 'translations.json#/div_action_target', 'platforms': ['web'], 'code_generation_disabled_swift': True}}, 'required': ['log_id']}], '$schema': 'http://json-schema.org/draft-07/schema'}, 'minItems': 1, '$description': 'translations.json#/div_action_menu_item_actions'}}, 'required': ['text']}, rule='required')
  data_keys = set(data.keys())
  if "text" in data_keys:
   data_keys.remove("text")
   data__text = data["text"]
   validate_common_json__non_empty_string(data__text, custom_formats, (name_prefix or "data") + ".text")
  if "action" in data_keys:
   data_keys.remove("action")
   data__action = data["action"]
   validate_div_action_json(data__action, custom_formats, (name_prefix or "data") + ".action")
  if "actions" in data_keys:
   data_keys.remove("actions")
   data__actions = data["actions"]
   if not isinstance(data__actions, (list, tuple)):
    if not (isinstance(data__actions, str) and '@' in data__actions):
     raise JsonSchemaValueException("" + (name_prefix or "data") + ".actions must be array", value=data__actions, name="" + (name_prefix or "data") + ".actions", definition={'type': 'array', 'items': {'definitions': {'menu_item': {'type': 'object', 'properties': {'text': {'$ref': 'common.json#/non_empty_string', '$description': 'translations.json#/div_action_menu_item_text'}, 'action': {'$ref': 'div-action.json', '$description': 'translations.json#/div_action_menu_item_action'}, 'actions': {'type': 'array', 'items': {'$ref': 'div-action.json'}, 'minItems': 1, '$description': 'translations.json#/div_action_menu_item_actions'}}, 'required': ['text']}}, 'allOf': [{'$ref': 'div-action-base.json'}, {'type': 'object', '$description': 'translations.json#/div_action', 'properties': {'menu_items': {'type': 'array', 'items': {'$ref': '#/definitions/menu_item'}, '$description': 'translations.json#/div_action_menu_items', 'platforms': ['android', 'ios']}, 'log_url': {'$ref': 'common.json#/url', '$description': 'translations.json#/div_action_log_url'}, 'target': {'type': 'string', 'enum': ['_self', '_blank'], 'force_enum_field': True, '$description': 'translations.json#/div_action_target', 'platforms': ['web'], 'code_generation_disabled_swift': True}}, 'required': ['log_id']}], '$schema': 'http://json-schema.org/draft-07/schema'}, 'minItems': 1, '$description': 'translations.json#/div_action_menu_item_actions'}, rule='type')
   data__actions_is_list = isinstance(data__actions, (list, tuple))
   if data__actions_is_list:
    data__actions_len = len(data__actions)
    if data__actions_len < 1:
     if not (isinstance(data__actions, str) and '@' in data__actions):
      raise JsonSchemaValueException("" + (name_prefix or "data") + ".actions must contain at least 1 items", value=data__actions, name="" + (name_prefix or "data") + ".actions", definition={'type': 'array', 'items': {'definitions': {'menu_item': {'type': 'object', 'properties': {'text': {'$ref': 'common.json#/non_empty_string', '$description': 'translations.json#/div_action_menu_item_text'}, 'action': {'$ref': 'div-action.json', '$description': 'translations.json#/div_action_menu_item_action'}, 'actions': {'type': 'array', 'items': {'$ref': 'div-action.json'}, 'minItems': 1, '$description': 'translations.json#/div_action_menu_item_actions'}}, 'required': ['text']}}, 'allOf': [{'$ref': 'div-action-base.json'}, {'type': 'object', '$description': 'translations.json#/div_action', 'properties': {'menu_items': {'type': 'array', 'items': {'$ref': '#/definitions/menu_item'}, '$description': 'translations.json#/div_action_menu_items', 'platforms': ['android', 'ios']}, 'log_url': {'$ref': 'common.json#/url', '$description': 'translations.json#/div_action_log_url'}, 'target': {'type': 'string', 'enum': ['_self', '_blank'], 'force_enum_field': True, '$description': 'translations.json#/div_action_target', 'platforms': ['web'], 'code_generation_disabled_swift': True}}, 'required': ['log_id']}], '$schema': 'http://json-schema.org/draft-07/schema'}, 'minItems': 1, '$description': 'translations.json#/div_action_menu_item_actions'}, rule='minItems')
    for data__actions_x, data__actions_item in enumerate(data__actions):
     validate_div_action_json(data__actions_item, custom_formats, (name_prefix or "data") + ".actions[{data__actions_x}]".format(**locals()))
 return data

def validate_div_action_base_json(data, custom_formats={}, name_prefix=None):
 data_is_dict = isinstance(data, dict)
 if data_is_dict:
  data_keys = set(data.keys())
  if "log_id" in data_keys:
   data_keys.remove("log_id")
   data__logid = data["log_id"]
   validate_common_json__non_empty_string(data__logid, custom_formats, (name_prefix or "data") + ".log_id")
  if "url" in data_keys:
   data_keys.remove("url")
   data__url = data["url"]
   validate_common_json__url(data__url, custom_formats, (name_prefix or "data") + ".url")
  if "referer" in data_keys:
   data_keys.remove("referer")
   data__referer = data["referer"]
   validate_common_json__url(data__referer, custom_formats, (name_prefix or "data") + ".referer")
  if "payload" in data_keys:
   data_keys.remove("payload")
   data__payload = data["payload"]
   if not isinstance(data__payload, (dict)):
    if not (isinstance(data__payload, str) and '@' in data__payload):
     raise JsonSchemaValueException("" + (name_prefix or "data") + ".payload must be object", value=data__payload, name="" + (name_prefix or "data") + ".payload", definition={'type': 'object', 'additionalProperties': True, '$description': 'translations.json#/div_action_base_payload'}, rule='type')
   data__payload_is_dict = isinstance(data__payload, dict)
   if data__payload_is_dict:
    data__payload_keys = set(data__payload.keys())
  if "download_callbacks" in data_keys:
   data_keys.remove("download_callbacks")
   data__downloadcallbacks = data["download_callbacks"]
   validate_div_download_callbacks_json(data__downloadcallbacks, custom_formats, (name_prefix or "data") + ".download_callbacks")
  if "typed" in data_keys:
   data_keys.remove("typed")
   data__typed = data["typed"]
   validate_div_action_typed_json(data__typed, custom_formats, (name_prefix or "data") + ".typed")
 return data

def validate_div_action_typed_json(data, custom_formats={}, name_prefix=None):
 data_any_of_count2 = 0
 if not data_any_of_count2:
  try:
   validate_div_action_array_insert_value_json(data, custom_formats, (name_prefix or "data") + "")
   data_any_of_count2 += 1
  except JsonSchemaValueException: pass
 if not data_any_of_count2:
  try:
   validate_div_action_array_remove_value_json(data, custom_formats, (name_prefix or "data") + "")
   data_any_of_count2 += 1
  except JsonSchemaValueException: pass
 if not data_any_of_count2:
  try:
   validate_div_action_set_variable_json(data, custom_formats, (name_prefix or "data") + "")
   data_any_of_count2 += 1
  except JsonSchemaValueException: pass
 if not data_any_of_count2:
  try:
   validate_div_action_focus_element_json(data, custom_formats, (name_prefix or "data") + "")
   data_any_of_count2 += 1
  except JsonSchemaValueException: pass
 if not data_any_of_count2:
  try:
   validate_div_action_copy_to_clipboard_json(data, custom_formats, (name_prefix or "data") + "")
   data_any_of_count2 += 1
  except JsonSchemaValueException: pass
 if not data_any_of_count2:
  if not (isinstance(data, str) and '@' in data):
   raise JsonSchemaValueException("" + (name_prefix or "data") + " cannot be validated by any definition", value=data, name="" + (name_prefix or "data") + "", definition={'anyOf': [{'type': 'object', '$description': 'translations.json#/div_action_array_insert_value', 'properties': {'type': {'type': 'string', 'enum': ['array_insert_value']}, 'variable_name': {'$ref': 'common.json#/non_empty_string'}, 'index': {'type': 'integer'}, 'value': {'$ref': 'div-typed-value.json'}}, 'required': ['type', 'variable_name', 'value'], '$schema': 'http://json-schema.org/draft-07/schema'}, {'type': 'object', '$description': 'translations.json#/div_action_array_remove_value', 'properties': {'type': {'type': 'string', 'enum': ['array_remove_value']}, 'variable_name': {'$ref': 'common.json#/non_empty_string'}, 'index': {'type': 'integer'}}, 'required': ['type', 'variable_name', 'index'], '$schema': 'http://json-schema.org/draft-07/schema'}, {'type': 'object', '$description': 'translations.json#/div_action_set_variable', 'properties': {'type': {'type': 'string', 'enum': ['set_variable']}, 'variable_name': {'$ref': 'common.json#/non_empty_string'}, 'value': {'$ref': 'div-typed-value.json'}}, 'required': ['type', 'variable_name', 'value'], '$schema': 'http://json-schema.org/draft-07/schema'}, {'type': 'object', '$description': 'translations.json#/div_action_focus_element', 'properties': {'type': {'type': 'string', 'enum': ['focus_element']}, 'element_id': {'$ref': 'common.json#/non_empty_string'}}, 'required': ['type', 'element_id'], '$schema': 'http://json-schema.org/draft-07/schema'}, {'type': 'object', '$description': 'translations.json#/div_action_copy_to_clipboard', 'properties': {'type': {'type': 'string', 'enum': ['copy_to_clipboard']}, 'content': {'$ref': 'div-action-copy-to-clipboard-content.json'}}, 'required': ['type', 'content'], '$schema': 'http://json-schema.org/draft-07/schema'}], '$schema': 'http://json-schema.org/draft-07/schema'}, rule='anyOf')
 return data

def validate_div_action_copy_to_clipboard_json(data, custom_formats={}, name_prefix=None):
 if not isinstance(data, (dict)):
  if not (isinstance(data, str) and '@' in data):
   raise JsonSchemaValueException("" + (name_prefix or "data") + " must be object", value=data, name="" + (name_prefix or "data") + "", definition={'type': 'object', '$description': 'translations.json#/div_action_copy_to_clipboard', 'properties': {'type': {'type': 'string', 'enum': ['copy_to_clipboard']}, 'content': {'definitions': {'content_text': {'type': 'object', 'properties': {'type': {'type': 'string', 'enum': ['text']}, 'value': {'type': 'string'}}, 'required': ['type', 'value']}, 'content_url': {'type': 'object', 'properties': {'type': {'type': 'string', 'enum': ['url']}, 'value': {'$ref': 'common.json#/url'}}, 'required': ['type', 'value']}}, 'anyOf': [{'$ref': '#/definitions/content_text'}, {'$ref': '#/definitions/content_url'}], '$schema': 'http://json-schema.org/draft-07/schema'}}, 'required': ['type', 'content'], '$schema': 'http://json-schema.org/draft-07/schema'}, rule='type')
 data_is_dict = isinstance(data, dict)
 if data_is_dict:
  data__missing_keys = set(['type', 'content']) - data.keys()
  if data__missing_keys:
   if not (isinstance(data, str) and '@' in data):
    raise JsonSchemaValueException("" + (name_prefix or "data") + " must contain " + (str(sorted(data__missing_keys)) + " properties"), value=data, name="" + (name_prefix or "data") + "", definition={'type': 'object', '$description': 'translations.json#/div_action_copy_to_clipboard', 'properties': {'type': {'type': 'string', 'enum': ['copy_to_clipboard']}, 'content': {'definitions': {'content_text': {'type': 'object', 'properties': {'type': {'type': 'string', 'enum': ['text']}, 'value': {'type': 'string'}}, 'required': ['type', 'value']}, 'content_url': {'type': 'object', 'properties': {'type': {'type': 'string', 'enum': ['url']}, 'value': {'$ref': 'common.json#/url'}}, 'required': ['type', 'value']}}, 'anyOf': [{'$ref': '#/definitions/content_text'}, {'$ref': '#/definitions/content_url'}], '$schema': 'http://json-schema.org/draft-07/schema'}}, 'required': ['type', 'content'], '$schema': 'http://json-schema.org/draft-07/schema'}, rule='required')
  data_keys = set(data.keys())
  if "type" in data_keys:
   data_keys.remove("type")
   data__type = data["type"]
   if not isinstance(data__type, (str)):
    if not (isinstance(data__type, str) and '@' in data__type):
     raise JsonSchemaValueException("" + (name_prefix or "data") + ".type must be string", value=data__type, name="" + (name_prefix or "data") + ".type", definition={'type': 'string', 'enum': ['copy_to_clipboard']}, rule='type')
   if data__type not in ['copy_to_clipboard']:
    if not (isinstance(data__type, str) and '@' in data__type):
     raise JsonSchemaValueException("" + (name_prefix or "data") + ".type must be one of ['copy_to_clipboard']", value=data__type, name="" + (name_prefix or "data") + ".type", definition={'type': 'string', 'enum': ['copy_to_clipboard']}, rule='enum')
  if "content" in data_keys:
   data_keys.remove("content")
   data__content = data["content"]
   validate_div_action_copy_to_clipboard_content_json(data__content, custom_formats, (name_prefix or "data") + ".content")
 return data

def validate_div_action_copy_to_clipboard_content_json(data, custom_formats={}, name_prefix=None):
 data_any_of_count3 = 0
 if not data_any_of_count3:
  try:
   validate_div_action_copy_to_clipboard_content_json__definitions_content_text(data, custom_formats, (name_prefix or "data") + "")
   data_any_of_count3 += 1
  except JsonSchemaValueException: pass
 if not data_any_of_count3:
  try:
   validate_div_action_copy_to_clipboard_content_json__definitions_content_url(data, custom_formats, (name_prefix or "data") + "")
   data_any_of_count3 += 1
  except JsonSchemaValueException: pass
 if not data_any_of_count3:
  if not (isinstance(data, str) and '@' in data):
   raise JsonSchemaValueException("" + (name_prefix or "data") + " cannot be validated by any definition", value=data, name="" + (name_prefix or "data") + "", definition={'definitions': {'content_text': {'type': 'object', 'properties': {'type': {'type': 'string', 'enum': ['text']}, 'value': {'type': 'string'}}, 'required': ['type', 'value']}, 'content_url': {'type': 'object', 'properties': {'type': {'type': 'string', 'enum': ['url']}, 'value': {'type': 'string', 'format': 'uri'}}, 'required': ['type', 'value']}}, 'anyOf': [{'type': 'object', 'properties': {'type': {'type': 'string', 'enum': ['text']}, 'value': {'type': 'string'}}, 'required': ['type', 'value']}, {'type': 'object', 'properties': {'type': {'type': 'string', 'enum': ['url']}, 'value': {'$ref': 'common.json#/url'}}, 'required': ['type', 'value']}], '$schema': 'http://json-schema.org/draft-07/schema'}, rule='anyOf')
 return data

def validate_div_action_copy_to_clipboard_content_json__definitions_content_url(data, custom_formats={}, name_prefix=None):
 if not isinstance(data, (dict)):
  if not (isinstance(data, str) and '@' in data):
   raise JsonSchemaValueException("" + (name_prefix or "data") + " must be object", value=data, name="" + (name_prefix or "data") + "", definition={'type': 'object', 'properties': {'type': {'type': 'string', 'enum': ['url']}, 'value': {'type': 'string', 'format': 'uri'}}, 'required': ['type', 'value']}, rule='type')
 data_is_dict = isinstance(data, dict)
 if data_is_dict:
  data__missing_keys = set(['type', 'value']) - data.keys()
  if data__missing_keys:
   if not (isinstance(data, str) and '@' in data):
    raise JsonSchemaValueException("" + (name_prefix or "data") + " must contain " + (str(sorted(data__missing_keys)) + " properties"), value=data, name="" + (name_prefix or "data") + "", definition={'type': 'object', 'properties': {'type': {'type': 'string', 'enum': ['url']}, 'value': {'type': 'string', 'format': 'uri'}}, 'required': ['type', 'value']}, rule='required')
  data_keys = set(data.keys())
  if "type" in data_keys:
   data_keys.remove("type")
   data__type = data["type"]
   if not isinstance(data__type, (str)):
    if not (isinstance(data__type, str) and '@' in data__type):
     raise JsonSchemaValueException("" + (name_prefix or "data") + ".type must be string", value=data__type, name="" + (name_prefix or "data") + ".type", definition={'type': 'string', 'enum': ['url']}, rule='type')
   if data__type not in ['url']:
    if not (isinstance(data__type, str) and '@' in data__type):
     raise JsonSchemaValueException("" + (name_prefix or "data") + ".type must be one of ['url']", value=data__type, name="" + (name_prefix or "data") + ".type", definition={'type': 'string', 'enum': ['url']}, rule='enum')
  if "value" in data_keys:
   data_keys.remove("value")
   data__value = data["value"]
   validate_common_json__url(data__value, custom_formats, (name_prefix or "data") + ".value")
 return data

def validate_div_action_copy_to_clipboard_content_json__definitions_content_text(data, custom_formats={}, name_prefix=None):
 if not isinstance(data, (dict)):
  if not (isinstance(data, str) and '@' in data):
   raise JsonSchemaValueException("" + (name_prefix or "data") + " must be object", value=data, name="" + (name_prefix or "data") + "", definition={'type': 'object', 'properties': {'type': {'type': 'string', 'enum': ['text']}, 'value': {'type': 'string'}}, 'required': ['type', 'value']}, rule='type')
 data_is_dict = isinstance(data, dict)
 if data_is_dict:
  data__missing_keys = set(['type', 'value']) - data.keys()
  if data__missing_keys:
   if not (isinstance(data, str) and '@' in data):
    raise JsonSchemaValueException("" + (name_prefix or "data") + " must contain " + (str(sorted(data__missing_keys)) + " properties"), value=data, name="" + (name_prefix or "data") + "", definition={'type': 'object', 'properties': {'type': {'type': 'string', 'enum': ['text']}, 'value': {'type': 'string'}}, 'required': ['type', 'value']}, rule='required')
  data_keys = set(data.keys())
  if "type" in data_keys:
   data_keys.remove("type")
   data__type = data["type"]
   if not isinstance(data__type, (str)):
    if not (isinstance(data__type, str) and '@' in data__type):
     raise JsonSchemaValueException("" + (name_prefix or "data") + ".type must be string", value=data__type, name="" + (name_prefix or "data") + ".type", definition={'type': 'string', 'enum': ['text']}, rule='type')
   if data__type not in ['text']:
    if not (isinstance(data__type, str) and '@' in data__type):
     raise JsonSchemaValueException("" + (name_prefix or "data") + ".type must be one of ['text']", value=data__type, name="" + (name_prefix or "data") + ".type", definition={'type': 'string', 'enum': ['text']}, rule='enum')
  if "value" in data_keys:
   data_keys.remove("value")
   data__value = data["value"]
   if not isinstance(data__value, (str)):
    if not (isinstance(data__value, str) and '@' in data__value):
     raise JsonSchemaValueException("" + (name_prefix or "data") + ".value must be string", value=data__value, name="" + (name_prefix or "data") + ".value", definition={'type': 'string'}, rule='type')
 return data

def validate_div_action_focus_element_json(data, custom_formats={}, name_prefix=None):
 if not isinstance(data, (dict)):
  if not (isinstance(data, str) and '@' in data):
   raise JsonSchemaValueException("" + (name_prefix or "data") + " must be object", value=data, name="" + (name_prefix or "data") + "", definition={'type': 'object', '$description': 'translations.json#/div_action_focus_element', 'properties': {'type': {'type': 'string', 'enum': ['focus_element']}, 'element_id': {'type': 'string', 'minLength': 1, 'clientMinLength': 1}}, 'required': ['type', 'element_id'], '$schema': 'http://json-schema.org/draft-07/schema'}, rule='type')
 data_is_dict = isinstance(data, dict)
 if data_is_dict:
  data__missing_keys = set(['type', 'element_id']) - data.keys()
  if data__missing_keys:
   if not (isinstance(data, str) and '@' in data):
    raise JsonSchemaValueException("" + (name_prefix or "data") + " must contain " + (str(sorted(data__missing_keys)) + " properties"), value=data, name="" + (name_prefix or "data") + "", definition={'type': 'object', '$description': 'translations.json#/div_action_focus_element', 'properties': {'type': {'type': 'string', 'enum': ['focus_element']}, 'element_id': {'type': 'string', 'minLength': 1, 'clientMinLength': 1}}, 'required': ['type', 'element_id'], '$schema': 'http://json-schema.org/draft-07/schema'}, rule='required')
  data_keys = set(data.keys())
  if "type" in data_keys:
   data_keys.remove("type")
   data__type = data["type"]
   if not isinstance(data__type, (str)):
    if not (isinstance(data__type, str) and '@' in data__type):
     raise JsonSchemaValueException("" + (name_prefix or "data") + ".type must be string", value=data__type, name="" + (name_prefix or "data") + ".type", definition={'type': 'string', 'enum': ['focus_element']}, rule='type')
   if data__type not in ['focus_element']:
    if not (isinstance(data__type, str) and '@' in data__type):
     raise JsonSchemaValueException("" + (name_prefix or "data") + ".type must be one of ['focus_element']", value=data__type, name="" + (name_prefix or "data") + ".type", definition={'type': 'string', 'enum': ['focus_element']}, rule='enum')
  if "element_id" in data_keys:
   data_keys.remove("element_id")
   data__elementid = data["element_id"]
   validate_common_json__non_empty_string(data__elementid, custom_formats, (name_prefix or "data") + ".element_id")
 return data

def validate_div_action_set_variable_json(data, custom_formats={}, name_prefix=None):
 if not isinstance(data, (dict)):
  if not (isinstance(data, str) and '@' in data):
   raise JsonSchemaValueException("" + (name_prefix or "data") + " must be object", value=data, name="" + (name_prefix or "data") + "", definition={'type': 'object', '$description': 'translations.json#/div_action_set_variable', 'properties': {'type': {'type': 'string', 'enum': ['set_variable']}, 'variable_name': {'type': 'string', 'minLength': 1, 'clientMinLength': 1}, 'value': {'definitions': {'string_value': {'alias_kotlin': 'str_value', 'type': 'object', 'properties': {'type': {'type': 'string', 'enum': ['string']}, 'value': {'type': 'string'}}, 'required': ['type', 'value']}, 'integer_value': {'type': 'object', 'properties': {'type': {'type': 'string', 'enum': ['integer']}, 'value': {'type': 'integer'}}, 'required': ['type', 'value']}, 'number_value': {'type': 'object', 'properties': {'type': {'type': 'string', 'enum': ['number']}, 'value': {'type': 'number'}}, 'required': ['type', 'value']}, 'color_value': {'type': 'object', 'properties': {'type': {'type': 'string', 'enum': ['color']}, 'value': {'$ref': 'common.json#/color'}}, 'required': ['type', 'value']}, 'boolean_value': {'alias_kotlin': 'bool_value', 'type': 'object', 'properties': {'type': {'type': 'string', 'enum': ['boolean']}, 'value': {'type': 'boolean'}}, 'required': ['type', 'value']}, 'url_value': {'type': 'object', 'properties': {'type': {'type': 'string', 'enum': ['url']}, 'value': {'$ref': 'common.json#/url'}}, 'required': ['type', 'value']}, 'dict_value': {'type': 'object', 'properties': {'type': {'type': 'string', 'enum': ['dict']}, 'value': {'type': 'object', 'additionalProperties': True}}, 'required': ['type', 'value']}, 'array_value': {'type': 'object', 'properties': {'type': {'type': 'string', 'enum': ['array']}, 'value': {'type': 'array'}}, 'required': ['type', 'value']}}, 'anyOf': [{'$ref': '#definitions/string_value'}, {'$ref': '#definitions/integer_value'}, {'$ref': '#definitions/number_value'}, {'$ref': '#definitions/color_value'}, {'$ref': '#definitions/boolean_value'}, {'$ref': '#definitions/url_value'}, {'$ref': '#definitions/dict_value'}, {'$ref': '#definitions/array_value'}], '$schema': 'http://json-schema.org/draft-07/schema'}}, 'required': ['type', 'variable_name', 'value'], '$schema': 'http://json-schema.org/draft-07/schema'}, rule='type')
 data_is_dict = isinstance(data, dict)
 if data_is_dict:
  data__missing_keys = set(['type', 'variable_name', 'value']) - data.keys()
  if data__missing_keys:
   if not (isinstance(data, str) and '@' in data):
    raise JsonSchemaValueException("" + (name_prefix or "data") + " must contain " + (str(sorted(data__missing_keys)) + " properties"), value=data, name="" + (name_prefix or "data") + "", definition={'type': 'object', '$description': 'translations.json#/div_action_set_variable', 'properties': {'type': {'type': 'string', 'enum': ['set_variable']}, 'variable_name': {'type': 'string', 'minLength': 1, 'clientMinLength': 1}, 'value': {'definitions': {'string_value': {'alias_kotlin': 'str_value', 'type': 'object', 'properties': {'type': {'type': 'string', 'enum': ['string']}, 'value': {'type': 'string'}}, 'required': ['type', 'value']}, 'integer_value': {'type': 'object', 'properties': {'type': {'type': 'string', 'enum': ['integer']}, 'value': {'type': 'integer'}}, 'required': ['type', 'value']}, 'number_value': {'type': 'object', 'properties': {'type': {'type': 'string', 'enum': ['number']}, 'value': {'type': 'number'}}, 'required': ['type', 'value']}, 'color_value': {'type': 'object', 'properties': {'type': {'type': 'string', 'enum': ['color']}, 'value': {'$ref': 'common.json#/color'}}, 'required': ['type', 'value']}, 'boolean_value': {'alias_kotlin': 'bool_value', 'type': 'object', 'properties': {'type': {'type': 'string', 'enum': ['boolean']}, 'value': {'type': 'boolean'}}, 'required': ['type', 'value']}, 'url_value': {'type': 'object', 'properties': {'type': {'type': 'string', 'enum': ['url']}, 'value': {'$ref': 'common.json#/url'}}, 'required': ['type', 'value']}, 'dict_value': {'type': 'object', 'properties': {'type': {'type': 'string', 'enum': ['dict']}, 'value': {'type': 'object', 'additionalProperties': True}}, 'required': ['type', 'value']}, 'array_value': {'type': 'object', 'properties': {'type': {'type': 'string', 'enum': ['array']}, 'value': {'type': 'array'}}, 'required': ['type', 'value']}}, 'anyOf': [{'$ref': '#definitions/string_value'}, {'$ref': '#definitions/integer_value'}, {'$ref': '#definitions/number_value'}, {'$ref': '#definitions/color_value'}, {'$ref': '#definitions/boolean_value'}, {'$ref': '#definitions/url_value'}, {'$ref': '#definitions/dict_value'}, {'$ref': '#definitions/array_value'}], '$schema': 'http://json-schema.org/draft-07/schema'}}, 'required': ['type', 'variable_name', 'value'], '$schema': 'http://json-schema.org/draft-07/schema'}, rule='required')
  data_keys = set(data.keys())
  if "type" in data_keys:
   data_keys.remove("type")
   data__type = data["type"]
   if not isinstance(data__type, (str)):
    if not (isinstance(data__type, str) and '@' in data__type):
     raise JsonSchemaValueException("" + (name_prefix or "data") + ".type must be string", value=data__type, name="" + (name_prefix or "data") + ".type", definition={'type': 'string', 'enum': ['set_variable']}, rule='type')
   if data__type not in ['set_variable']:
    if not (isinstance(data__type, str) and '@' in data__type):
     raise JsonSchemaValueException("" + (name_prefix or "data") + ".type must be one of ['set_variable']", value=data__type, name="" + (name_prefix or "data") + ".type", definition={'type': 'string', 'enum': ['set_variable']}, rule='enum')
  if "variable_name" in data_keys:
   data_keys.remove("variable_name")
   data__variablename = data["variable_name"]
   validate_common_json__non_empty_string(data__variablename, custom_formats, (name_prefix or "data") + ".variable_name")
  if "value" in data_keys:
   data_keys.remove("value")
   data__value = data["value"]
   validate_div_typed_value_json(data__value, custom_formats, (name_prefix or "data") + ".value")
 return data

def validate_div_typed_value_json(data, custom_formats={}, name_prefix=None):
 data_any_of_count4 = 0
 if not data_any_of_count4:
  try:
   validate_div_typed_value_json_definitions_string_value(data, custom_formats, (name_prefix or "data") + "")
   data_any_of_count4 += 1
  except JsonSchemaValueException: pass
 if not data_any_of_count4:
  try:
   validate_div_typed_value_json_definitions_integer_value(data, custom_formats, (name_prefix or "data") + "")
   data_any_of_count4 += 1
  except JsonSchemaValueException: pass
 if not data_any_of_count4:
  try:
   validate_div_typed_value_json_definitions_number_value(data, custom_formats, (name_prefix or "data") + "")
   data_any_of_count4 += 1
  except JsonSchemaValueException: pass
 if not data_any_of_count4:
  try:
   validate_div_typed_value_json_definitions_color_value(data, custom_formats, (name_prefix or "data") + "")
   data_any_of_count4 += 1
  except JsonSchemaValueException: pass
 if not data_any_of_count4:
  try:
   validate_div_typed_value_json_definitions_boolean_value(data, custom_formats, (name_prefix or "data") + "")
   data_any_of_count4 += 1
  except JsonSchemaValueException: pass
 if not data_any_of_count4:
  try:
   validate_div_typed_value_json_definitions_url_value(data, custom_formats, (name_prefix or "data") + "")
   data_any_of_count4 += 1
  except JsonSchemaValueException: pass
 if not data_any_of_count4:
  try:
   validate_div_typed_value_json_definitions_dict_value(data, custom_formats, (name_prefix or "data") + "")
   data_any_of_count4 += 1
  except JsonSchemaValueException: pass
 if not data_any_of_count4:
  try:
   validate_div_typed_value_json_definitions_array_value(data, custom_formats, (name_prefix or "data") + "")
   data_any_of_count4 += 1
  except JsonSchemaValueException: pass
 if not data_any_of_count4:
  if not (isinstance(data, str) and '@' in data):
   raise JsonSchemaValueException("" + (name_prefix or "data") + " cannot be validated by any definition", value=data, name="" + (name_prefix or "data") + "", definition={'definitions': {'string_value': {'alias_kotlin': 'str_value', 'type': 'object', 'properties': {'type': {'type': 'string', 'enum': ['string']}, 'value': {'type': 'string'}}, 'required': ['type', 'value']}, 'integer_value': {'type': 'object', 'properties': {'type': {'type': 'string', 'enum': ['integer']}, 'value': {'type': 'integer'}}, 'required': ['type', 'value']}, 'number_value': {'type': 'object', 'properties': {'type': {'type': 'string', 'enum': ['number']}, 'value': {'type': 'number'}}, 'required': ['type', 'value']}, 'color_value': {'type': 'object', 'properties': {'type': {'type': 'string', 'enum': ['color']}, 'value': {'type': 'string', 'format': 'color'}}, 'required': ['type', 'value']}, 'boolean_value': {'alias_kotlin': 'bool_value', 'type': 'object', 'properties': {'type': {'type': 'string', 'enum': ['boolean']}, 'value': {'type': 'boolean'}}, 'required': ['type', 'value']}, 'url_value': {'type': 'object', 'properties': {'type': {'type': 'string', 'enum': ['url']}, 'value': {'type': 'string', 'format': 'uri'}}, 'required': ['type', 'value']}, 'dict_value': {'type': 'object', 'properties': {'type': {'type': 'string', 'enum': ['dict']}, 'value': {'type': 'object', 'additionalProperties': True}}, 'required': ['type', 'value']}, 'array_value': {'type': 'object', 'properties': {'type': {'type': 'string', 'enum': ['array']}, 'value': {'type': 'array'}}, 'required': ['type', 'value']}}, 'anyOf': [{'alias_kotlin': 'str_value', 'type': 'object', 'properties': {'type': {'type': 'string', 'enum': ['string']}, 'value': {'type': 'string'}}, 'required': ['type', 'value']}, {'type': 'object', 'properties': {'type': {'type': 'string', 'enum': ['integer']}, 'value': {'type': 'integer'}}, 'required': ['type', 'value']}, {'type': 'object', 'properties': {'type': {'type': 'string', 'enum': ['number']}, 'value': {'type': 'number'}}, 'required': ['type', 'value']}, {'type': 'object', 'properties': {'type': {'type': 'string', 'enum': ['color']}, 'value': {'$ref': 'common.json#/color'}}, 'required': ['type', 'value']}, {'alias_kotlin': 'bool_value', 'type': 'object', 'properties': {'type': {'type': 'string', 'enum': ['boolean']}, 'value': {'type': 'boolean'}}, 'required': ['type', 'value']}, {'type': 'object', 'properties': {'type': {'type': 'string', 'enum': ['url']}, 'value': {'$ref': 'common.json#/url'}}, 'required': ['type', 'value']}, {'type': 'object', 'properties': {'type': {'type': 'string', 'enum': ['dict']}, 'value': {'type': 'object', 'additionalProperties': True}}, 'required': ['type', 'value']}, {'type': 'object', 'properties': {'type': {'type': 'string', 'enum': ['array']}, 'value': {'type': 'array'}}, 'required': ['type', 'value']}], '$schema': 'http://json-schema.org/draft-07/schema'}, rule='anyOf')
 return data

def validate_div_typed_value_json_definitions_array_value(data, custom_formats={}, name_prefix=None):
 if not isinstance(data, (dict)):
  if not (isinstance(data, str) and '@' in data):
   raise JsonSchemaValueException("" + (name_prefix or "data") + " must be object", value=data, name="" + (name_prefix or "data") + "", definition={'type': 'object', 'properties': {'type': {'type': 'string', 'enum': ['array']}, 'value': {'type': 'array'}}, 'required': ['type', 'value']}, rule='type')
 data_is_dict = isinstance(data, dict)
 if data_is_dict:
  data__missing_keys = set(['type', 'value']) - data.keys()
  if data__missing_keys:
   if not (isinstance(data, str) and '@' in data):
    raise JsonSchemaValueException("" + (name_prefix or "data") + " must contain " + (str(sorted(data__missing_keys)) + " properties"), value=data, name="" + (name_prefix or "data") + "", definition={'type': 'object', 'properties': {'type': {'type': 'string', 'enum': ['array']}, 'value': {'type': 'array'}}, 'required': ['type', 'value']}, rule='required')
  data_keys = set(data.keys())
  if "type" in data_keys:
   data_keys.remove("type")
   data__type = data["type"]
   if not isinstance(data__type, (str)):
    if not (isinstance(data__type, str) and '@' in data__type):
     raise JsonSchemaValueException("" + (name_prefix or "data") + ".type must be string", value=data__type, name="" + (name_prefix or "data") + ".type", definition={'type': 'string', 'enum': ['array']}, rule='type')
   if data__type not in ['array']:
    if not (isinstance(data__type, str) and '@' in data__type):
     raise JsonSchemaValueException("" + (name_prefix or "data") + ".type must be one of ['array']", value=data__type, name="" + (name_prefix or "data") + ".type", definition={'type': 'string', 'enum': ['array']}, rule='enum')
  if "value" in data_keys:
   data_keys.remove("value")
   data__value = data["value"]
   if not isinstance(data__value, (list, tuple)):
    if not (isinstance(data__value, str) and '@' in data__value):
     raise JsonSchemaValueException("" + (name_prefix or "data") + ".value must be array", value=data__value, name="" + (name_prefix or "data") + ".value", definition={'type': 'array'}, rule='type')
 return data

def validate_div_typed_value_json_definitions_dict_value(data, custom_formats={}, name_prefix=None):
 if not isinstance(data, (dict)):
  if not (isinstance(data, str) and '@' in data):
   raise JsonSchemaValueException("" + (name_prefix or "data") + " must be object", value=data, name="" + (name_prefix or "data") + "", definition={'type': 'object', 'properties': {'type': {'type': 'string', 'enum': ['dict']}, 'value': {'type': 'object', 'additionalProperties': True}}, 'required': ['type', 'value']}, rule='type')
 data_is_dict = isinstance(data, dict)
 if data_is_dict:
  data__missing_keys = set(['type', 'value']) - data.keys()
  if data__missing_keys:
   if not (isinstance(data, str) and '@' in data):
    raise JsonSchemaValueException("" + (name_prefix or "data") + " must contain " + (str(sorted(data__missing_keys)) + " properties"), value=data, name="" + (name_prefix or "data") + "", definition={'type': 'object', 'properties': {'type': {'type': 'string', 'enum': ['dict']}, 'value': {'type': 'object', 'additionalProperties': True}}, 'required': ['type', 'value']}, rule='required')
  data_keys = set(data.keys())
  if "type" in data_keys:
   data_keys.remove("type")
   data__type = data["type"]
   if not isinstance(data__type, (str)):
    if not (isinstance(data__type, str) and '@' in data__type):
     raise JsonSchemaValueException("" + (name_prefix or "data") + ".type must be string", value=data__type, name="" + (name_prefix or "data") + ".type", definition={'type': 'string', 'enum': ['dict']}, rule='type')
   if data__type not in ['dict']:
    if not (isinstance(data__type, str) and '@' in data__type):
     raise JsonSchemaValueException("" + (name_prefix or "data") + ".type must be one of ['dict']", value=data__type, name="" + (name_prefix or "data") + ".type", definition={'type': 'string', 'enum': ['dict']}, rule='enum')
  if "value" in data_keys:
   data_keys.remove("value")
   data__value = data["value"]
   if not isinstance(data__value, (dict)):
    if not (isinstance(data__value, str) and '@' in data__value):
     raise JsonSchemaValueException("" + (name_prefix or "data") + ".value must be object", value=data__value, name="" + (name_prefix or "data") + ".value", definition={'type': 'object', 'additionalProperties': True}, rule='type')
   data__value_is_dict = isinstance(data__value, dict)
   if data__value_is_dict:
    data__value_keys = set(data__value.keys())
 return data

def validate_div_typed_value_json_definitions_url_value(data, custom_formats={}, name_prefix=None):
 if not isinstance(data, (dict)):
  if not (isinstance(data, str) and '@' in data):
   raise JsonSchemaValueException("" + (name_prefix or "data") + " must be object", value=data, name="" + (name_prefix or "data") + "", definition={'type': 'object', 'properties': {'type': {'type': 'string', 'enum': ['url']}, 'value': {'type': 'string', 'format': 'uri'}}, 'required': ['type', 'value']}, rule='type')
 data_is_dict = isinstance(data, dict)
 if data_is_dict:
  data__missing_keys = set(['type', 'value']) - data.keys()
  if data__missing_keys:
   if not (isinstance(data, str) and '@' in data):
    raise JsonSchemaValueException("" + (name_prefix or "data") + " must contain " + (str(sorted(data__missing_keys)) + " properties"), value=data, name="" + (name_prefix or "data") + "", definition={'type': 'object', 'properties': {'type': {'type': 'string', 'enum': ['url']}, 'value': {'type': 'string', 'format': 'uri'}}, 'required': ['type', 'value']}, rule='required')
  data_keys = set(data.keys())
  if "type" in data_keys:
   data_keys.remove("type")
   data__type = data["type"]
   if not isinstance(data__type, (str)):
    if not (isinstance(data__type, str) and '@' in data__type):
     raise JsonSchemaValueException("" + (name_prefix or "data") + ".type must be string", value=data__type, name="" + (name_prefix or "data") + ".type", definition={'type': 'string', 'enum': ['url']}, rule='type')
   if data__type not in ['url']:
    if not (isinstance(data__type, str) and '@' in data__type):
     raise JsonSchemaValueException("" + (name_prefix or "data") + ".type must be one of ['url']", value=data__type, name="" + (name_prefix or "data") + ".type", definition={'type': 'string', 'enum': ['url']}, rule='enum')
  if "value" in data_keys:
   data_keys.remove("value")
   data__value = data["value"]
   validate_common_json__url(data__value, custom_formats, (name_prefix or "data") + ".value")
 return data

def validate_div_typed_value_json_definitions_boolean_value(data, custom_formats={}, name_prefix=None):
 if not isinstance(data, (dict)):
  if not (isinstance(data, str) and '@' in data):
   raise JsonSchemaValueException("" + (name_prefix or "data") + " must be object", value=data, name="" + (name_prefix or "data") + "", definition={'alias_kotlin': 'bool_value', 'type': 'object', 'properties': {'type': {'type': 'string', 'enum': ['boolean']}, 'value': {'type': 'boolean'}}, 'required': ['type', 'value']}, rule='type')
 data_is_dict = isinstance(data, dict)
 if data_is_dict:
  data__missing_keys = set(['type', 'value']) - data.keys()
  if data__missing_keys:
   if not (isinstance(data, str) and '@' in data):
    raise JsonSchemaValueException("" + (name_prefix or "data") + " must contain " + (str(sorted(data__missing_keys)) + " properties"), value=data, name="" + (name_prefix or "data") + "", definition={'alias_kotlin': 'bool_value', 'type': 'object', 'properties': {'type': {'type': 'string', 'enum': ['boolean']}, 'value': {'type': 'boolean'}}, 'required': ['type', 'value']}, rule='required')
  data_keys = set(data.keys())
  if "type" in data_keys:
   data_keys.remove("type")
   data__type = data["type"]
   if not isinstance(data__type, (str)):
    if not (isinstance(data__type, str) and '@' in data__type):
     raise JsonSchemaValueException("" + (name_prefix or "data") + ".type must be string", value=data__type, name="" + (name_prefix or "data") + ".type", definition={'type': 'string', 'enum': ['boolean']}, rule='type')
   if data__type not in ['boolean']:
    if not (isinstance(data__type, str) and '@' in data__type):
     raise JsonSchemaValueException("" + (name_prefix or "data") + ".type must be one of ['boolean']", value=data__type, name="" + (name_prefix or "data") + ".type", definition={'type': 'string', 'enum': ['boolean']}, rule='enum')
  if "value" in data_keys:
   data_keys.remove("value")
   data__value = data["value"]
   if not isinstance(data__value, (bool)):
    if not (isinstance(data__value, str) and '@' in data__value):
     raise JsonSchemaValueException("" + (name_prefix or "data") + ".value must be boolean", value=data__value, name="" + (name_prefix or "data") + ".value", definition={'type': 'boolean'}, rule='type')
 return data

def validate_div_typed_value_json_definitions_color_value(data, custom_formats={}, name_prefix=None):
 if not isinstance(data, (dict)):
  if not (isinstance(data, str) and '@' in data):
   raise JsonSchemaValueException("" + (name_prefix or "data") + " must be object", value=data, name="" + (name_prefix or "data") + "", definition={'type': 'object', 'properties': {'type': {'type': 'string', 'enum': ['color']}, 'value': {'type': 'string', 'format': 'color'}}, 'required': ['type', 'value']}, rule='type')
 data_is_dict = isinstance(data, dict)
 if data_is_dict:
  data__missing_keys = set(['type', 'value']) - data.keys()
  if data__missing_keys:
   if not (isinstance(data, str) and '@' in data):
    raise JsonSchemaValueException("" + (name_prefix or "data") + " must contain " + (str(sorted(data__missing_keys)) + " properties"), value=data, name="" + (name_prefix or "data") + "", definition={'type': 'object', 'properties': {'type': {'type': 'string', 'enum': ['color']}, 'value': {'type': 'string', 'format': 'color'}}, 'required': ['type', 'value']}, rule='required')
  data_keys = set(data.keys())
  if "type" in data_keys:
   data_keys.remove("type")
   data__type = data["type"]
   if not isinstance(data__type, (str)):
    if not (isinstance(data__type, str) and '@' in data__type):
     raise JsonSchemaValueException("" + (name_prefix or "data") + ".type must be string", value=data__type, name="" + (name_prefix or "data") + ".type", definition={'type': 'string', 'enum': ['color']}, rule='type')
   if data__type not in ['color']:
    if not (isinstance(data__type, str) and '@' in data__type):
     raise JsonSchemaValueException("" + (name_prefix or "data") + ".type must be one of ['color']", value=data__type, name="" + (name_prefix or "data") + ".type", definition={'type': 'string', 'enum': ['color']}, rule='enum')
  if "value" in data_keys:
   data_keys.remove("value")
   data__value = data["value"]
   validate_common_json__color(data__value, custom_formats, (name_prefix or "data") + ".value")
 return data

def validate_common_json__color(data, custom_formats={}, name_prefix=None):
 if not isinstance(data, (str)):
  if not (isinstance(data, str) and '@' in data):
   raise JsonSchemaValueException("" + (name_prefix or "data") + " must be string", value=data, name="" + (name_prefix or "data") + "", definition={'type': 'string', 'format': 'color'}, rule='type')
 if isinstance(data, str):
  if not custom_formats["color"](data):
   if not (isinstance(data, str) and '@' in data):
    raise JsonSchemaValueException("" + (name_prefix or "data") + " must be color", value=data, name="" + (name_prefix or "data") + "", definition={'type': 'string', 'format': 'color'}, rule='format')
 return data

def validate_div_typed_value_json_definitions_number_value(data, custom_formats={}, name_prefix=None):
 if not isinstance(data, (dict)):
  if not (isinstance(data, str) and '@' in data):
   raise JsonSchemaValueException("" + (name_prefix or "data") + " must be object", value=data, name="" + (name_prefix or "data") + "", definition={'type': 'object', 'properties': {'type': {'type': 'string', 'enum': ['number']}, 'value': {'type': 'number'}}, 'required': ['type', 'value']}, rule='type')
 data_is_dict = isinstance(data, dict)
 if data_is_dict:
  data__missing_keys = set(['type', 'value']) - data.keys()
  if data__missing_keys:
   if not (isinstance(data, str) and '@' in data):
    raise JsonSchemaValueException("" + (name_prefix or "data") + " must contain " + (str(sorted(data__missing_keys)) + " properties"), value=data, name="" + (name_prefix or "data") + "", definition={'type': 'object', 'properties': {'type': {'type': 'string', 'enum': ['number']}, 'value': {'type': 'number'}}, 'required': ['type', 'value']}, rule='required')
  data_keys = set(data.keys())
  if "type" in data_keys:
   data_keys.remove("type")
   data__type = data["type"]
   if not isinstance(data__type, (str)):
    if not (isinstance(data__type, str) and '@' in data__type):
     raise JsonSchemaValueException("" + (name_prefix or "data") + ".type must be string", value=data__type, name="" + (name_prefix or "data") + ".type", definition={'type': 'string', 'enum': ['number']}, rule='type')
   if data__type not in ['number']:
    if not (isinstance(data__type, str) and '@' in data__type):
     raise JsonSchemaValueException("" + (name_prefix or "data") + ".type must be one of ['number']", value=data__type, name="" + (name_prefix or "data") + ".type", definition={'type': 'string', 'enum': ['number']}, rule='enum')
  if "value" in data_keys:
   data_keys.remove("value")
   data__value = data["value"]
   if not isinstance(data__value, (int, float, Decimal)) or isinstance(data__value, bool):
    if not (isinstance(data__value, str) and '@' in data__value):
     raise JsonSchemaValueException("" + (name_prefix or "data") + ".value must be number", value=data__value, name="" + (name_prefix or "data") + ".value", definition={'type': 'number'}, rule='type')
 return data

def validate_div_typed_value_json_definitions_integer_value(data, custom_formats={}, name_prefix=None):
 if not isinstance(data, (dict)):
  if not (isinstance(data, str) and '@' in data):
   raise JsonSchemaValueException("" + (name_prefix or "data") + " must be object", value=data, name="" + (name_prefix or "data") + "", definition={'type': 'object', 'properties': {'type': {'type': 'string', 'enum': ['integer']}, 'value': {'type': 'integer'}}, 'required': ['type', 'value']}, rule='type')
 data_is_dict = isinstance(data, dict)
 if data_is_dict:
  data__missing_keys = set(['type', 'value']) - data.keys()
  if data__missing_keys:
   if not (isinstance(data, str) and '@' in data):
    raise JsonSchemaValueException("" + (name_prefix or "data") + " must contain " + (str(sorted(data__missing_keys)) + " properties"), value=data, name="" + (name_prefix or "data") + "", definition={'type': 'object', 'properties': {'type': {'type': 'string', 'enum': ['integer']}, 'value': {'type': 'integer'}}, 'required': ['type', 'value']}, rule='required')
  data_keys = set(data.keys())
  if "type" in data_keys:
   data_keys.remove("type")
   data__type = data["type"]
   if not isinstance(data__type, (str)):
    if not (isinstance(data__type, str) and '@' in data__type):
     raise JsonSchemaValueException("" + (name_prefix or "data") + ".type must be string", value=data__type, name="" + (name_prefix or "data") + ".type", definition={'type': 'string', 'enum': ['integer']}, rule='type')
   if data__type not in ['integer']:
    if not (isinstance(data__type, str) and '@' in data__type):
     raise JsonSchemaValueException("" + (name_prefix or "data") + ".type must be one of ['integer']", value=data__type, name="" + (name_prefix or "data") + ".type", definition={'type': 'string', 'enum': ['integer']}, rule='enum')
  if "value" in data_keys:
   data_keys.remove("value")
   data__value = data["value"]
   if not isinstance(data__value, (int)) and not (isinstance(data__value, float) and data__value.is_integer()) or isinstance(data__value, bool):
    if not (isinstance(data__value, str) and '@' in data__value):
     raise JsonSchemaValueException("" + (name_prefix or "data") + ".value must be integer", value=data__value, name="" + (name_prefix or "data") + ".value", definition={'type': 'integer'}, rule='type')
 return data

def validate_div_typed_value_json_definitions_string_value(data, custom_formats={}, name_prefix=None):
 if not isinstance(data, (dict)):
  if not (isinstance(data, str) and '@' in data):
   raise JsonSchemaValueException("" + (name_prefix or "data") + " must be object", value=data, name="" + (name_prefix or "data") + "", definition={'alias_kotlin': 'str_value', 'type': 'object', 'properties': {'type': {'type': 'string', 'enum': ['string']}, 'value': {'type': 'string'}}, 'required': ['type', 'value']}, rule='type')
 data_is_dict = isinstance(data, dict)
 if data_is_dict:
  data__missing_keys = set(['type', 'value']) - data.keys()
  if data__missing_keys:
   if not (isinstance(data, str) and '@' in data):
    raise JsonSchemaValueException("" + (name_prefix or "data") + " must contain " + (str(sorted(data__missing_keys)) + " properties"), value=data, name="" + (name_prefix or "data") + "", definition={'alias_kotlin': 'str_value', 'type': 'object', 'properties': {'type': {'type': 'string', 'enum': ['string']}, 'value': {'type': 'string'}}, 'required': ['type', 'value']}, rule='required')
  data_keys = set(data.keys())
  if "type" in data_keys:
   data_keys.remove("type")
   data__type = data["type"]
   if not isinstance(data__type, (str)):
    if not (isinstance(data__type, str) and '@' in data__type):
     raise JsonSchemaValueException("" + (name_prefix or "data") + ".type must be string", value=data__type, name="" + (name_prefix or "data") + ".type", definition={'type': 'string', 'enum': ['string']}, rule='type')
   if data__type not in ['string']:
    if not (isinstance(data__type, str) and '@' in data__type):
     raise JsonSchemaValueException("" + (name_prefix or "data") + ".type must be one of ['string']", value=data__type, name="" + (name_prefix or "data") + ".type", definition={'type': 'string', 'enum': ['string']}, rule='enum')
  if "value" in data_keys:
   data_keys.remove("value")
   data__value = data["value"]
   if not isinstance(data__value, (str)):
    if not (isinstance(data__value, str) and '@' in data__value):
     raise JsonSchemaValueException("" + (name_prefix or "data") + ".value must be string", value=data__value, name="" + (name_prefix or "data") + ".value", definition={'type': 'string'}, rule='type')
 return data

def validate_div_action_array_remove_value_json(data, custom_formats={}, name_prefix=None):
 if not isinstance(data, (dict)):
  if not (isinstance(data, str) and '@' in data):
   raise JsonSchemaValueException("" + (name_prefix or "data") + " must be object", value=data, name="" + (name_prefix or "data") + "", definition={'type': 'object', '$description': 'translations.json#/div_action_array_remove_value', 'properties': {'type': {'type': 'string', 'enum': ['array_remove_value']}, 'variable_name': {'type': 'string', 'minLength': 1, 'clientMinLength': 1}, 'index': {'type': 'integer'}}, 'required': ['type', 'variable_name', 'index'], '$schema': 'http://json-schema.org/draft-07/schema'}, rule='type')
 data_is_dict = isinstance(data, dict)
 if data_is_dict:
  data__missing_keys = set(['type', 'variable_name', 'index']) - data.keys()
  if data__missing_keys:
   if not (isinstance(data, str) and '@' in data):
    raise JsonSchemaValueException("" + (name_prefix or "data") + " must contain " + (str(sorted(data__missing_keys)) + " properties"), value=data, name="" + (name_prefix or "data") + "", definition={'type': 'object', '$description': 'translations.json#/div_action_array_remove_value', 'properties': {'type': {'type': 'string', 'enum': ['array_remove_value']}, 'variable_name': {'type': 'string', 'minLength': 1, 'clientMinLength': 1}, 'index': {'type': 'integer'}}, 'required': ['type', 'variable_name', 'index'], '$schema': 'http://json-schema.org/draft-07/schema'}, rule='required')
  data_keys = set(data.keys())
  if "type" in data_keys:
   data_keys.remove("type")
   data__type = data["type"]
   if not isinstance(data__type, (str)):
    if not (isinstance(data__type, str) and '@' in data__type):
     raise JsonSchemaValueException("" + (name_prefix or "data") + ".type must be string", value=data__type, name="" + (name_prefix or "data") + ".type", definition={'type': 'string', 'enum': ['array_remove_value']}, rule='type')
   if data__type not in ['array_remove_value']:
    if not (isinstance(data__type, str) and '@' in data__type):
     raise JsonSchemaValueException("" + (name_prefix or "data") + ".type must be one of ['array_remove_value']", value=data__type, name="" + (name_prefix or "data") + ".type", definition={'type': 'string', 'enum': ['array_remove_value']}, rule='enum')
  if "variable_name" in data_keys:
   data_keys.remove("variable_name")
   data__variablename = data["variable_name"]
   validate_common_json__non_empty_string(data__variablename, custom_formats, (name_prefix or "data") + ".variable_name")
  if "index" in data_keys:
   data_keys.remove("index")
   data__index = data["index"]
   if not isinstance(data__index, (int)) and not (isinstance(data__index, float) and data__index.is_integer()) or isinstance(data__index, bool):
    if not (isinstance(data__index, str) and '@' in data__index):
     raise JsonSchemaValueException("" + (name_prefix or "data") + ".index must be integer", value=data__index, name="" + (name_prefix or "data") + ".index", definition={'type': 'integer'}, rule='type')
 return data

def validate_div_action_array_insert_value_json(data, custom_formats={}, name_prefix=None):
 if not isinstance(data, (dict)):
  if not (isinstance(data, str) and '@' in data):
   raise JsonSchemaValueException("" + (name_prefix or "data") + " must be object", value=data, name="" + (name_prefix or "data") + "", definition={'type': 'object', '$description': 'translations.json#/div_action_array_insert_value', 'properties': {'type': {'type': 'string', 'enum': ['array_insert_value']}, 'variable_name': {'type': 'string', 'minLength': 1, 'clientMinLength': 1}, 'index': {'type': 'integer'}, 'value': {'definitions': {'string_value': {'alias_kotlin': 'str_value', 'type': 'object', 'properties': {'type': {'type': 'string', 'enum': ['string']}, 'value': {'type': 'string'}}, 'required': ['type', 'value']}, 'integer_value': {'type': 'object', 'properties': {'type': {'type': 'string', 'enum': ['integer']}, 'value': {'type': 'integer'}}, 'required': ['type', 'value']}, 'number_value': {'type': 'object', 'properties': {'type': {'type': 'string', 'enum': ['number']}, 'value': {'type': 'number'}}, 'required': ['type', 'value']}, 'color_value': {'type': 'object', 'properties': {'type': {'type': 'string', 'enum': ['color']}, 'value': {'$ref': 'common.json#/color'}}, 'required': ['type', 'value']}, 'boolean_value': {'alias_kotlin': 'bool_value', 'type': 'object', 'properties': {'type': {'type': 'string', 'enum': ['boolean']}, 'value': {'type': 'boolean'}}, 'required': ['type', 'value']}, 'url_value': {'type': 'object', 'properties': {'type': {'type': 'string', 'enum': ['url']}, 'value': {'$ref': 'common.json#/url'}}, 'required': ['type', 'value']}, 'dict_value': {'type': 'object', 'properties': {'type': {'type': 'string', 'enum': ['dict']}, 'value': {'type': 'object', 'additionalProperties': True}}, 'required': ['type', 'value']}, 'array_value': {'type': 'object', 'properties': {'type': {'type': 'string', 'enum': ['array']}, 'value': {'type': 'array'}}, 'required': ['type', 'value']}}, 'anyOf': [{'$ref': '#definitions/string_value'}, {'$ref': '#definitions/integer_value'}, {'$ref': '#definitions/number_value'}, {'$ref': '#definitions/color_value'}, {'$ref': '#definitions/boolean_value'}, {'$ref': '#definitions/url_value'}, {'$ref': '#definitions/dict_value'}, {'$ref': '#definitions/array_value'}], '$schema': 'http://json-schema.org/draft-07/schema'}}, 'required': ['type', 'variable_name', 'value'], '$schema': 'http://json-schema.org/draft-07/schema'}, rule='type')
 data_is_dict = isinstance(data, dict)
 if data_is_dict:
  data__missing_keys = set(['type', 'variable_name', 'value']) - data.keys()
  if data__missing_keys:
   if not (isinstance(data, str) and '@' in data):
    raise JsonSchemaValueException("" + (name_prefix or "data") + " must contain " + (str(sorted(data__missing_keys)) + " properties"), value=data, name="" + (name_prefix or "data") + "", definition={'type': 'object', '$description': 'translations.json#/div_action_array_insert_value', 'properties': {'type': {'type': 'string', 'enum': ['array_insert_value']}, 'variable_name': {'type': 'string', 'minLength': 1, 'clientMinLength': 1}, 'index': {'type': 'integer'}, 'value': {'definitions': {'string_value': {'alias_kotlin': 'str_value', 'type': 'object', 'properties': {'type': {'type': 'string', 'enum': ['string']}, 'value': {'type': 'string'}}, 'required': ['type', 'value']}, 'integer_value': {'type': 'object', 'properties': {'type': {'type': 'string', 'enum': ['integer']}, 'value': {'type': 'integer'}}, 'required': ['type', 'value']}, 'number_value': {'type': 'object', 'properties': {'type': {'type': 'string', 'enum': ['number']}, 'value': {'type': 'number'}}, 'required': ['type', 'value']}, 'color_value': {'type': 'object', 'properties': {'type': {'type': 'string', 'enum': ['color']}, 'value': {'$ref': 'common.json#/color'}}, 'required': ['type', 'value']}, 'boolean_value': {'alias_kotlin': 'bool_value', 'type': 'object', 'properties': {'type': {'type': 'string', 'enum': ['boolean']}, 'value': {'type': 'boolean'}}, 'required': ['type', 'value']}, 'url_value': {'type': 'object', 'properties': {'type': {'type': 'string', 'enum': ['url']}, 'value': {'$ref': 'common.json#/url'}}, 'required': ['type', 'value']}, 'dict_value': {'type': 'object', 'properties': {'type': {'type': 'string', 'enum': ['dict']}, 'value': {'type': 'object', 'additionalProperties': True}}, 'required': ['type', 'value']}, 'array_value': {'type': 'object', 'properties': {'type': {'type': 'string', 'enum': ['array']}, 'value': {'type': 'array'}}, 'required': ['type', 'value']}}, 'anyOf': [{'$ref': '#definitions/string_value'}, {'$ref': '#definitions/integer_value'}, {'$ref': '#definitions/number_value'}, {'$ref': '#definitions/color_value'}, {'$ref': '#definitions/boolean_value'}, {'$ref': '#definitions/url_value'}, {'$ref': '#definitions/dict_value'}, {'$ref': '#definitions/array_value'}], '$schema': 'http://json-schema.org/draft-07/schema'}}, 'required': ['type', 'variable_name', 'value'], '$schema': 'http://json-schema.org/draft-07/schema'}, rule='required')
  data_keys = set(data.keys())
  if "type" in data_keys:
   data_keys.remove("type")
   data__type = data["type"]
   if not isinstance(data__type, (str)):
    if not (isinstance(data__type, str) and '@' in data__type):
     raise JsonSchemaValueException("" + (name_prefix or "data") + ".type must be string", value=data__type, name="" + (name_prefix or "data") + ".type", definition={'type': 'string', 'enum': ['array_insert_value']}, rule='type')
   if data__type not in ['array_insert_value']:
    if not (isinstance(data__type, str) and '@' in data__type):
     raise JsonSchemaValueException("" + (name_prefix or "data") + ".type must be one of ['array_insert_value']", value=data__type, name="" + (name_prefix or "data") + ".type", definition={'type': 'string', 'enum': ['array_insert_value']}, rule='enum')
  if "variable_name" in data_keys:
   data_keys.remove("variable_name")
   data__variablename = data["variable_name"]
   validate_common_json__non_empty_string(data__variablename, custom_formats, (name_prefix or "data") + ".variable_name")
  if "index" in data_keys:
   data_keys.remove("index")
   data__index = data["index"]
   if not isinstance(data__index, (int)) and not (isinstance(data__index, float) and data__index.is_integer()) or isinstance(data__index, bool):
    if not (isinstance(data__index, str) and '@' in data__index):
     raise JsonSchemaValueException("" + (name_prefix or "data") + ".index must be integer", value=data__index, name="" + (name_prefix or "data") + ".index", definition={'type': 'integer'}, rule='type')
  if "value" in data_keys:
   data_keys.remove("value")
   data__value = data["value"]
   validate_div_typed_value_json(data__value, custom_formats, (name_prefix or "data") + ".value")
 return data

def validate_div_download_callbacks_json(data, custom_formats={}, name_prefix=None):
 if not isinstance(data, (dict)):
  if not (isinstance(data, str) and '@' in data):
   raise JsonSchemaValueException("" + (name_prefix or "data") + " must be object", value=data, name="" + (name_prefix or "data") + "", definition={'type': 'object', '$description': 'translations.json#/div_download_callbacks', 'platforms': ['android', 'ios'], 'properties': {'on_fail_actions': {'type': 'array', 'items': {'definitions': {'menu_item': {'type': 'object', 'properties': {'text': {'$ref': 'common.json#/non_empty_string', '$description': 'translations.json#/div_action_menu_item_text'}, 'action': {'$ref': 'div-action.json', '$description': 'translations.json#/div_action_menu_item_action'}, 'actions': {'type': 'array', 'items': {'$ref': 'div-action.json'}, 'minItems': 1, '$description': 'translations.json#/div_action_menu_item_actions'}}, 'required': ['text']}}, 'allOf': [{'$ref': 'div-action-base.json'}, {'type': 'object', '$description': 'translations.json#/div_action', 'properties': {'menu_items': {'type': 'array', 'items': {'$ref': '#/definitions/menu_item'}, '$description': 'translations.json#/div_action_menu_items', 'platforms': ['android', 'ios']}, 'log_url': {'$ref': 'common.json#/url', '$description': 'translations.json#/div_action_log_url'}, 'target': {'type': 'string', 'enum': ['_self', '_blank'], 'force_enum_field': True, '$description': 'translations.json#/div_action_target', 'platforms': ['web'], 'code_generation_disabled_swift': True}}, 'required': ['log_id']}], '$schema': 'http://json-schema.org/draft-07/schema'}, 'minItems': 1, '$description': 'translations.json#/div_download_callbacks_on_fail_actions'}, 'on_success_actions': {'type': 'array', 'items': {'definitions': {'menu_item': {'type': 'object', 'properties': {'text': {'$ref': 'common.json#/non_empty_string', '$description': 'translations.json#/div_action_menu_item_text'}, 'action': {'$ref': 'div-action.json', '$description': 'translations.json#/div_action_menu_item_action'}, 'actions': {'type': 'array', 'items': {'$ref': 'div-action.json'}, 'minItems': 1, '$description': 'translations.json#/div_action_menu_item_actions'}}, 'required': ['text']}}, 'allOf': [{'$ref': 'div-action-base.json'}, {'type': 'object', '$description': 'translations.json#/div_action', 'properties': {'menu_items': {'type': 'array', 'items': {'$ref': '#/definitions/menu_item'}, '$description': 'translations.json#/div_action_menu_items', 'platforms': ['android', 'ios']}, 'log_url': {'$ref': 'common.json#/url', '$description': 'translations.json#/div_action_log_url'}, 'target': {'type': 'string', 'enum': ['_self', '_blank'], 'force_enum_field': True, '$description': 'translations.json#/div_action_target', 'platforms': ['web'], 'code_generation_disabled_swift': True}}, 'required': ['log_id']}], '$schema': 'http://json-schema.org/draft-07/schema'}, 'minItems': 1, '$description': 'translations.json#/div_download_callbacks_on_success_actions'}}, '$schema': 'http://json-schema.org/draft-07/schema'}, rule='type')
 data_is_dict = isinstance(data, dict)
 if data_is_dict:
  data_keys = set(data.keys())
  if "on_fail_actions" in data_keys:
   data_keys.remove("on_fail_actions")
   data__onfailactions = data["on_fail_actions"]
   if not isinstance(data__onfailactions, (list, tuple)):
    if not (isinstance(data__onfailactions, str) and '@' in data__onfailactions):
     raise JsonSchemaValueException("" + (name_prefix or "data") + ".on_fail_actions must be array", value=data__onfailactions, name="" + (name_prefix or "data") + ".on_fail_actions", definition={'type': 'array', 'items': {'definitions': {'menu_item': {'type': 'object', 'properties': {'text': {'$ref': 'common.json#/non_empty_string', '$description': 'translations.json#/div_action_menu_item_text'}, 'action': {'$ref': 'div-action.json', '$description': 'translations.json#/div_action_menu_item_action'}, 'actions': {'type': 'array', 'items': {'$ref': 'div-action.json'}, 'minItems': 1, '$description': 'translations.json#/div_action_menu_item_actions'}}, 'required': ['text']}}, 'allOf': [{'$ref': 'div-action-base.json'}, {'type': 'object', '$description': 'translations.json#/div_action', 'properties': {'menu_items': {'type': 'array', 'items': {'$ref': '#/definitions/menu_item'}, '$description': 'translations.json#/div_action_menu_items', 'platforms': ['android', 'ios']}, 'log_url': {'$ref': 'common.json#/url', '$description': 'translations.json#/div_action_log_url'}, 'target': {'type': 'string', 'enum': ['_self', '_blank'], 'force_enum_field': True, '$description': 'translations.json#/div_action_target', 'platforms': ['web'], 'code_generation_disabled_swift': True}}, 'required': ['log_id']}], '$schema': 'http://json-schema.org/draft-07/schema'}, 'minItems': 1, '$description': 'translations.json#/div_download_callbacks_on_fail_actions'}, rule='type')
   data__onfailactions_is_list = isinstance(data__onfailactions, (list, tuple))
   if data__onfailactions_is_list:
    data__onfailactions_len = len(data__onfailactions)
    if data__onfailactions_len < 1:
     if not (isinstance(data__onfailactions, str) and '@' in data__onfailactions):
      raise JsonSchemaValueException("" + (name_prefix or "data") + ".on_fail_actions must contain at least 1 items", value=data__onfailactions, name="" + (name_prefix or "data") + ".on_fail_actions", definition={'type': 'array', 'items': {'definitions': {'menu_item': {'type': 'object', 'properties': {'text': {'$ref': 'common.json#/non_empty_string', '$description': 'translations.json#/div_action_menu_item_text'}, 'action': {'$ref': 'div-action.json', '$description': 'translations.json#/div_action_menu_item_action'}, 'actions': {'type': 'array', 'items': {'$ref': 'div-action.json'}, 'minItems': 1, '$description': 'translations.json#/div_action_menu_item_actions'}}, 'required': ['text']}}, 'allOf': [{'$ref': 'div-action-base.json'}, {'type': 'object', '$description': 'translations.json#/div_action', 'properties': {'menu_items': {'type': 'array', 'items': {'$ref': '#/definitions/menu_item'}, '$description': 'translations.json#/div_action_menu_items', 'platforms': ['android', 'ios']}, 'log_url': {'$ref': 'common.json#/url', '$description': 'translations.json#/div_action_log_url'}, 'target': {'type': 'string', 'enum': ['_self', '_blank'], 'force_enum_field': True, '$description': 'translations.json#/div_action_target', 'platforms': ['web'], 'code_generation_disabled_swift': True}}, 'required': ['log_id']}], '$schema': 'http://json-schema.org/draft-07/schema'}, 'minItems': 1, '$description': 'translations.json#/div_download_callbacks_on_fail_actions'}, rule='minItems')
    for data__onfailactions_x, data__onfailactions_item in enumerate(data__onfailactions):
     validate_div_action_json(data__onfailactions_item, custom_formats, (name_prefix or "data") + ".on_fail_actions[{data__onfailactions_x}]".format(**locals()))
  if "on_success_actions" in data_keys:
   data_keys.remove("on_success_actions")
   data__onsuccessactions = data["on_success_actions"]
   if not isinstance(data__onsuccessactions, (list, tuple)):
    if not (isinstance(data__onsuccessactions, str) and '@' in data__onsuccessactions):
     raise JsonSchemaValueException("" + (name_prefix or "data") + ".on_success_actions must be array", value=data__onsuccessactions, name="" + (name_prefix or "data") + ".on_success_actions", definition={'type': 'array', 'items': {'definitions': {'menu_item': {'type': 'object', 'properties': {'text': {'$ref': 'common.json#/non_empty_string', '$description': 'translations.json#/div_action_menu_item_text'}, 'action': {'$ref': 'div-action.json', '$description': 'translations.json#/div_action_menu_item_action'}, 'actions': {'type': 'array', 'items': {'$ref': 'div-action.json'}, 'minItems': 1, '$description': 'translations.json#/div_action_menu_item_actions'}}, 'required': ['text']}}, 'allOf': [{'$ref': 'div-action-base.json'}, {'type': 'object', '$description': 'translations.json#/div_action', 'properties': {'menu_items': {'type': 'array', 'items': {'$ref': '#/definitions/menu_item'}, '$description': 'translations.json#/div_action_menu_items', 'platforms': ['android', 'ios']}, 'log_url': {'$ref': 'common.json#/url', '$description': 'translations.json#/div_action_log_url'}, 'target': {'type': 'string', 'enum': ['_self', '_blank'], 'force_enum_field': True, '$description': 'translations.json#/div_action_target', 'platforms': ['web'], 'code_generation_disabled_swift': True}}, 'required': ['log_id']}], '$schema': 'http://json-schema.org/draft-07/schema'}, 'minItems': 1, '$description': 'translations.json#/div_download_callbacks_on_success_actions'}, rule='type')
   data__onsuccessactions_is_list = isinstance(data__onsuccessactions, (list, tuple))
   if data__onsuccessactions_is_list:
    data__onsuccessactions_len = len(data__onsuccessactions)
    if data__onsuccessactions_len < 1:
     if not (isinstance(data__onsuccessactions, str) and '@' in data__onsuccessactions):
      raise JsonSchemaValueException("" + (name_prefix or "data") + ".on_success_actions must contain at least 1 items", value=data__onsuccessactions, name="" + (name_prefix or "data") + ".on_success_actions", definition={'type': 'array', 'items': {'definitions': {'menu_item': {'type': 'object', 'properties': {'text': {'$ref': 'common.json#/non_empty_string', '$description': 'translations.json#/div_action_menu_item_text'}, 'action': {'$ref': 'div-action.json', '$description': 'translations.json#/div_action_menu_item_action'}, 'actions': {'type': 'array', 'items': {'$ref': 'div-action.json'}, 'minItems': 1, '$description': 'translations.json#/div_action_menu_item_actions'}}, 'required': ['text']}}, 'allOf': [{'$ref': 'div-action-base.json'}, {'type': 'object', '$description': 'translations.json#/div_action', 'properties': {'menu_items': {'type': 'array', 'items': {'$ref': '#/definitions/menu_item'}, '$description': 'translations.json#/div_action_menu_items', 'platforms': ['android', 'ios']}, 'log_url': {'$ref': 'common.json#/url', '$description': 'translations.json#/div_action_log_url'}, 'target': {'type': 'string', 'enum': ['_self', '_blank'], 'force_enum_field': True, '$description': 'translations.json#/div_action_target', 'platforms': ['web'], 'code_generation_disabled_swift': True}}, 'required': ['log_id']}], '$schema': 'http://json-schema.org/draft-07/schema'}, 'minItems': 1, '$description': 'translations.json#/div_download_callbacks_on_success_actions'}, rule='minItems')
    for data__onsuccessactions_x, data__onsuccessactions_item in enumerate(data__onsuccessactions):
     validate_div_action_json(data__onsuccessactions_item, custom_formats, (name_prefix or "data") + ".on_success_actions[{data__onsuccessactions_x}]".format(**locals()))
 return data

def validate_div_variable_name_json(data, custom_formats={}, name_prefix=None):
 validate_common_json__non_empty_string(data, custom_formats, (name_prefix or "data") + "")
 return data

def validate_common_json__non_empty_string(data, custom_formats={}, name_prefix=None):
 if not isinstance(data, (str)):
  if not (isinstance(data, str) and '@' in data):
   raise JsonSchemaValueException("" + (name_prefix or "data") + " must be string", value=data, name="" + (name_prefix or "data") + "", definition={'type': 'string', 'minLength': 1, 'clientMinLength': 1}, rule='type')
 if isinstance(data, str):
  data_len = len(data)
  if data_len < 1:
   if not (isinstance(data, str) and '@' in data):
    raise JsonSchemaValueException("" + (name_prefix or "data") + " must be longer than or equal to 1 characters", value=data, name="" + (name_prefix or "data") + "", definition={'type': 'string', 'minLength': 1, 'clientMinLength': 1}, rule='minLength')
 return data

def validate_common_json__boolean_int(data, custom_formats={}, name_prefix=None):
 data_one_of_count5 = 0
 if data_one_of_count5 < 2:
  try:
   if not isinstance(data, (bool)):
    if not (isinstance(data, str) and '@' in data):
     raise JsonSchemaValueException("" + (name_prefix or "data") + " must be boolean", value=data, name="" + (name_prefix or "data") + "", definition={'type': 'boolean'}, rule='type')
   data_one_of_count5 += 1
  except JsonSchemaValueException: pass
 if data_one_of_count5 < 2:
  try:
   if not isinstance(data, (int)) and not (isinstance(data, float) and data.is_integer()) or isinstance(data, bool):
    if not (isinstance(data, str) and '@' in data):
     raise JsonSchemaValueException("" + (name_prefix or "data") + " must be integer", value=data, name="" + (name_prefix or "data") + "", definition={'type': 'integer', 'enum': [0, 1]}, rule='type')
   if data not in [0, 1]:
    if not (isinstance(data, str) and '@' in data):
     raise JsonSchemaValueException("" + (name_prefix or "data") + " must be one of [0, 1]", value=data, name="" + (name_prefix or "data") + "", definition={'type': 'integer', 'enum': [0, 1]}, rule='enum')
   data_one_of_count5 += 1
  except JsonSchemaValueException: pass
 if data_one_of_count5 != 1:
  if not (isinstance(data, str) and '@' in data):
   raise JsonSchemaValueException("" + (name_prefix or "data") + " must be valid exactly by one definition" + (" (" + str(data_one_of_count5) + " matches found)"), value=data, name="" + (name_prefix or "data") + "", definition={'oneOf': [{'type': 'boolean'}, {'type': 'integer', 'enum': [0, 1]}]}, rule='oneOf')
 return data

def validate_div_video_source_json(data, custom_formats={}, name_prefix=None):
 if not isinstance(data, (dict)):
  if not (isinstance(data, str) and '@' in data):
   raise JsonSchemaValueException("" + (name_prefix or "data") + " must be object", value=data, name="" + (name_prefix or "data") + "", definition={'definitions': {'resolution': {'type': 'object', 'properties': {'type': {'type': 'string', 'enum': ['resolution']}, 'width': {'type': 'integer', 'constraint': 'number > 0'}, 'height': {'type': 'integer', 'constraint': 'number > 0'}}, 'required': ['type', 'width', 'height']}}, 'type': 'object', 'properties': {'type': {'type': 'string', 'enum': ['video_source']}, 'url': {'type': 'string', 'format': 'uri'}, 'resolution': {'type': 'object', 'properties': {'type': {'type': 'string', 'enum': ['resolution']}, 'width': {'$ref': 'common.json#/positive_integer', '$description': 'translations.json#/div_video_source_resolution_width'}, 'height': {'$ref': 'common.json#/positive_integer', '$description': 'translations.json#/div_video_source_resolution_height'}}, 'required': ['type', 'width', 'height']}, 'mime_type': {'type': 'string', '$description': 'translations.json#/div_video_source_mime_type'}, 'bitrate': {'type': 'integer', '$description': 'translations.json#/div_video_source_bitrate'}}, 'required': ['type', 'url', 'mime_type'], '$schema': 'http://json-schema.org/draft-07/schema'}, rule='type')
 data_is_dict = isinstance(data, dict)
 if data_is_dict:
  data__missing_keys = set(['type', 'url', 'mime_type']) - data.keys()
  if data__missing_keys:
   if not (isinstance(data, str) and '@' in data):
    raise JsonSchemaValueException("" + (name_prefix or "data") + " must contain " + (str(sorted(data__missing_keys)) + " properties"), value=data, name="" + (name_prefix or "data") + "", definition={'definitions': {'resolution': {'type': 'object', 'properties': {'type': {'type': 'string', 'enum': ['resolution']}, 'width': {'type': 'integer', 'constraint': 'number > 0'}, 'height': {'type': 'integer', 'constraint': 'number > 0'}}, 'required': ['type', 'width', 'height']}}, 'type': 'object', 'properties': {'type': {'type': 'string', 'enum': ['video_source']}, 'url': {'type': 'string', 'format': 'uri'}, 'resolution': {'type': 'object', 'properties': {'type': {'type': 'string', 'enum': ['resolution']}, 'width': {'$ref': 'common.json#/positive_integer', '$description': 'translations.json#/div_video_source_resolution_width'}, 'height': {'$ref': 'common.json#/positive_integer', '$description': 'translations.json#/div_video_source_resolution_height'}}, 'required': ['type', 'width', 'height']}, 'mime_type': {'type': 'string', '$description': 'translations.json#/div_video_source_mime_type'}, 'bitrate': {'type': 'integer', '$description': 'translations.json#/div_video_source_bitrate'}}, 'required': ['type', 'url', 'mime_type'], '$schema': 'http://json-schema.org/draft-07/schema'}, rule='required')
  data_keys = set(data.keys())
  if "type" in data_keys:
   data_keys.remove("type")
   data__type = data["type"]
   if not isinstance(data__type, (str)):
    if not (isinstance(data__type, str) and '@' in data__type):
     raise JsonSchemaValueException("" + (name_prefix or "data") + ".type must be string", value=data__type, name="" + (name_prefix or "data") + ".type", definition={'type': 'string', 'enum': ['video_source']}, rule='type')
   if data__type not in ['video_source']:
    if not (isinstance(data__type, str) and '@' in data__type):
     raise JsonSchemaValueException("" + (name_prefix or "data") + ".type must be one of ['video_source']", value=data__type, name="" + (name_prefix or "data") + ".type", definition={'type': 'string', 'enum': ['video_source']}, rule='enum')
  if "url" in data_keys:
   data_keys.remove("url")
   data__url = data["url"]
   validate_common_json__url(data__url, custom_formats, (name_prefix or "data") + ".url")
  if "resolution" in data_keys:
   data_keys.remove("resolution")
   data__resolution = data["resolution"]
   validate_div_video_source_json__definitions_resolution(data__resolution, custom_formats, (name_prefix or "data") + ".resolution")
  if "mime_type" in data_keys:
   data_keys.remove("mime_type")
   data__mimetype = data["mime_type"]
   if not isinstance(data__mimetype, (str)):
    if not (isinstance(data__mimetype, str) and '@' in data__mimetype):
     raise JsonSchemaValueException("" + (name_prefix or "data") + ".mime_type must be string", value=data__mimetype, name="" + (name_prefix or "data") + ".mime_type", definition={'type': 'string', '$description': 'translations.json#/div_video_source_mime_type'}, rule='type')
  if "bitrate" in data_keys:
   data_keys.remove("bitrate")
   data__bitrate = data["bitrate"]
   if not isinstance(data__bitrate, (int)) and not (isinstance(data__bitrate, float) and data__bitrate.is_integer()) or isinstance(data__bitrate, bool):
    if not (isinstance(data__bitrate, str) and '@' in data__bitrate):
     raise JsonSchemaValueException("" + (name_prefix or "data") + ".bitrate must be integer", value=data__bitrate, name="" + (name_prefix or "data") + ".bitrate", definition={'type': 'integer', '$description': 'translations.json#/div_video_source_bitrate'}, rule='type')
 return data

def validate_div_video_source_json__definitions_resolution(data, custom_formats={}, name_prefix=None):
 if not isinstance(data, (dict)):
  if not (isinstance(data, str) and '@' in data):
   raise JsonSchemaValueException("" + (name_prefix or "data") + " must be object", value=data, name="" + (name_prefix or "data") + "", definition={'type': 'object', 'properties': {'type': {'type': 'string', 'enum': ['resolution']}, 'width': {'type': 'integer', 'constraint': 'number > 0'}, 'height': {'type': 'integer', 'constraint': 'number > 0'}}, 'required': ['type', 'width', 'height']}, rule='type')
 data_is_dict = isinstance(data, dict)
 if data_is_dict:
  data__missing_keys = set(['type', 'width', 'height']) - data.keys()
  if data__missing_keys:
   if not (isinstance(data, str) and '@' in data):
    raise JsonSchemaValueException("" + (name_prefix or "data") + " must contain " + (str(sorted(data__missing_keys)) + " properties"), value=data, name="" + (name_prefix or "data") + "", definition={'type': 'object', 'properties': {'type': {'type': 'string', 'enum': ['resolution']}, 'width': {'type': 'integer', 'constraint': 'number > 0'}, 'height': {'type': 'integer', 'constraint': 'number > 0'}}, 'required': ['type', 'width', 'height']}, rule='required')
  data_keys = set(data.keys())
  if "type" in data_keys:
   data_keys.remove("type")
   data__type = data["type"]
   if not isinstance(data__type, (str)):
    if not (isinstance(data__type, str) and '@' in data__type):
     raise JsonSchemaValueException("" + (name_prefix or "data") + ".type must be string", value=data__type, name="" + (name_prefix or "data") + ".type", definition={'type': 'string', 'enum': ['resolution']}, rule='type')
   if data__type not in ['resolution']:
    if not (isinstance(data__type, str) and '@' in data__type):
     raise JsonSchemaValueException("" + (name_prefix or "data") + ".type must be one of ['resolution']", value=data__type, name="" + (name_prefix or "data") + ".type", definition={'type': 'string', 'enum': ['resolution']}, rule='enum')
  if "width" in data_keys:
   data_keys.remove("width")
   data__width = data["width"]
   validate_common_json__positive_integer(data__width, custom_formats, (name_prefix or "data") + ".width")
  if "height" in data_keys:
   data_keys.remove("height")
   data__height = data["height"]
   validate_common_json__positive_integer(data__height, custom_formats, (name_prefix or "data") + ".height")
 return data

def validate_common_json__positive_integer(data, custom_formats={}, name_prefix=None):
 if not isinstance(data, (int)) and not (isinstance(data, float) and data.is_integer()) or isinstance(data, bool):
  if not (isinstance(data, str) and '@' in data):
   raise JsonSchemaValueException("" + (name_prefix or "data") + " must be integer", value=data, name="" + (name_prefix or "data") + "", definition={'type': 'integer', 'constraint': 'number > 0'}, rule='type')
 return data

def validate_div_base_json(data, custom_formats={}, name_prefix=None):
 if not isinstance(data, (dict)):
  if not (isinstance(data, str) and '@' in data):
   raise JsonSchemaValueException("" + (name_prefix or "data") + " must be object", value=data, name="" + (name_prefix or "data") + "", definition={'protocol_name': 'div-base', 'codegen': {'swift': {'super_protocol': 'DivBlockModeling'}, 'documentation': {'include_in_toc': True}}, 'type': 'object', 'properties': {'id': {'type': 'string', 'minLength': 1, 'clientMinLength': 1}, 'border': {'type': 'object', '$description': 'translations.json#/div_border', 'properties': {'has_shadow': {'$ref': 'common.json#/boolean_int', 'default_value': 'false', '$description': 'translations.json#/div_border_has_shadow'}, 'shadow': {'$ref': 'div-shadow.json', '$description': 'translations.json#/div_border_shadow'}, 'stroke': {'$ref': 'div-stroke.json', '$description': 'translations.json#/div_border_stroke'}, 'corner_radius': {'$ref': 'common.json#/non_negative_integer', '$description': 'translations.json#/div_border_corner_radius'}, 'corners_radius': {'$ref': 'div-corners-radius.json', '$description': 'translations.json#/div_border_corners_radius'}}, '$schema': 'http://json-schema.org/draft-07/schema'}, 'width': {'anyOf': [{'$ref': 'div-fixed-size.json', '$description': 'translations.json#/div_size_fixed'}, {'$ref': 'div-match-parent-size.json', '$description': 'translations.json#/div_size_match_parent'}, {'$ref': 'div-wrap-content-size.json', '$description': 'translations.json#/div_size_wrap_content'}], '$schema': 'http://json-schema.org/draft-07/schema'}, 'height': {'anyOf': [{'$ref': 'div-fixed-size.json', '$description': 'translations.json#/div_size_fixed'}, {'$ref': 'div-match-parent-size.json', '$description': 'translations.json#/div_size_match_parent'}, {'$ref': 'div-wrap-content-size.json', '$description': 'translations.json#/div_size_wrap_content'}], '$schema': 'http://json-schema.org/draft-07/schema'}, 'background': {'type': 'array', 'items': {'anyOf': [{'$ref': 'div-linear-gradient.json', '$description': 'translations.json#/div_gradient_linear'}, {'$ref': 'div-radial-gradient.json', '$description': 'translations.json#/div_gradient_radial'}, {'$ref': 'div-image-background.json', '$description': 'translations.json#/div_background_image'}, {'$ref': 'div-solid-background.json', '$description': 'translations.json#/div_background_solid'}, {'$ref': 'div-nine-patch-background.json', '$description': 'translations.json#/div_nine_patch_background'}], '$schema': 'http://json-schema.org/draft-07/schema'}, 'minItems': 1, '$description': 'translations.json#/div_base_background'}, 'paddings': {'type': 'object', '$description': 'translations.json#/div_edge_insets', 'properties': {'left': {'$ref': 'common.json#/non_negative_integer', 'default_value': '0', '$description': 'translations.json#/div_edge_insets_left'}, 'right': {'$ref': 'common.json#/non_negative_integer', 'default_value': '0', '$description': 'translations.json#/div_edge_insets_right'}, 'top': {'$ref': 'common.json#/non_negative_integer', 'default_value': '0', '$description': 'translations.json#/div_edge_insets_top'}, 'bottom': {'$ref': 'common.json#/non_negative_integer', 'default_value': '0', '$description': 'translations.json#/div_edge_insets_bottom'}, 'start': {'$ref': 'common.json#/non_negative_integer', '$description': 'translations.json#/div_edge_insets_start', 'platforms': []}, 'end': {'$ref': 'common.json#/non_negative_integer', '$description': 'translations.json#/div_edge_insets_end', 'platforms': []}, 'unit': {'$ref': 'div-size-unit.json', 'default_value': 'dp'}}, '$schema': 'http://json-schema.org/draft-07/schema'}, 'margins': {'type': 'object', '$description': 'translations.json#/div_edge_insets', 'properties': {'left': {'$ref': 'common.json#/non_negative_integer', 'default_value': '0', '$description': 'translations.json#/div_edge_insets_left'}, 'right': {'$ref': 'common.json#/non_negative_integer', 'default_value': '0', '$description': 'translations.json#/div_edge_insets_right'}, 'top': {'$ref': 'common.json#/non_negative_integer', 'default_value': '0', '$description': 'translations.json#/div_edge_insets_top'}, 'bottom': {'$ref': 'common.json#/non_negative_integer', 'default_value': '0', '$description': 'translations.json#/div_edge_insets_bottom'}, 'start': {'$ref': 'common.json#/non_negative_integer', '$description': 'translations.json#/div_edge_insets_start', 'platforms': []}, 'end': {'$ref': 'common.json#/non_negative_integer', '$description': 'translations.json#/div_edge_insets_end', 'platforms': []}, 'unit': {'$ref': 'div-size-unit.json', 'default_value': 'dp'}}, '$schema': 'http://json-schema.org/draft-07/schema'}, 'alpha': {'type': 'number', 'default_value': '1.0', 'constraint': 'number >= 0.0 && number <= 1.0', '$description': 'translations.json#/div_base_alpha'}, 'alignment_vertical': {'type': 'string', 'enum': ['top', 'center', 'bottom', 'baseline'], '$schema': 'http://json-schema.org/draft-07/schema'}, 'alignment_horizontal': {'type': 'string', 'enum': ['left', 'center', 'right', 'start', 'end'], '$schema': 'http://json-schema.org/draft-07/schema'}, 'row_span': {'type': 'integer', 'constraint': 'number >= 0'}, 'column_span': {'type': 'integer', 'constraint': 'number >= 0'}, 'visibility_action': {'$description': 'translations.json#/div_visibility_action', 'allOf': [{'$ref': 'div-sight-action.json'}, {'properties': {'visibility_percentage': {'type': 'integer', 'constraint': 'number > 0 && number <= 100', 'default_value': '50', '$description': 'translations.json#/div_visibility_action_visibility_percentage'}, 'visibility_duration': {'$ref': 'common.json#/non_negative_integer', 'default_value': '800', '$description': 'translations.json#/div_visibility_action_visibility_duration'}}}], '$schema': 'http://json-schema.org/draft-07/schema'}, 'visibility_actions': {'type': 'array', 'items': {'$description': 'translations.json#/div_visibility_action', 'allOf': [{'$ref': 'div-sight-action.json'}, {'properties': {'visibility_percentage': {'type': 'integer', 'constraint': 'number > 0 && number <= 100', 'default_value': '50', '$description': 'translations.json#/div_visibility_action_visibility_percentage'}, 'visibility_duration': {'$ref': 'common.json#/non_negative_integer', 'default_value': '800', '$description': 'translations.json#/div_visibility_action_visibility_duration'}}}], '$schema': 'http://json-schema.org/draft-07/schema'}, 'minItems': 1, '$description': 'translations.json#/div_base_visibility_actions'}, 'disappear_actions': {'type': 'array', 'items': {'$description': 'translations.json#/div_disappear_action', 'allOf': [{'$ref': 'div-sight-action.json'}, {'properties': {'visibility_percentage': {'type': 'integer', 'constraint': 'number >= 0 && number < 100', 'default_value': '0', '$description': 'translations.json#/div_disappear_action_visibility_percentage'}, 'disappear_duration': {'$ref': 'common.json#/non_negative_integer', 'default_value': '800', '$description': 'translations.json#/div_disappear_action_disappear_duration'}}}], '$schema': 'http://json-schema.org/draft-07/schema'}, 'minItems': 1, '$description': 'translations.json#/div_base_disappear_actions'}, 'tooltips': {'type': 'array', 'items': {'type': 'object', '$description': 'translations.json#/div_tooltip', 'properties': {'id': {'$ref': 'common.json#/non_empty_string', 'supports_expressions': False, '$description': 'translations.json#/div_tooltip_id'}, 'div': {'$ref': 'div.json', '$description': 'translations.json#/div_tooltip_div'}, 'position': {'type': 'string', 'enum': ['left', 'top-left', 'top', 'top-right', 'right', 'bottom-right', 'bottom', 'bottom-left', 'center'], '$description': 'translations.json#/div_tooltip_position'}, 'duration': {'$ref': 'common.json#/non_negative_integer', 'default_value': '5000', '$description': 'translations.json#/div_tooltip_duration'}, 'offset': {'$ref': 'div-point.json', '$description': 'translations.json#/div_tooltip_offset'}, 'animation_in': {'$ref': 'div-animation.json', '$description': 'translations.json#/div_tooltip_animation_in'}, 'animation_out': {'$ref': 'div-animation.json', '$description': 'translations.json#/div_tooltip_animation_out'}}, 'required': ['id', 'div', 'position'], '$schema': 'http://json-schema.org/draft-07/schema'}, 'minItems': 1, '$description': 'translations.json#/div_base_tooltips'}, 'accessibility': {'type': 'object', '$description': 'translations.json#/div_accessibility', 'properties': {'description': {'$ref': 'common.json#/non_empty_string', '$description': 'translations.json#/div_accessibility_description'}, 'type': {'type': 'string', 'enum': ['none', 'button', 'image', 'text', 'edit_text', 'header', 'tab_bar', 'list', 'select'], 'supports_expressions': False, '$description': 'translations.json#/div_accessibility_type', 'platforms': ['android', 'ios']}, 'state_description': {'$ref': 'common.json#/non_empty_string', '$description': 'translations.json#/div_accessibility_state_description', 'platforms': ['android', 'ios']}, 'hint': {'$ref': 'common.json#/non_empty_string', '$description': 'translations.json#/div_accessibility_hint', 'platforms': ['android', 'ios']}, 'mode': {'type': 'string', 'enum': ['default', 'merge', 'exclude'], 'default_value': 'default', '$description': 'translations.json#/div_accessibility_mode', 'platforms': ['android', 'ios']}, 'mute_after_action': {'$ref': 'common.json#/boolean_int', 'default_value': 'false', '$description': 'translations.json#/div_accessibility_mute_after_action', 'platforms': ['ios']}}, '$schema': 'http://json-schema.org/draft-07/schema'}, 'extensions': {'type': 'array', 'items': {'type': 'object', '$description': 'translations.json#/div_extension', 'properties': {'id': {'$ref': 'common.json#/non_empty_string', 'supports_expressions': False, '$description': 'translations.json#/div_extension_id'}, 'params': {'type': 'object', 'additionalProperties': True, '$description': 'translations.json#/div_extension_params'}}, 'required': ['id'], '$schema': 'http://json-schema.org/draft-07/schema'}, 'minItems': 1, '$description': 'translations.json#/div_base_extensions'}, 'transition_triggers': {'type': 'array', 'items': {'type': 'string', 'enum': ['data_change', 'state_change', 'visibility_change'], '$description': 'translations.json#/div_transition_trigger', '$schema': 'http://json-schema.org/draft-07/schema'}, 'minItems': 1, 'supports_expressions': False, '$description': 'translations.json#/div_base_transition_triggers'}, 'transition_in': {'$description': 'translations.json#/div_appearance_transition', 'anyOf': [{'$ref': 'div-appearance-set-transition.json', '$description': 'translations.json#/div_appearance_transition_set'}, {'$ref': 'div-fade-transition.json', '$description': 'translations.json#/div_appearance_transition_fade'}, {'$ref': 'div-scale-transition.json', '$description': 'translations.json#/div_appearance_transition_scale'}, {'$ref': 'div-slide-transition.json', '$description': 'translations.json#/div_appearance_transition_slide'}], '$schema': 'http://json-schema.org/draft-07/schema'}, 'transition_change': {'$description': 'translations.json#/div_change_transition', 'anyOf': [{'$ref': 'div-change-set-transition.json', '$description': 'translations.json#/div_change_transition_set'}, {'$ref': 'div-change-bounds-transition.json', '$description': 'translations.json#/div_change_transition_bounds'}], '$schema': 'http://json-schema.org/draft-07/schema'}, 'transition_out': {'$description': 'translations.json#/div_appearance_transition', 'anyOf': [{'$ref': 'div-appearance-set-transition.json', '$description': 'translations.json#/div_appearance_transition_set'}, {'$ref': 'div-fade-transition.json', '$description': 'translations.json#/div_appearance_transition_fade'}, {'$ref': 'div-scale-transition.json', '$description': 'translations.json#/div_appearance_transition_scale'}, {'$ref': 'div-slide-transition.json', '$description': 'translations.json#/div_appearance_transition_slide'}], '$schema': 'http://json-schema.org/draft-07/schema'}, 'selected_actions': {'type': 'array', 'items': {'definitions': {'menu_item': {'type': 'object', 'properties': {'text': {'$ref': 'common.json#/non_empty_string', '$description': 'translations.json#/div_action_menu_item_text'}, 'action': {'$ref': 'div-action.json', '$description': 'translations.json#/div_action_menu_item_action'}, 'actions': {'type': 'array', 'items': {'$ref': 'div-action.json'}, 'minItems': 1, '$description': 'translations.json#/div_action_menu_item_actions'}}, 'required': ['text']}}, 'allOf': [{'$ref': 'div-action-base.json'}, {'type': 'object', '$description': 'translations.json#/div_action', 'properties': {'menu_items': {'type': 'array', 'items': {'$ref': '#/definitions/menu_item'}, '$description': 'translations.json#/div_action_menu_items', 'platforms': ['android', 'ios']}, 'log_url': {'$ref': 'common.json#/url', '$description': 'translations.json#/div_action_log_url'}, 'target': {'type': 'string', 'enum': ['_self', '_blank'], 'force_enum_field': True, '$description': 'translations.json#/div_action_target', 'platforms': ['web'], 'code_generation_disabled_swift': True}}, 'required': ['log_id']}], '$schema': 'http://json-schema.org/draft-07/schema'}, 'minItems': 1, '$description': 'translations.json#/div_base_selected_actions'}, 'focus': {'type': 'object', '$description': 'translations.json#/div_focus', 'properties': {'background': {'type': 'array', 'items': {'$ref': 'div-background.json'}, 'minItems': 1, '$description': 'translations.json#/div_focus_background'}, 'border': {'$ref': 'div-border.json', '$description': 'translations.json#/div_focus_border'}, 'on_focus': {'type': 'array', 'items': {'$ref': 'div-action.json'}, 'minItems': 1, '$description': 'translations.json#/div_focus_on_focus'}, 'on_blur': {'type': 'array', 'items': {'$ref': 'div-action.json'}, 'minItems': 1, '$description': 'translations.json#/div_focus_on_blur'}, 'next_focus_ids': {'type': 'object', '$description': 'translations.json#/div_focus_next_focus_ids', 'properties': {'forward': {'$ref': 'common.json#/non_empty_string'}, 'right': {'$ref': 'common.json#/non_empty_string'}, 'down': {'$ref': 'common.json#/non_empty_string'}, 'left': {'$ref': 'common.json#/non_empty_string'}, 'up': {'$ref': 'common.json#/non_empty_string'}}, 'platforms': ['android', 'ios']}}, '$schema': 'http://json-schema.org/draft-07/schema'}, 'visibility': {'type': 'string', 'enum': ['visible', 'invisible', 'gone'], '$description': 'translations.json#/div_visibility', '$schema': 'http://json-schema.org/draft-07/schema'}, 'transform': {'type': 'object', '$description': 'translations.json#/div_transform', 'properties': {'rotation': {'type': 'number', '$description': 'translations.json#/div_transform_rotation'}, 'pivot_x': {'$ref': 'div-pivot.json', 'default_value': '{"type": "pivot-percentage","value":50}', '$description': 'translations.json#/div_transform_pivot_x'}, 'pivot_y': {'$ref': 'div-pivot.json', 'default_value': '{"type": "pivot-percentage","value":50}', '$description': 'translations.json#/div_transform_pivot_y'}}, '$schema': 'http://json-schema.org/draft-07/schema'}}, '$schema': 'http://json-schema.org/draft-07/schema'}, rule='type')
 data_is_dict = isinstance(data, dict)
 if data_is_dict:
  data_keys = set(data.keys())
  if "id" in data_keys:
   data_keys.remove("id")
   data__id = data["id"]
   validate_common_json__non_empty_string(data__id, custom_formats, (name_prefix or "data") + ".id")
  if "border" in data_keys:
   data_keys.remove("border")
   data__border = data["border"]
   validate_div_border_json(data__border, custom_formats, (name_prefix or "data") + ".border")
  if "width" in data_keys:
   data_keys.remove("width")
   data__width = data["width"]
   validate_div_size_json(data__width, custom_formats, (name_prefix or "data") + ".width")
  if "height" in data_keys:
   data_keys.remove("height")
   data__height = data["height"]
   validate_div_size_json(data__height, custom_formats, (name_prefix or "data") + ".height")
  if "background" in data_keys:
   data_keys.remove("background")
   data__background = data["background"]
   if not isinstance(data__background, (list, tuple)):
    if not (isinstance(data__background, str) and '@' in data__background):
     raise JsonSchemaValueException("" + (name_prefix or "data") + ".background must be array", value=data__background, name="" + (name_prefix or "data") + ".background", definition={'type': 'array', 'items': {'anyOf': [{'$ref': 'div-linear-gradient.json', '$description': 'translations.json#/div_gradient_linear'}, {'$ref': 'div-radial-gradient.json', '$description': 'translations.json#/div_gradient_radial'}, {'$ref': 'div-image-background.json', '$description': 'translations.json#/div_background_image'}, {'$ref': 'div-solid-background.json', '$description': 'translations.json#/div_background_solid'}, {'$ref': 'div-nine-patch-background.json', '$description': 'translations.json#/div_nine_patch_background'}], '$schema': 'http://json-schema.org/draft-07/schema'}, 'minItems': 1, '$description': 'translations.json#/div_base_background'}, rule='type')
   data__background_is_list = isinstance(data__background, (list, tuple))
   if data__background_is_list:
    data__background_len = len(data__background)
    if data__background_len < 1:
     if not (isinstance(data__background, str) and '@' in data__background):
      raise JsonSchemaValueException("" + (name_prefix or "data") + ".background must contain at least 1 items", value=data__background, name="" + (name_prefix or "data") + ".background", definition={'type': 'array', 'items': {'anyOf': [{'$ref': 'div-linear-gradient.json', '$description': 'translations.json#/div_gradient_linear'}, {'$ref': 'div-radial-gradient.json', '$description': 'translations.json#/div_gradient_radial'}, {'$ref': 'div-image-background.json', '$description': 'translations.json#/div_background_image'}, {'$ref': 'div-solid-background.json', '$description': 'translations.json#/div_background_solid'}, {'$ref': 'div-nine-patch-background.json', '$description': 'translations.json#/div_nine_patch_background'}], '$schema': 'http://json-schema.org/draft-07/schema'}, 'minItems': 1, '$description': 'translations.json#/div_base_background'}, rule='minItems')
    for data__background_x, data__background_item in enumerate(data__background):
     validate_div_background_json(data__background_item, custom_formats, (name_prefix or "data") + ".background[{data__background_x}]".format(**locals()))
  if "paddings" in data_keys:
   data_keys.remove("paddings")
   data__paddings = data["paddings"]
   validate_div_edge_insets_json(data__paddings, custom_formats, (name_prefix or "data") + ".paddings")
  if "margins" in data_keys:
   data_keys.remove("margins")
   data__margins = data["margins"]
   validate_div_edge_insets_json(data__margins, custom_formats, (name_prefix or "data") + ".margins")
  if "alpha" in data_keys:
   data_keys.remove("alpha")
   data__alpha = data["alpha"]
   if not isinstance(data__alpha, (int, float, Decimal)) or isinstance(data__alpha, bool):
    if not (isinstance(data__alpha, str) and '@' in data__alpha):
     raise JsonSchemaValueException("" + (name_prefix or "data") + ".alpha must be number", value=data__alpha, name="" + (name_prefix or "data") + ".alpha", definition={'type': 'number', 'default_value': '1.0', 'constraint': 'number >= 0.0 && number <= 1.0', '$description': 'translations.json#/div_base_alpha'}, rule='type')
  if "alignment_vertical" in data_keys:
   data_keys.remove("alignment_vertical")
   data__alignmentvertical = data["alignment_vertical"]
   validate_div_alignment_vertical_json(data__alignmentvertical, custom_formats, (name_prefix or "data") + ".alignment_vertical")
  if "alignment_horizontal" in data_keys:
   data_keys.remove("alignment_horizontal")
   data__alignmenthorizontal = data["alignment_horizontal"]
   validate_div_alignment_horizontal_json(data__alignmenthorizontal, custom_formats, (name_prefix or "data") + ".alignment_horizontal")
  if "row_span" in data_keys:
   data_keys.remove("row_span")
   data__rowspan = data["row_span"]
   validate_common_json__non_negative_integer(data__rowspan, custom_formats, (name_prefix or "data") + ".row_span")
  if "column_span" in data_keys:
   data_keys.remove("column_span")
   data__columnspan = data["column_span"]
   validate_common_json__non_negative_integer(data__columnspan, custom_formats, (name_prefix or "data") + ".column_span")
  if "visibility_action" in data_keys:
   data_keys.remove("visibility_action")
   data__visibilityaction = data["visibility_action"]
   validate_div_visibility_action_json(data__visibilityaction, custom_formats, (name_prefix or "data") + ".visibility_action")
  if "visibility_actions" in data_keys:
   data_keys.remove("visibility_actions")
   data__visibilityactions = data["visibility_actions"]
   if not isinstance(data__visibilityactions, (list, tuple)):
    if not (isinstance(data__visibilityactions, str) and '@' in data__visibilityactions):
     raise JsonSchemaValueException("" + (name_prefix or "data") + ".visibility_actions must be array", value=data__visibilityactions, name="" + (name_prefix or "data") + ".visibility_actions", definition={'type': 'array', 'items': {'$description': 'translations.json#/div_visibility_action', 'allOf': [{'$ref': 'div-sight-action.json'}, {'properties': {'visibility_percentage': {'type': 'integer', 'constraint': 'number > 0 && number <= 100', 'default_value': '50', '$description': 'translations.json#/div_visibility_action_visibility_percentage'}, 'visibility_duration': {'$ref': 'common.json#/non_negative_integer', 'default_value': '800', '$description': 'translations.json#/div_visibility_action_visibility_duration'}}}], '$schema': 'http://json-schema.org/draft-07/schema'}, 'minItems': 1, '$description': 'translations.json#/div_base_visibility_actions'}, rule='type')
   data__visibilityactions_is_list = isinstance(data__visibilityactions, (list, tuple))
   if data__visibilityactions_is_list:
    data__visibilityactions_len = len(data__visibilityactions)
    if data__visibilityactions_len < 1:
     if not (isinstance(data__visibilityactions, str) and '@' in data__visibilityactions):
      raise JsonSchemaValueException("" + (name_prefix or "data") + ".visibility_actions must contain at least 1 items", value=data__visibilityactions, name="" + (name_prefix or "data") + ".visibility_actions", definition={'type': 'array', 'items': {'$description': 'translations.json#/div_visibility_action', 'allOf': [{'$ref': 'div-sight-action.json'}, {'properties': {'visibility_percentage': {'type': 'integer', 'constraint': 'number > 0 && number <= 100', 'default_value': '50', '$description': 'translations.json#/div_visibility_action_visibility_percentage'}, 'visibility_duration': {'$ref': 'common.json#/non_negative_integer', 'default_value': '800', '$description': 'translations.json#/div_visibility_action_visibility_duration'}}}], '$schema': 'http://json-schema.org/draft-07/schema'}, 'minItems': 1, '$description': 'translations.json#/div_base_visibility_actions'}, rule='minItems')
    for data__visibilityactions_x, data__visibilityactions_item in enumerate(data__visibilityactions):
     validate_div_visibility_action_json(data__visibilityactions_item, custom_formats, (name_prefix or "data") + ".visibility_actions[{data__visibilityactions_x}]".format(**locals()))
  if "disappear_actions" in data_keys:
   data_keys.remove("disappear_actions")
   data__disappearactions = data["disappear_actions"]
   if not isinstance(data__disappearactions, (list, tuple)):
    if not (isinstance(data__disappearactions, str) and '@' in data__disappearactions):
     raise JsonSchemaValueException("" + (name_prefix or "data") + ".disappear_actions must be array", value=data__disappearactions, name="" + (name_prefix or "data") + ".disappear_actions", definition={'type': 'array', 'items': {'$description': 'translations.json#/div_disappear_action', 'allOf': [{'$ref': 'div-sight-action.json'}, {'properties': {'visibility_percentage': {'type': 'integer', 'constraint': 'number >= 0 && number < 100', 'default_value': '0', '$description': 'translations.json#/div_disappear_action_visibility_percentage'}, 'disappear_duration': {'$ref': 'common.json#/non_negative_integer', 'default_value': '800', '$description': 'translations.json#/div_disappear_action_disappear_duration'}}}], '$schema': 'http://json-schema.org/draft-07/schema'}, 'minItems': 1, '$description': 'translations.json#/div_base_disappear_actions'}, rule='type')
   data__disappearactions_is_list = isinstance(data__disappearactions, (list, tuple))
   if data__disappearactions_is_list:
    data__disappearactions_len = len(data__disappearactions)
    if data__disappearactions_len < 1:
     if not (isinstance(data__disappearactions, str) and '@' in data__disappearactions):
      raise JsonSchemaValueException("" + (name_prefix or "data") + ".disappear_actions must contain at least 1 items", value=data__disappearactions, name="" + (name_prefix or "data") + ".disappear_actions", definition={'type': 'array', 'items': {'$description': 'translations.json#/div_disappear_action', 'allOf': [{'$ref': 'div-sight-action.json'}, {'properties': {'visibility_percentage': {'type': 'integer', 'constraint': 'number >= 0 && number < 100', 'default_value': '0', '$description': 'translations.json#/div_disappear_action_visibility_percentage'}, 'disappear_duration': {'$ref': 'common.json#/non_negative_integer', 'default_value': '800', '$description': 'translations.json#/div_disappear_action_disappear_duration'}}}], '$schema': 'http://json-schema.org/draft-07/schema'}, 'minItems': 1, '$description': 'translations.json#/div_base_disappear_actions'}, rule='minItems')
    for data__disappearactions_x, data__disappearactions_item in enumerate(data__disappearactions):
     validate_div_disappear_action_json(data__disappearactions_item, custom_formats, (name_prefix or "data") + ".disappear_actions[{data__disappearactions_x}]".format(**locals()))
  if "tooltips" in data_keys:
   data_keys.remove("tooltips")
   data__tooltips = data["tooltips"]
   if not isinstance(data__tooltips, (list, tuple)):
    if not (isinstance(data__tooltips, str) and '@' in data__tooltips):
     raise JsonSchemaValueException("" + (name_prefix or "data") + ".tooltips must be array", value=data__tooltips, name="" + (name_prefix or "data") + ".tooltips", definition={'type': 'array', 'items': {'type': 'object', '$description': 'translations.json#/div_tooltip', 'properties': {'id': {'$ref': 'common.json#/non_empty_string', 'supports_expressions': False, '$description': 'translations.json#/div_tooltip_id'}, 'div': {'$ref': 'div.json', '$description': 'translations.json#/div_tooltip_div'}, 'position': {'type': 'string', 'enum': ['left', 'top-left', 'top', 'top-right', 'right', 'bottom-right', 'bottom', 'bottom-left', 'center'], '$description': 'translations.json#/div_tooltip_position'}, 'duration': {'$ref': 'common.json#/non_negative_integer', 'default_value': '5000', '$description': 'translations.json#/div_tooltip_duration'}, 'offset': {'$ref': 'div-point.json', '$description': 'translations.json#/div_tooltip_offset'}, 'animation_in': {'$ref': 'div-animation.json', '$description': 'translations.json#/div_tooltip_animation_in'}, 'animation_out': {'$ref': 'div-animation.json', '$description': 'translations.json#/div_tooltip_animation_out'}}, 'required': ['id', 'div', 'position'], '$schema': 'http://json-schema.org/draft-07/schema'}, 'minItems': 1, '$description': 'translations.json#/div_base_tooltips'}, rule='type')
   data__tooltips_is_list = isinstance(data__tooltips, (list, tuple))
   if data__tooltips_is_list:
    data__tooltips_len = len(data__tooltips)
    if data__tooltips_len < 1:
     if not (isinstance(data__tooltips, str) and '@' in data__tooltips):
      raise JsonSchemaValueException("" + (name_prefix or "data") + ".tooltips must contain at least 1 items", value=data__tooltips, name="" + (name_prefix or "data") + ".tooltips", definition={'type': 'array', 'items': {'type': 'object', '$description': 'translations.json#/div_tooltip', 'properties': {'id': {'$ref': 'common.json#/non_empty_string', 'supports_expressions': False, '$description': 'translations.json#/div_tooltip_id'}, 'div': {'$ref': 'div.json', '$description': 'translations.json#/div_tooltip_div'}, 'position': {'type': 'string', 'enum': ['left', 'top-left', 'top', 'top-right', 'right', 'bottom-right', 'bottom', 'bottom-left', 'center'], '$description': 'translations.json#/div_tooltip_position'}, 'duration': {'$ref': 'common.json#/non_negative_integer', 'default_value': '5000', '$description': 'translations.json#/div_tooltip_duration'}, 'offset': {'$ref': 'div-point.json', '$description': 'translations.json#/div_tooltip_offset'}, 'animation_in': {'$ref': 'div-animation.json', '$description': 'translations.json#/div_tooltip_animation_in'}, 'animation_out': {'$ref': 'div-animation.json', '$description': 'translations.json#/div_tooltip_animation_out'}}, 'required': ['id', 'div', 'position'], '$schema': 'http://json-schema.org/draft-07/schema'}, 'minItems': 1, '$description': 'translations.json#/div_base_tooltips'}, rule='minItems')
    for data__tooltips_x, data__tooltips_item in enumerate(data__tooltips):
     validate_div_tooltip_json(data__tooltips_item, custom_formats, (name_prefix or "data") + ".tooltips[{data__tooltips_x}]".format(**locals()))
  if "accessibility" in data_keys:
   data_keys.remove("accessibility")
   data__accessibility = data["accessibility"]
   validate_div_accessibility_json(data__accessibility, custom_formats, (name_prefix or "data") + ".accessibility")
  if "extensions" in data_keys:
   data_keys.remove("extensions")
   data__extensions = data["extensions"]
   if not isinstance(data__extensions, (list, tuple)):
    if not (isinstance(data__extensions, str) and '@' in data__extensions):
     raise JsonSchemaValueException("" + (name_prefix or "data") + ".extensions must be array", value=data__extensions, name="" + (name_prefix or "data") + ".extensions", definition={'type': 'array', 'items': {'type': 'object', '$description': 'translations.json#/div_extension', 'properties': {'id': {'$ref': 'common.json#/non_empty_string', 'supports_expressions': False, '$description': 'translations.json#/div_extension_id'}, 'params': {'type': 'object', 'additionalProperties': True, '$description': 'translations.json#/div_extension_params'}}, 'required': ['id'], '$schema': 'http://json-schema.org/draft-07/schema'}, 'minItems': 1, '$description': 'translations.json#/div_base_extensions'}, rule='type')
   data__extensions_is_list = isinstance(data__extensions, (list, tuple))
   if data__extensions_is_list:
    data__extensions_len = len(data__extensions)
    if data__extensions_len < 1:
     if not (isinstance(data__extensions, str) and '@' in data__extensions):
      raise JsonSchemaValueException("" + (name_prefix or "data") + ".extensions must contain at least 1 items", value=data__extensions, name="" + (name_prefix or "data") + ".extensions", definition={'type': 'array', 'items': {'type': 'object', '$description': 'translations.json#/div_extension', 'properties': {'id': {'$ref': 'common.json#/non_empty_string', 'supports_expressions': False, '$description': 'translations.json#/div_extension_id'}, 'params': {'type': 'object', 'additionalProperties': True, '$description': 'translations.json#/div_extension_params'}}, 'required': ['id'], '$schema': 'http://json-schema.org/draft-07/schema'}, 'minItems': 1, '$description': 'translations.json#/div_base_extensions'}, rule='minItems')
    for data__extensions_x, data__extensions_item in enumerate(data__extensions):
     validate_div_extension_json(data__extensions_item, custom_formats, (name_prefix or "data") + ".extensions[{data__extensions_x}]".format(**locals()))
  if "transition_triggers" in data_keys:
   data_keys.remove("transition_triggers")
   data__transitiontriggers = data["transition_triggers"]
   if not isinstance(data__transitiontriggers, (list, tuple)):
    if not (isinstance(data__transitiontriggers, str) and '@' in data__transitiontriggers):
     raise JsonSchemaValueException("" + (name_prefix or "data") + ".transition_triggers must be array", value=data__transitiontriggers, name="" + (name_prefix or "data") + ".transition_triggers", definition={'type': 'array', 'items': {'type': 'string', 'enum': ['data_change', 'state_change', 'visibility_change'], '$description': 'translations.json#/div_transition_trigger', '$schema': 'http://json-schema.org/draft-07/schema'}, 'minItems': 1, 'supports_expressions': False, '$description': 'translations.json#/div_base_transition_triggers'}, rule='type')
   data__transitiontriggers_is_list = isinstance(data__transitiontriggers, (list, tuple))
   if data__transitiontriggers_is_list:
    data__transitiontriggers_len = len(data__transitiontriggers)
    if data__transitiontriggers_len < 1:
     if not (isinstance(data__transitiontriggers, str) and '@' in data__transitiontriggers):
      raise JsonSchemaValueException("" + (name_prefix or "data") + ".transition_triggers must contain at least 1 items", value=data__transitiontriggers, name="" + (name_prefix or "data") + ".transition_triggers", definition={'type': 'array', 'items': {'type': 'string', 'enum': ['data_change', 'state_change', 'visibility_change'], '$description': 'translations.json#/div_transition_trigger', '$schema': 'http://json-schema.org/draft-07/schema'}, 'minItems': 1, 'supports_expressions': False, '$description': 'translations.json#/div_base_transition_triggers'}, rule='minItems')
    for data__transitiontriggers_x, data__transitiontriggers_item in enumerate(data__transitiontriggers):
     validate_div_transition_trigger_json(data__transitiontriggers_item, custom_formats, (name_prefix or "data") + ".transition_triggers[{data__transitiontriggers_x}]".format(**locals()))
  if "transition_in" in data_keys:
   data_keys.remove("transition_in")
   data__transitionin = data["transition_in"]
   validate_div_appearance_transition_json(data__transitionin, custom_formats, (name_prefix or "data") + ".transition_in")
  if "transition_change" in data_keys:
   data_keys.remove("transition_change")
   data__transitionchange = data["transition_change"]
   validate_div_change_transition_json(data__transitionchange, custom_formats, (name_prefix or "data") + ".transition_change")
  if "transition_out" in data_keys:
   data_keys.remove("transition_out")
   data__transitionout = data["transition_out"]
   validate_div_appearance_transition_json(data__transitionout, custom_formats, (name_prefix or "data") + ".transition_out")
  if "selected_actions" in data_keys:
   data_keys.remove("selected_actions")
   data__selectedactions = data["selected_actions"]
   if not isinstance(data__selectedactions, (list, tuple)):
    if not (isinstance(data__selectedactions, str) and '@' in data__selectedactions):
     raise JsonSchemaValueException("" + (name_prefix or "data") + ".selected_actions must be array", value=data__selectedactions, name="" + (name_prefix or "data") + ".selected_actions", definition={'type': 'array', 'items': {'definitions': {'menu_item': {'type': 'object', 'properties': {'text': {'$ref': 'common.json#/non_empty_string', '$description': 'translations.json#/div_action_menu_item_text'}, 'action': {'$ref': 'div-action.json', '$description': 'translations.json#/div_action_menu_item_action'}, 'actions': {'type': 'array', 'items': {'$ref': 'div-action.json'}, 'minItems': 1, '$description': 'translations.json#/div_action_menu_item_actions'}}, 'required': ['text']}}, 'allOf': [{'$ref': 'div-action-base.json'}, {'type': 'object', '$description': 'translations.json#/div_action', 'properties': {'menu_items': {'type': 'array', 'items': {'$ref': '#/definitions/menu_item'}, '$description': 'translations.json#/div_action_menu_items', 'platforms': ['android', 'ios']}, 'log_url': {'$ref': 'common.json#/url', '$description': 'translations.json#/div_action_log_url'}, 'target': {'type': 'string', 'enum': ['_self', '_blank'], 'force_enum_field': True, '$description': 'translations.json#/div_action_target', 'platforms': ['web'], 'code_generation_disabled_swift': True}}, 'required': ['log_id']}], '$schema': 'http://json-schema.org/draft-07/schema'}, 'minItems': 1, '$description': 'translations.json#/div_base_selected_actions'}, rule='type')
   data__selectedactions_is_list = isinstance(data__selectedactions, (list, tuple))
   if data__selectedactions_is_list:
    data__selectedactions_len = len(data__selectedactions)
    if data__selectedactions_len < 1:
     if not (isinstance(data__selectedactions, str) and '@' in data__selectedactions):
      raise JsonSchemaValueException("" + (name_prefix or "data") + ".selected_actions must contain at least 1 items", value=data__selectedactions, name="" + (name_prefix or "data") + ".selected_actions", definition={'type': 'array', 'items': {'definitions': {'menu_item': {'type': 'object', 'properties': {'text': {'$ref': 'common.json#/non_empty_string', '$description': 'translations.json#/div_action_menu_item_text'}, 'action': {'$ref': 'div-action.json', '$description': 'translations.json#/div_action_menu_item_action'}, 'actions': {'type': 'array', 'items': {'$ref': 'div-action.json'}, 'minItems': 1, '$description': 'translations.json#/div_action_menu_item_actions'}}, 'required': ['text']}}, 'allOf': [{'$ref': 'div-action-base.json'}, {'type': 'object', '$description': 'translations.json#/div_action', 'properties': {'menu_items': {'type': 'array', 'items': {'$ref': '#/definitions/menu_item'}, '$description': 'translations.json#/div_action_menu_items', 'platforms': ['android', 'ios']}, 'log_url': {'$ref': 'common.json#/url', '$description': 'translations.json#/div_action_log_url'}, 'target': {'type': 'string', 'enum': ['_self', '_blank'], 'force_enum_field': True, '$description': 'translations.json#/div_action_target', 'platforms': ['web'], 'code_generation_disabled_swift': True}}, 'required': ['log_id']}], '$schema': 'http://json-schema.org/draft-07/schema'}, 'minItems': 1, '$description': 'translations.json#/div_base_selected_actions'}, rule='minItems')
    for data__selectedactions_x, data__selectedactions_item in enumerate(data__selectedactions):
     validate_div_action_json(data__selectedactions_item, custom_formats, (name_prefix or "data") + ".selected_actions[{data__selectedactions_x}]".format(**locals()))
  if "focus" in data_keys:
   data_keys.remove("focus")
   data__focus = data["focus"]
   validate_div_focus_json(data__focus, custom_formats, (name_prefix or "data") + ".focus")
  if "visibility" in data_keys:
   data_keys.remove("visibility")
   data__visibility = data["visibility"]
   validate_div_visibility_json(data__visibility, custom_formats, (name_prefix or "data") + ".visibility")
  if "transform" in data_keys:
   data_keys.remove("transform")
   data__transform = data["transform"]
   validate_div_transform_json(data__transform, custom_formats, (name_prefix or "data") + ".transform")
 return data

def validate_div_transform_json(data, custom_formats={}, name_prefix=None):
 if not isinstance(data, (dict)):
  if not (isinstance(data, str) and '@' in data):
   raise JsonSchemaValueException("" + (name_prefix or "data") + " must be object", value=data, name="" + (name_prefix or "data") + "", definition={'type': 'object', '$description': 'translations.json#/div_transform', 'properties': {'rotation': {'type': 'number', '$description': 'translations.json#/div_transform_rotation'}, 'pivot_x': {'anyOf': [{'$ref': 'div-pivot-fixed.json', '$description': 'translations.json#/div_pivot_fixed'}, {'$ref': 'div-pivot-percentage.json', '$description': 'translations.json#/div_pivot_percentage'}], '$schema': 'http://json-schema.org/draft-07/schema'}, 'pivot_y': {'anyOf': [{'$ref': 'div-pivot-fixed.json', '$description': 'translations.json#/div_pivot_fixed'}, {'$ref': 'div-pivot-percentage.json', '$description': 'translations.json#/div_pivot_percentage'}], '$schema': 'http://json-schema.org/draft-07/schema'}}, '$schema': 'http://json-schema.org/draft-07/schema'}, rule='type')
 data_is_dict = isinstance(data, dict)
 if data_is_dict:
  data_keys = set(data.keys())
  if "rotation" in data_keys:
   data_keys.remove("rotation")
   data__rotation = data["rotation"]
   if not isinstance(data__rotation, (int, float, Decimal)) or isinstance(data__rotation, bool):
    if not (isinstance(data__rotation, str) and '@' in data__rotation):
     raise JsonSchemaValueException("" + (name_prefix or "data") + ".rotation must be number", value=data__rotation, name="" + (name_prefix or "data") + ".rotation", definition={'type': 'number', '$description': 'translations.json#/div_transform_rotation'}, rule='type')
  if "pivot_x" in data_keys:
   data_keys.remove("pivot_x")
   data__pivotx = data["pivot_x"]
   validate_div_pivot_json(data__pivotx, custom_formats, (name_prefix or "data") + ".pivot_x")
  if "pivot_y" in data_keys:
   data_keys.remove("pivot_y")
   data__pivoty = data["pivot_y"]
   validate_div_pivot_json(data__pivoty, custom_formats, (name_prefix or "data") + ".pivot_y")
 return data

def validate_div_pivot_json(data, custom_formats={}, name_prefix=None):
 data_any_of_count6 = 0
 if not data_any_of_count6:
  try:
   validate_div_pivot_fixed_json(data, custom_formats, (name_prefix or "data") + "")
   data_any_of_count6 += 1
  except JsonSchemaValueException: pass
 if not data_any_of_count6:
  try:
   validate_div_pivot_percentage_json(data, custom_formats, (name_prefix or "data") + "")
   data_any_of_count6 += 1
  except JsonSchemaValueException: pass
 if not data_any_of_count6:
  if not (isinstance(data, str) and '@' in data):
   raise JsonSchemaValueException("" + (name_prefix or "data") + " cannot be validated by any definition", value=data, name="" + (name_prefix or "data") + "", definition={'anyOf': [{'type': 'object', '$description': 'translations.json#/div_pivot_fixed_short', 'properties': {'value': {'type': 'integer', '$description': 'translations.json#/div_pivot_fixed_value'}, 'unit': {'$ref': 'div-size-unit.json', '$description': 'translations.json#/div_pivot_fixed_unit', 'default_value': 'dp'}, 'type': {'type': 'string', 'enum': ['pivot-fixed']}}, '$schema': 'http://json-schema.org/draft-07/schema'}, {'type': 'object', '$description': 'translations.json#/div_pivot_percentage_short', 'properties': {'value': {'type': 'number', '$description': 'translations.json#/div_pivot_percentage_value'}, 'type': {'type': 'string', 'enum': ['pivot-percentage']}}, 'required': ['type', 'value'], '$schema': 'http://json-schema.org/draft-07/schema'}], '$schema': 'http://json-schema.org/draft-07/schema'}, rule='anyOf')
 return data

def validate_div_pivot_percentage_json(data, custom_formats={}, name_prefix=None):
 if not isinstance(data, (dict)):
  if not (isinstance(data, str) and '@' in data):
   raise JsonSchemaValueException("" + (name_prefix or "data") + " must be object", value=data, name="" + (name_prefix or "data") + "", definition={'type': 'object', '$description': 'translations.json#/div_pivot_percentage_short', 'properties': {'value': {'type': 'number', '$description': 'translations.json#/div_pivot_percentage_value'}, 'type': {'type': 'string', 'enum': ['pivot-percentage']}}, 'required': ['type', 'value'], '$schema': 'http://json-schema.org/draft-07/schema'}, rule='type')
 data_is_dict = isinstance(data, dict)
 if data_is_dict:
  data__missing_keys = set(['type', 'value']) - data.keys()
  if data__missing_keys:
   if not (isinstance(data, str) and '@' in data):
    raise JsonSchemaValueException("" + (name_prefix or "data") + " must contain " + (str(sorted(data__missing_keys)) + " properties"), value=data, name="" + (name_prefix or "data") + "", definition={'type': 'object', '$description': 'translations.json#/div_pivot_percentage_short', 'properties': {'value': {'type': 'number', '$description': 'translations.json#/div_pivot_percentage_value'}, 'type': {'type': 'string', 'enum': ['pivot-percentage']}}, 'required': ['type', 'value'], '$schema': 'http://json-schema.org/draft-07/schema'}, rule='required')
  data_keys = set(data.keys())
  if "value" in data_keys:
   data_keys.remove("value")
   data__value = data["value"]
   if not isinstance(data__value, (int, float, Decimal)) or isinstance(data__value, bool):
    if not (isinstance(data__value, str) and '@' in data__value):
     raise JsonSchemaValueException("" + (name_prefix or "data") + ".value must be number", value=data__value, name="" + (name_prefix or "data") + ".value", definition={'type': 'number', '$description': 'translations.json#/div_pivot_percentage_value'}, rule='type')
  if "type" in data_keys:
   data_keys.remove("type")
   data__type = data["type"]
   if not isinstance(data__type, (str)):
    if not (isinstance(data__type, str) and '@' in data__type):
     raise JsonSchemaValueException("" + (name_prefix or "data") + ".type must be string", value=data__type, name="" + (name_prefix or "data") + ".type", definition={'type': 'string', 'enum': ['pivot-percentage']}, rule='type')
   if data__type not in ['pivot-percentage']:
    if not (isinstance(data__type, str) and '@' in data__type):
     raise JsonSchemaValueException("" + (name_prefix or "data") + ".type must be one of ['pivot-percentage']", value=data__type, name="" + (name_prefix or "data") + ".type", definition={'type': 'string', 'enum': ['pivot-percentage']}, rule='enum')
 return data

def validate_div_pivot_fixed_json(data, custom_formats={}, name_prefix=None):
 if not isinstance(data, (dict)):
  if not (isinstance(data, str) and '@' in data):
   raise JsonSchemaValueException("" + (name_prefix or "data") + " must be object", value=data, name="" + (name_prefix or "data") + "", definition={'type': 'object', '$description': 'translations.json#/div_pivot_fixed_short', 'properties': {'value': {'type': 'integer', '$description': 'translations.json#/div_pivot_fixed_value'}, 'unit': {'type': 'string', 'enum': ['dp', 'sp', 'px'], '$description': 'translations.json#/div_size_unit', 'platforms': ['android', 'ios'], '$schema': 'http://json-schema.org/draft-07/schema'}, 'type': {'type': 'string', 'enum': ['pivot-fixed']}}, '$schema': 'http://json-schema.org/draft-07/schema'}, rule='type')
 data_is_dict = isinstance(data, dict)
 if data_is_dict:
  data_keys = set(data.keys())
  if "value" in data_keys:
   data_keys.remove("value")
   data__value = data["value"]
   if not isinstance(data__value, (int)) and not (isinstance(data__value, float) and data__value.is_integer()) or isinstance(data__value, bool):
    if not (isinstance(data__value, str) and '@' in data__value):
     raise JsonSchemaValueException("" + (name_prefix or "data") + ".value must be integer", value=data__value, name="" + (name_prefix or "data") + ".value", definition={'type': 'integer', '$description': 'translations.json#/div_pivot_fixed_value'}, rule='type')
  if "unit" in data_keys:
   data_keys.remove("unit")
   data__unit = data["unit"]
   validate_div_size_unit_json(data__unit, custom_formats, (name_prefix or "data") + ".unit")
  if "type" in data_keys:
   data_keys.remove("type")
   data__type = data["type"]
   if not isinstance(data__type, (str)):
    if not (isinstance(data__type, str) and '@' in data__type):
     raise JsonSchemaValueException("" + (name_prefix or "data") + ".type must be string", value=data__type, name="" + (name_prefix or "data") + ".type", definition={'type': 'string', 'enum': ['pivot-fixed']}, rule='type')
   if data__type not in ['pivot-fixed']:
    if not (isinstance(data__type, str) and '@' in data__type):
     raise JsonSchemaValueException("" + (name_prefix or "data") + ".type must be one of ['pivot-fixed']", value=data__type, name="" + (name_prefix or "data") + ".type", definition={'type': 'string', 'enum': ['pivot-fixed']}, rule='enum')
 return data

def validate_div_size_unit_json(data, custom_formats={}, name_prefix=None):
 if not isinstance(data, (str)):
  if not (isinstance(data, str) and '@' in data):
   raise JsonSchemaValueException("" + (name_prefix or "data") + " must be string", value=data, name="" + (name_prefix or "data") + "", definition={'type': 'string', 'enum': ['dp', 'sp', 'px'], '$description': 'translations.json#/div_size_unit', 'platforms': ['android', 'ios'], '$schema': 'http://json-schema.org/draft-07/schema'}, rule='type')
 if data not in ['dp', 'sp', 'px']:
  if not (isinstance(data, str) and '@' in data):
   raise JsonSchemaValueException("" + (name_prefix or "data") + " must be one of ['dp', 'sp', 'px']", value=data, name="" + (name_prefix or "data") + "", definition={'type': 'string', 'enum': ['dp', 'sp', 'px'], '$description': 'translations.json#/div_size_unit', 'platforms': ['android', 'ios'], '$schema': 'http://json-schema.org/draft-07/schema'}, rule='enum')
 return data

def validate_div_visibility_json(data, custom_formats={}, name_prefix=None):
 if not isinstance(data, (str)):
  if not (isinstance(data, str) and '@' in data):
   raise JsonSchemaValueException("" + (name_prefix or "data") + " must be string", value=data, name="" + (name_prefix or "data") + "", definition={'type': 'string', 'enum': ['visible', 'invisible', 'gone'], '$description': 'translations.json#/div_visibility', '$schema': 'http://json-schema.org/draft-07/schema'}, rule='type')
 if data not in ['visible', 'invisible', 'gone']:
  if not (isinstance(data, str) and '@' in data):
   raise JsonSchemaValueException("" + (name_prefix or "data") + " must be one of ['visible', 'invisible', 'gone']", value=data, name="" + (name_prefix or "data") + "", definition={'type': 'string', 'enum': ['visible', 'invisible', 'gone'], '$description': 'translations.json#/div_visibility', '$schema': 'http://json-schema.org/draft-07/schema'}, rule='enum')
 return data

def validate_div_focus_json(data, custom_formats={}, name_prefix=None):
 if not isinstance(data, (dict)):
  if not (isinstance(data, str) and '@' in data):
   raise JsonSchemaValueException("" + (name_prefix or "data") + " must be object", value=data, name="" + (name_prefix or "data") + "", definition={'type': 'object', '$description': 'translations.json#/div_focus', 'properties': {'background': {'type': 'array', 'items': {'anyOf': [{'$ref': 'div-linear-gradient.json', '$description': 'translations.json#/div_gradient_linear'}, {'$ref': 'div-radial-gradient.json', '$description': 'translations.json#/div_gradient_radial'}, {'$ref': 'div-image-background.json', '$description': 'translations.json#/div_background_image'}, {'$ref': 'div-solid-background.json', '$description': 'translations.json#/div_background_solid'}, {'$ref': 'div-nine-patch-background.json', '$description': 'translations.json#/div_nine_patch_background'}], '$schema': 'http://json-schema.org/draft-07/schema'}, 'minItems': 1, '$description': 'translations.json#/div_focus_background'}, 'border': {'type': 'object', '$description': 'translations.json#/div_border', 'properties': {'has_shadow': {'$ref': 'common.json#/boolean_int', 'default_value': 'false', '$description': 'translations.json#/div_border_has_shadow'}, 'shadow': {'$ref': 'div-shadow.json', '$description': 'translations.json#/div_border_shadow'}, 'stroke': {'$ref': 'div-stroke.json', '$description': 'translations.json#/div_border_stroke'}, 'corner_radius': {'$ref': 'common.json#/non_negative_integer', '$description': 'translations.json#/div_border_corner_radius'}, 'corners_radius': {'$ref': 'div-corners-radius.json', '$description': 'translations.json#/div_border_corners_radius'}}, '$schema': 'http://json-schema.org/draft-07/schema'}, 'on_focus': {'type': 'array', 'items': {'definitions': {'menu_item': {'type': 'object', 'properties': {'text': {'$ref': 'common.json#/non_empty_string', '$description': 'translations.json#/div_action_menu_item_text'}, 'action': {'$ref': 'div-action.json', '$description': 'translations.json#/div_action_menu_item_action'}, 'actions': {'type': 'array', 'items': {'$ref': 'div-action.json'}, 'minItems': 1, '$description': 'translations.json#/div_action_menu_item_actions'}}, 'required': ['text']}}, 'allOf': [{'$ref': 'div-action-base.json'}, {'type': 'object', '$description': 'translations.json#/div_action', 'properties': {'menu_items': {'type': 'array', 'items': {'$ref': '#/definitions/menu_item'}, '$description': 'translations.json#/div_action_menu_items', 'platforms': ['android', 'ios']}, 'log_url': {'$ref': 'common.json#/url', '$description': 'translations.json#/div_action_log_url'}, 'target': {'type': 'string', 'enum': ['_self', '_blank'], 'force_enum_field': True, '$description': 'translations.json#/div_action_target', 'platforms': ['web'], 'code_generation_disabled_swift': True}}, 'required': ['log_id']}], '$schema': 'http://json-schema.org/draft-07/schema'}, 'minItems': 1, '$description': 'translations.json#/div_focus_on_focus'}, 'on_blur': {'type': 'array', 'items': {'definitions': {'menu_item': {'type': 'object', 'properties': {'text': {'$ref': 'common.json#/non_empty_string', '$description': 'translations.json#/div_action_menu_item_text'}, 'action': {'$ref': 'div-action.json', '$description': 'translations.json#/div_action_menu_item_action'}, 'actions': {'type': 'array', 'items': {'$ref': 'div-action.json'}, 'minItems': 1, '$description': 'translations.json#/div_action_menu_item_actions'}}, 'required': ['text']}}, 'allOf': [{'$ref': 'div-action-base.json'}, {'type': 'object', '$description': 'translations.json#/div_action', 'properties': {'menu_items': {'type': 'array', 'items': {'$ref': '#/definitions/menu_item'}, '$description': 'translations.json#/div_action_menu_items', 'platforms': ['android', 'ios']}, 'log_url': {'$ref': 'common.json#/url', '$description': 'translations.json#/div_action_log_url'}, 'target': {'type': 'string', 'enum': ['_self', '_blank'], 'force_enum_field': True, '$description': 'translations.json#/div_action_target', 'platforms': ['web'], 'code_generation_disabled_swift': True}}, 'required': ['log_id']}], '$schema': 'http://json-schema.org/draft-07/schema'}, 'minItems': 1, '$description': 'translations.json#/div_focus_on_blur'}, 'next_focus_ids': {'type': 'object', '$description': 'translations.json#/div_focus_next_focus_ids', 'properties': {'forward': {'type': 'string', 'minLength': 1, 'clientMinLength': 1}, 'right': {'type': 'string', 'minLength': 1, 'clientMinLength': 1}, 'down': {'type': 'string', 'minLength': 1, 'clientMinLength': 1}, 'left': {'type': 'string', 'minLength': 1, 'clientMinLength': 1}, 'up': {'type': 'string', 'minLength': 1, 'clientMinLength': 1}}, 'platforms': ['android', 'ios']}}, '$schema': 'http://json-schema.org/draft-07/schema'}, rule='type')
 data_is_dict = isinstance(data, dict)
 if data_is_dict:
  data_keys = set(data.keys())
  if "background" in data_keys:
   data_keys.remove("background")
   data__background = data["background"]
   if not isinstance(data__background, (list, tuple)):
    if not (isinstance(data__background, str) and '@' in data__background):
     raise JsonSchemaValueException("" + (name_prefix or "data") + ".background must be array", value=data__background, name="" + (name_prefix or "data") + ".background", definition={'type': 'array', 'items': {'anyOf': [{'$ref': 'div-linear-gradient.json', '$description': 'translations.json#/div_gradient_linear'}, {'$ref': 'div-radial-gradient.json', '$description': 'translations.json#/div_gradient_radial'}, {'$ref': 'div-image-background.json', '$description': 'translations.json#/div_background_image'}, {'$ref': 'div-solid-background.json', '$description': 'translations.json#/div_background_solid'}, {'$ref': 'div-nine-patch-background.json', '$description': 'translations.json#/div_nine_patch_background'}], '$schema': 'http://json-schema.org/draft-07/schema'}, 'minItems': 1, '$description': 'translations.json#/div_focus_background'}, rule='type')
   data__background_is_list = isinstance(data__background, (list, tuple))
   if data__background_is_list:
    data__background_len = len(data__background)
    if data__background_len < 1:
     if not (isinstance(data__background, str) and '@' in data__background):
      raise JsonSchemaValueException("" + (name_prefix or "data") + ".background must contain at least 1 items", value=data__background, name="" + (name_prefix or "data") + ".background", definition={'type': 'array', 'items': {'anyOf': [{'$ref': 'div-linear-gradient.json', '$description': 'translations.json#/div_gradient_linear'}, {'$ref': 'div-radial-gradient.json', '$description': 'translations.json#/div_gradient_radial'}, {'$ref': 'div-image-background.json', '$description': 'translations.json#/div_background_image'}, {'$ref': 'div-solid-background.json', '$description': 'translations.json#/div_background_solid'}, {'$ref': 'div-nine-patch-background.json', '$description': 'translations.json#/div_nine_patch_background'}], '$schema': 'http://json-schema.org/draft-07/schema'}, 'minItems': 1, '$description': 'translations.json#/div_focus_background'}, rule='minItems')
    for data__background_x, data__background_item in enumerate(data__background):
     validate_div_background_json(data__background_item, custom_formats, (name_prefix or "data") + ".background[{data__background_x}]".format(**locals()))
  if "border" in data_keys:
   data_keys.remove("border")
   data__border = data["border"]
   validate_div_border_json(data__border, custom_formats, (name_prefix or "data") + ".border")
  if "on_focus" in data_keys:
   data_keys.remove("on_focus")
   data__onfocus = data["on_focus"]
   if not isinstance(data__onfocus, (list, tuple)):
    if not (isinstance(data__onfocus, str) and '@' in data__onfocus):
     raise JsonSchemaValueException("" + (name_prefix or "data") + ".on_focus must be array", value=data__onfocus, name="" + (name_prefix or "data") + ".on_focus", definition={'type': 'array', 'items': {'definitions': {'menu_item': {'type': 'object', 'properties': {'text': {'$ref': 'common.json#/non_empty_string', '$description': 'translations.json#/div_action_menu_item_text'}, 'action': {'$ref': 'div-action.json', '$description': 'translations.json#/div_action_menu_item_action'}, 'actions': {'type': 'array', 'items': {'$ref': 'div-action.json'}, 'minItems': 1, '$description': 'translations.json#/div_action_menu_item_actions'}}, 'required': ['text']}}, 'allOf': [{'$ref': 'div-action-base.json'}, {'type': 'object', '$description': 'translations.json#/div_action', 'properties': {'menu_items': {'type': 'array', 'items': {'$ref': '#/definitions/menu_item'}, '$description': 'translations.json#/div_action_menu_items', 'platforms': ['android', 'ios']}, 'log_url': {'$ref': 'common.json#/url', '$description': 'translations.json#/div_action_log_url'}, 'target': {'type': 'string', 'enum': ['_self', '_blank'], 'force_enum_field': True, '$description': 'translations.json#/div_action_target', 'platforms': ['web'], 'code_generation_disabled_swift': True}}, 'required': ['log_id']}], '$schema': 'http://json-schema.org/draft-07/schema'}, 'minItems': 1, '$description': 'translations.json#/div_focus_on_focus'}, rule='type')
   data__onfocus_is_list = isinstance(data__onfocus, (list, tuple))
   if data__onfocus_is_list:
    data__onfocus_len = len(data__onfocus)
    if data__onfocus_len < 1:
     if not (isinstance(data__onfocus, str) and '@' in data__onfocus):
      raise JsonSchemaValueException("" + (name_prefix or "data") + ".on_focus must contain at least 1 items", value=data__onfocus, name="" + (name_prefix or "data") + ".on_focus", definition={'type': 'array', 'items': {'definitions': {'menu_item': {'type': 'object', 'properties': {'text': {'$ref': 'common.json#/non_empty_string', '$description': 'translations.json#/div_action_menu_item_text'}, 'action': {'$ref': 'div-action.json', '$description': 'translations.json#/div_action_menu_item_action'}, 'actions': {'type': 'array', 'items': {'$ref': 'div-action.json'}, 'minItems': 1, '$description': 'translations.json#/div_action_menu_item_actions'}}, 'required': ['text']}}, 'allOf': [{'$ref': 'div-action-base.json'}, {'type': 'object', '$description': 'translations.json#/div_action', 'properties': {'menu_items': {'type': 'array', 'items': {'$ref': '#/definitions/menu_item'}, '$description': 'translations.json#/div_action_menu_items', 'platforms': ['android', 'ios']}, 'log_url': {'$ref': 'common.json#/url', '$description': 'translations.json#/div_action_log_url'}, 'target': {'type': 'string', 'enum': ['_self', '_blank'], 'force_enum_field': True, '$description': 'translations.json#/div_action_target', 'platforms': ['web'], 'code_generation_disabled_swift': True}}, 'required': ['log_id']}], '$schema': 'http://json-schema.org/draft-07/schema'}, 'minItems': 1, '$description': 'translations.json#/div_focus_on_focus'}, rule='minItems')
    for data__onfocus_x, data__onfocus_item in enumerate(data__onfocus):
     validate_div_action_json(data__onfocus_item, custom_formats, (name_prefix or "data") + ".on_focus[{data__onfocus_x}]".format(**locals()))
  if "on_blur" in data_keys:
   data_keys.remove("on_blur")
   data__onblur = data["on_blur"]
   if not isinstance(data__onblur, (list, tuple)):
    if not (isinstance(data__onblur, str) and '@' in data__onblur):
     raise JsonSchemaValueException("" + (name_prefix or "data") + ".on_blur must be array", value=data__onblur, name="" + (name_prefix or "data") + ".on_blur", definition={'type': 'array', 'items': {'definitions': {'menu_item': {'type': 'object', 'properties': {'text': {'$ref': 'common.json#/non_empty_string', '$description': 'translations.json#/div_action_menu_item_text'}, 'action': {'$ref': 'div-action.json', '$description': 'translations.json#/div_action_menu_item_action'}, 'actions': {'type': 'array', 'items': {'$ref': 'div-action.json'}, 'minItems': 1, '$description': 'translations.json#/div_action_menu_item_actions'}}, 'required': ['text']}}, 'allOf': [{'$ref': 'div-action-base.json'}, {'type': 'object', '$description': 'translations.json#/div_action', 'properties': {'menu_items': {'type': 'array', 'items': {'$ref': '#/definitions/menu_item'}, '$description': 'translations.json#/div_action_menu_items', 'platforms': ['android', 'ios']}, 'log_url': {'$ref': 'common.json#/url', '$description': 'translations.json#/div_action_log_url'}, 'target': {'type': 'string', 'enum': ['_self', '_blank'], 'force_enum_field': True, '$description': 'translations.json#/div_action_target', 'platforms': ['web'], 'code_generation_disabled_swift': True}}, 'required': ['log_id']}], '$schema': 'http://json-schema.org/draft-07/schema'}, 'minItems': 1, '$description': 'translations.json#/div_focus_on_blur'}, rule='type')
   data__onblur_is_list = isinstance(data__onblur, (list, tuple))
   if data__onblur_is_list:
    data__onblur_len = len(data__onblur)
    if data__onblur_len < 1:
     if not (isinstance(data__onblur, str) and '@' in data__onblur):
      raise JsonSchemaValueException("" + (name_prefix or "data") + ".on_blur must contain at least 1 items", value=data__onblur, name="" + (name_prefix or "data") + ".on_blur", definition={'type': 'array', 'items': {'definitions': {'menu_item': {'type': 'object', 'properties': {'text': {'$ref': 'common.json#/non_empty_string', '$description': 'translations.json#/div_action_menu_item_text'}, 'action': {'$ref': 'div-action.json', '$description': 'translations.json#/div_action_menu_item_action'}, 'actions': {'type': 'array', 'items': {'$ref': 'div-action.json'}, 'minItems': 1, '$description': 'translations.json#/div_action_menu_item_actions'}}, 'required': ['text']}}, 'allOf': [{'$ref': 'div-action-base.json'}, {'type': 'object', '$description': 'translations.json#/div_action', 'properties': {'menu_items': {'type': 'array', 'items': {'$ref': '#/definitions/menu_item'}, '$description': 'translations.json#/div_action_menu_items', 'platforms': ['android', 'ios']}, 'log_url': {'$ref': 'common.json#/url', '$description': 'translations.json#/div_action_log_url'}, 'target': {'type': 'string', 'enum': ['_self', '_blank'], 'force_enum_field': True, '$description': 'translations.json#/div_action_target', 'platforms': ['web'], 'code_generation_disabled_swift': True}}, 'required': ['log_id']}], '$schema': 'http://json-schema.org/draft-07/schema'}, 'minItems': 1, '$description': 'translations.json#/div_focus_on_blur'}, rule='minItems')
    for data__onblur_x, data__onblur_item in enumerate(data__onblur):
     validate_div_action_json(data__onblur_item, custom_formats, (name_prefix or "data") + ".on_blur[{data__onblur_x}]".format(**locals()))
  if "next_focus_ids" in data_keys:
   data_keys.remove("next_focus_ids")
   data__nextfocusids = data["next_focus_ids"]
   if not isinstance(data__nextfocusids, (dict)):
    if not (isinstance(data__nextfocusids, str) and '@' in data__nextfocusids):
     raise JsonSchemaValueException("" + (name_prefix or "data") + ".next_focus_ids must be object", value=data__nextfocusids, name="" + (name_prefix or "data") + ".next_focus_ids", definition={'type': 'object', '$description': 'translations.json#/div_focus_next_focus_ids', 'properties': {'forward': {'type': 'string', 'minLength': 1, 'clientMinLength': 1}, 'right': {'type': 'string', 'minLength': 1, 'clientMinLength': 1}, 'down': {'type': 'string', 'minLength': 1, 'clientMinLength': 1}, 'left': {'type': 'string', 'minLength': 1, 'clientMinLength': 1}, 'up': {'type': 'string', 'minLength': 1, 'clientMinLength': 1}}, 'platforms': ['android', 'ios']}, rule='type')
   data__nextfocusids_is_dict = isinstance(data__nextfocusids, dict)
   if data__nextfocusids_is_dict:
    data__nextfocusids_keys = set(data__nextfocusids.keys())
    if "forward" in data__nextfocusids_keys:
     data__nextfocusids_keys.remove("forward")
     data__nextfocusids__forward = data__nextfocusids["forward"]
     validate_common_json__non_empty_string(data__nextfocusids__forward, custom_formats, (name_prefix or "data") + ".next_focus_ids.forward")
    if "right" in data__nextfocusids_keys:
     data__nextfocusids_keys.remove("right")
     data__nextfocusids__right = data__nextfocusids["right"]
     validate_common_json__non_empty_string(data__nextfocusids__right, custom_formats, (name_prefix or "data") + ".next_focus_ids.right")
    if "down" in data__nextfocusids_keys:
     data__nextfocusids_keys.remove("down")
     data__nextfocusids__down = data__nextfocusids["down"]
     validate_common_json__non_empty_string(data__nextfocusids__down, custom_formats, (name_prefix or "data") + ".next_focus_ids.down")
    if "left" in data__nextfocusids_keys:
     data__nextfocusids_keys.remove("left")
     data__nextfocusids__left = data__nextfocusids["left"]
     validate_common_json__non_empty_string(data__nextfocusids__left, custom_formats, (name_prefix or "data") + ".next_focus_ids.left")
    if "up" in data__nextfocusids_keys:
     data__nextfocusids_keys.remove("up")
     data__nextfocusids__up = data__nextfocusids["up"]
     validate_common_json__non_empty_string(data__nextfocusids__up, custom_formats, (name_prefix or "data") + ".next_focus_ids.up")
 return data

def validate_div_change_transition_json(data, custom_formats={}, name_prefix=None):
 data_any_of_count7 = 0
 if not data_any_of_count7:
  try:
   validate_div_change_set_transition_json(data, custom_formats, (name_prefix or "data") + "")
   data_any_of_count7 += 1
  except JsonSchemaValueException: pass
 if not data_any_of_count7:
  try:
   validate_div_change_bounds_transition_json(data, custom_formats, (name_prefix or "data") + "")
   data_any_of_count7 += 1
  except JsonSchemaValueException: pass
 if not data_any_of_count7:
  if not (isinstance(data, str) and '@' in data):
   raise JsonSchemaValueException("" + (name_prefix or "data") + " cannot be validated by any definition", value=data, name="" + (name_prefix or "data") + "", definition={'$description': 'translations.json#/div_change_transition', 'anyOf': [{'type': 'object', '$description': 'translations.json#/div_change_set_transition', 'properties': {'type': {'type': 'string', 'enum': ['set']}, 'items': {'type': 'array', 'items': {'$ref': 'div-change-transition.json'}, 'minItems': 1, '$description': 'translations.json#/div_change_set_transition_items'}}, 'required': ['type', 'items'], '$schema': 'http://json-schema.org/draft-07/schema'}, {'$description': 'translations.json#/div_change_bounds_transition', 'allOf': [{'$ref': 'div-transition-base.json'}, {'properties': {'type': {'type': 'string', 'enum': ['change_bounds']}}}], 'required': ['type'], '$schema': 'http://json-schema.org/draft-07/schema'}], '$schema': 'http://json-schema.org/draft-07/schema'}, rule='anyOf')
 return data

def validate_div_change_bounds_transition_json(data, custom_formats={}, name_prefix=None):
 validate_div_transition_base_json(data, custom_formats, (name_prefix or "data") + "")
 data_is_dict = isinstance(data, dict)
 if data_is_dict:
  data_keys = set(data.keys())
  if "type" in data_keys:
   data_keys.remove("type")
   data__type = data["type"]
   if not isinstance(data__type, (str)):
    if not (isinstance(data__type, str) and '@' in data__type):
     raise JsonSchemaValueException("" + (name_prefix or "data") + ".type must be string", value=data__type, name="" + (name_prefix or "data") + ".type", definition={'type': 'string', 'enum': ['change_bounds']}, rule='type')
   if data__type not in ['change_bounds']:
    if not (isinstance(data__type, str) and '@' in data__type):
     raise JsonSchemaValueException("" + (name_prefix or "data") + ".type must be one of ['change_bounds']", value=data__type, name="" + (name_prefix or "data") + ".type", definition={'type': 'string', 'enum': ['change_bounds']}, rule='enum')
 data_is_dict = isinstance(data, dict)
 if data_is_dict:
  data__missing_keys = set(['type']) - data.keys()
  if data__missing_keys:
   if not (isinstance(data, str) and '@' in data):
    raise JsonSchemaValueException("" + (name_prefix or "data") + " must contain " + (str(sorted(data__missing_keys)) + " properties"), value=data, name="" + (name_prefix or "data") + "", definition={'$description': 'translations.json#/div_change_bounds_transition', 'allOf': [{'type': 'object', 'protocol_name': 'div-transition-base', 'codegen': {'documentation': {'include_in_toc': True}}, 'properties': {'start_delay': {'$ref': 'common.json#/non_negative_integer', 'default_value': '0', '$description': 'translations.json#/div_transition_base_start_delay'}, 'duration': {'$ref': 'common.json#/non_negative_integer', 'default_value': '200', '$description': 'translations.json#/div_transition_base_duration'}, 'interpolator': {'$ref': 'div-animation-interpolator.json', 'default_value': 'ease_in_out', '$description': 'translations.json#/div_transition_base_interpolator'}}, '$schema': 'http://json-schema.org/draft-07/schema'}, {'properties': {'type': {'type': 'string', 'enum': ['change_bounds']}}}], 'required': ['type'], '$schema': 'http://json-schema.org/draft-07/schema'}, rule='required')
 return data

def validate_div_transition_base_json(data, custom_formats={}, name_prefix=None):
 if not isinstance(data, (dict)):
  if not (isinstance(data, str) and '@' in data):
   raise JsonSchemaValueException("" + (name_prefix or "data") + " must be object", value=data, name="" + (name_prefix or "data") + "", definition={'type': 'object', 'protocol_name': 'div-transition-base', 'codegen': {'documentation': {'include_in_toc': True}}, 'properties': {'start_delay': {'type': 'integer', 'constraint': 'number >= 0'}, 'duration': {'type': 'integer', 'constraint': 'number >= 0'}, 'interpolator': {'type': 'string', 'enum': ['linear', 'ease', 'ease_in', 'ease_out', 'ease_in_out', 'spring'], '$description': 'translations.json#/div_animation_interpolator', '$schema': 'http://json-schema.org/draft-07/schema'}}, '$schema': 'http://json-schema.org/draft-07/schema'}, rule='type')
 data_is_dict = isinstance(data, dict)
 if data_is_dict:
  data_keys = set(data.keys())
  if "start_delay" in data_keys:
   data_keys.remove("start_delay")
   data__startdelay = data["start_delay"]
   validate_common_json__non_negative_integer(data__startdelay, custom_formats, (name_prefix or "data") + ".start_delay")
  if "duration" in data_keys:
   data_keys.remove("duration")
   data__duration = data["duration"]
   validate_common_json__non_negative_integer(data__duration, custom_formats, (name_prefix or "data") + ".duration")
  if "interpolator" in data_keys:
   data_keys.remove("interpolator")
   data__interpolator = data["interpolator"]
   validate_div_animation_interpolator_json(data__interpolator, custom_formats, (name_prefix or "data") + ".interpolator")
 return data

def validate_div_animation_interpolator_json(data, custom_formats={}, name_prefix=None):
 if not isinstance(data, (str)):
  if not (isinstance(data, str) and '@' in data):
   raise JsonSchemaValueException("" + (name_prefix or "data") + " must be string", value=data, name="" + (name_prefix or "data") + "", definition={'type': 'string', 'enum': ['linear', 'ease', 'ease_in', 'ease_out', 'ease_in_out', 'spring'], '$description': 'translations.json#/div_animation_interpolator', '$schema': 'http://json-schema.org/draft-07/schema'}, rule='type')
 if data not in ['linear', 'ease', 'ease_in', 'ease_out', 'ease_in_out', 'spring']:
  if not (isinstance(data, str) and '@' in data):
   raise JsonSchemaValueException("" + (name_prefix or "data") + " must be one of ['linear', 'ease', 'ease_in', 'ease_out', 'ease_in_out', 'spring']", value=data, name="" + (name_prefix or "data") + "", definition={'type': 'string', 'enum': ['linear', 'ease', 'ease_in', 'ease_out', 'ease_in_out', 'spring'], '$description': 'translations.json#/div_animation_interpolator', '$schema': 'http://json-schema.org/draft-07/schema'}, rule='enum')
 return data

def validate_div_change_set_transition_json(data, custom_formats={}, name_prefix=None):
 if not isinstance(data, (dict)):
  if not (isinstance(data, str) and '@' in data):
   raise JsonSchemaValueException("" + (name_prefix or "data") + " must be object", value=data, name="" + (name_prefix or "data") + "", definition={'type': 'object', '$description': 'translations.json#/div_change_set_transition', 'properties': {'type': {'type': 'string', 'enum': ['set']}, 'items': {'type': 'array', 'items': {'$description': 'translations.json#/div_change_transition', 'anyOf': [{'$ref': 'div-change-set-transition.json', '$description': 'translations.json#/div_change_transition_set'}, {'$ref': 'div-change-bounds-transition.json', '$description': 'translations.json#/div_change_transition_bounds'}], '$schema': 'http://json-schema.org/draft-07/schema'}, 'minItems': 1, '$description': 'translations.json#/div_change_set_transition_items'}}, 'required': ['type', 'items'], '$schema': 'http://json-schema.org/draft-07/schema'}, rule='type')
 data_is_dict = isinstance(data, dict)
 if data_is_dict:
  data__missing_keys = set(['type', 'items']) - data.keys()
  if data__missing_keys:
   if not (isinstance(data, str) and '@' in data):
    raise JsonSchemaValueException("" + (name_prefix or "data") + " must contain " + (str(sorted(data__missing_keys)) + " properties"), value=data, name="" + (name_prefix or "data") + "", definition={'type': 'object', '$description': 'translations.json#/div_change_set_transition', 'properties': {'type': {'type': 'string', 'enum': ['set']}, 'items': {'type': 'array', 'items': {'$description': 'translations.json#/div_change_transition', 'anyOf': [{'$ref': 'div-change-set-transition.json', '$description': 'translations.json#/div_change_transition_set'}, {'$ref': 'div-change-bounds-transition.json', '$description': 'translations.json#/div_change_transition_bounds'}], '$schema': 'http://json-schema.org/draft-07/schema'}, 'minItems': 1, '$description': 'translations.json#/div_change_set_transition_items'}}, 'required': ['type', 'items'], '$schema': 'http://json-schema.org/draft-07/schema'}, rule='required')
  data_keys = set(data.keys())
  if "type" in data_keys:
   data_keys.remove("type")
   data__type = data["type"]
   if not isinstance(data__type, (str)):
    if not (isinstance(data__type, str) and '@' in data__type):
     raise JsonSchemaValueException("" + (name_prefix or "data") + ".type must be string", value=data__type, name="" + (name_prefix or "data") + ".type", definition={'type': 'string', 'enum': ['set']}, rule='type')
   if data__type not in ['set']:
    if not (isinstance(data__type, str) and '@' in data__type):
     raise JsonSchemaValueException("" + (name_prefix or "data") + ".type must be one of ['set']", value=data__type, name="" + (name_prefix or "data") + ".type", definition={'type': 'string', 'enum': ['set']}, rule='enum')
  if "items" in data_keys:
   data_keys.remove("items")
   data__items = data["items"]
   if not isinstance(data__items, (list, tuple)):
    if not (isinstance(data__items, str) and '@' in data__items):
     raise JsonSchemaValueException("" + (name_prefix or "data") + ".items must be array", value=data__items, name="" + (name_prefix or "data") + ".items", definition={'type': 'array', 'items': {'$description': 'translations.json#/div_change_transition', 'anyOf': [{'$ref': 'div-change-set-transition.json', '$description': 'translations.json#/div_change_transition_set'}, {'$ref': 'div-change-bounds-transition.json', '$description': 'translations.json#/div_change_transition_bounds'}], '$schema': 'http://json-schema.org/draft-07/schema'}, 'minItems': 1, '$description': 'translations.json#/div_change_set_transition_items'}, rule='type')
   data__items_is_list = isinstance(data__items, (list, tuple))
   if data__items_is_list:
    data__items_len = len(data__items)
    if data__items_len < 1:
     if not (isinstance(data__items, str) and '@' in data__items):
      raise JsonSchemaValueException("" + (name_prefix or "data") + ".items must contain at least 1 items", value=data__items, name="" + (name_prefix or "data") + ".items", definition={'type': 'array', 'items': {'$description': 'translations.json#/div_change_transition', 'anyOf': [{'$ref': 'div-change-set-transition.json', '$description': 'translations.json#/div_change_transition_set'}, {'$ref': 'div-change-bounds-transition.json', '$description': 'translations.json#/div_change_transition_bounds'}], '$schema': 'http://json-schema.org/draft-07/schema'}, 'minItems': 1, '$description': 'translations.json#/div_change_set_transition_items'}, rule='minItems')
    for data__items_x, data__items_item in enumerate(data__items):
     validate_div_change_transition_json(data__items_item, custom_formats, (name_prefix or "data") + ".items[{data__items_x}]".format(**locals()))
 return data

def validate_div_appearance_transition_json(data, custom_formats={}, name_prefix=None):
 data_any_of_count8 = 0
 if not data_any_of_count8:
  try:
   validate_div_appearance_set_transition_json(data, custom_formats, (name_prefix or "data") + "")
   data_any_of_count8 += 1
  except JsonSchemaValueException: pass
 if not data_any_of_count8:
  try:
   validate_div_fade_transition_json(data, custom_formats, (name_prefix or "data") + "")
   data_any_of_count8 += 1
  except JsonSchemaValueException: pass
 if not data_any_of_count8:
  try:
   validate_div_scale_transition_json(data, custom_formats, (name_prefix or "data") + "")
   data_any_of_count8 += 1
  except JsonSchemaValueException: pass
 if not data_any_of_count8:
  try:
   validate_div_slide_transition_json(data, custom_formats, (name_prefix or "data") + "")
   data_any_of_count8 += 1
  except JsonSchemaValueException: pass
 if not data_any_of_count8:
  if not (isinstance(data, str) and '@' in data):
   raise JsonSchemaValueException("" + (name_prefix or "data") + " cannot be validated by any definition", value=data, name="" + (name_prefix or "data") + "", definition={'$description': 'translations.json#/div_appearance_transition', 'anyOf': [{'type': 'object', '$description': 'translations.json#/div_appearance_set_transition', 'properties': {'type': {'type': 'string', 'enum': ['set']}, 'items': {'type': 'array', 'items': {'$ref': 'div-appearance-transition.json'}, 'minItems': 1, '$description': 'translations.json#/div_appearance_set_transition_items'}}, 'required': ['type', 'items'], '$schema': 'http://json-schema.org/draft-07/schema'}, {'$description': 'translations.json#/div_fade_transition', 'allOf': [{'$ref': 'div-transition-base.json'}, {'properties': {'type': {'type': 'string', 'enum': ['fade']}, 'alpha': {'type': 'number', 'constraint': 'number >= 0.0 && number <= 1.0', 'default_value': '0.0', '$description': 'translations.json#/div_fade_transition_alpha'}}}], 'required': ['type'], '$schema': 'http://json-schema.org/draft-07/schema'}, {'$description': 'translations.json#/div_scale_transition', 'allOf': [{'$ref': 'div-transition-base.json'}, {'properties': {'type': {'type': 'string', 'enum': ['scale']}, 'scale': {'type': 'number', 'constraint': 'number >= 0.0', 'default_value': '0.0', '$description': 'translations.json#/div_scale_transition_scale'}, 'pivot_x': {'type': 'number', 'constraint': 'number >= 0.0 && number <= 1.0', 'default_value': '0.5', '$description': 'translations.json#/div_scale_transition_pivot_x'}, 'pivot_y': {'type': 'number', 'constraint': 'number >= 0.0 && number <= 1.0', 'default_value': '0.5', '$description': 'translations.json#/div_scale_transition_pivot_y'}}}], 'required': ['type'], '$schema': 'http://json-schema.org/draft-07/schema'}, {'$description': 'translations.json#/div_slide_transition', 'allOf': [{'$ref': 'div-transition-base.json'}, {'properties': {'type': {'type': 'string', 'enum': ['slide']}, 'edge': {'type': 'string', 'enum': ['left', 'top', 'right', 'bottom'], 'default_value': 'bottom', '$description': 'translations.json#/div_slide_transition_edge'}, 'distance': {'$ref': 'div-dimension.json', '$description': 'translations.json#/div_slide_transition_distance'}}}], 'required': ['type'], '$schema': 'http://json-schema.org/draft-07/schema'}], '$schema': 'http://json-schema.org/draft-07/schema'}, rule='anyOf')
 return data

def validate_div_slide_transition_json(data, custom_formats={}, name_prefix=None):
 validate_div_transition_base_json(data, custom_formats, (name_prefix or "data") + "")
 data_is_dict = isinstance(data, dict)
 if data_is_dict:
  data_keys = set(data.keys())
  if "type" in data_keys:
   data_keys.remove("type")
   data__type = data["type"]
   if not isinstance(data__type, (str)):
    if not (isinstance(data__type, str) and '@' in data__type):
     raise JsonSchemaValueException("" + (name_prefix or "data") + ".type must be string", value=data__type, name="" + (name_prefix or "data") + ".type", definition={'type': 'string', 'enum': ['slide']}, rule='type')
   if data__type not in ['slide']:
    if not (isinstance(data__type, str) and '@' in data__type):
     raise JsonSchemaValueException("" + (name_prefix or "data") + ".type must be one of ['slide']", value=data__type, name="" + (name_prefix or "data") + ".type", definition={'type': 'string', 'enum': ['slide']}, rule='enum')
  if "edge" in data_keys:
   data_keys.remove("edge")
   data__edge = data["edge"]
   if not isinstance(data__edge, (str)):
    if not (isinstance(data__edge, str) and '@' in data__edge):
     raise JsonSchemaValueException("" + (name_prefix or "data") + ".edge must be string", value=data__edge, name="" + (name_prefix or "data") + ".edge", definition={'type': 'string', 'enum': ['left', 'top', 'right', 'bottom'], 'default_value': 'bottom', '$description': 'translations.json#/div_slide_transition_edge'}, rule='type')
   if data__edge not in ['left', 'top', 'right', 'bottom']:
    if not (isinstance(data__edge, str) and '@' in data__edge):
     raise JsonSchemaValueException("" + (name_prefix or "data") + ".edge must be one of ['left', 'top', 'right', 'bottom']", value=data__edge, name="" + (name_prefix or "data") + ".edge", definition={'type': 'string', 'enum': ['left', 'top', 'right', 'bottom'], 'default_value': 'bottom', '$description': 'translations.json#/div_slide_transition_edge'}, rule='enum')
  if "distance" in data_keys:
   data_keys.remove("distance")
   data__distance = data["distance"]
   validate_div_dimension_json(data__distance, custom_formats, (name_prefix or "data") + ".distance")
 data_is_dict = isinstance(data, dict)
 if data_is_dict:
  data__missing_keys = set(['type']) - data.keys()
  if data__missing_keys:
   if not (isinstance(data, str) and '@' in data):
    raise JsonSchemaValueException("" + (name_prefix or "data") + " must contain " + (str(sorted(data__missing_keys)) + " properties"), value=data, name="" + (name_prefix or "data") + "", definition={'$description': 'translations.json#/div_slide_transition', 'allOf': [{'type': 'object', 'protocol_name': 'div-transition-base', 'codegen': {'documentation': {'include_in_toc': True}}, 'properties': {'start_delay': {'$ref': 'common.json#/non_negative_integer', 'default_value': '0', '$description': 'translations.json#/div_transition_base_start_delay'}, 'duration': {'$ref': 'common.json#/non_negative_integer', 'default_value': '200', '$description': 'translations.json#/div_transition_base_duration'}, 'interpolator': {'$ref': 'div-animation-interpolator.json', 'default_value': 'ease_in_out', '$description': 'translations.json#/div_transition_base_interpolator'}}, '$schema': 'http://json-schema.org/draft-07/schema'}, {'properties': {'type': {'type': 'string', 'enum': ['slide']}, 'edge': {'type': 'string', 'enum': ['left', 'top', 'right', 'bottom'], 'default_value': 'bottom', '$description': 'translations.json#/div_slide_transition_edge'}, 'distance': {'type': 'object', '$description': 'translations.json#/div_dimension', 'codegen': {'divan': {'forced_properties_order': ['value']}}, 'properties': {'value': {'type': 'number', '$description': 'translations.json#/div_dimension_value'}, 'unit': {'$ref': 'div-size-unit.json', 'default_value': 'dp'}}, 'required': ['value'], '$schema': 'http://json-schema.org/draft-07/schema'}}}], 'required': ['type'], '$schema': 'http://json-schema.org/draft-07/schema'}, rule='required')
 return data

def validate_div_dimension_json(data, custom_formats={}, name_prefix=None):
 if not isinstance(data, (dict)):
  if not (isinstance(data, str) and '@' in data):
   raise JsonSchemaValueException("" + (name_prefix or "data") + " must be object", value=data, name="" + (name_prefix or "data") + "", definition={'type': 'object', '$description': 'translations.json#/div_dimension', 'codegen': {'divan': {'forced_properties_order': ['value']}}, 'properties': {'value': {'type': 'number', '$description': 'translations.json#/div_dimension_value'}, 'unit': {'type': 'string', 'enum': ['dp', 'sp', 'px'], '$description': 'translations.json#/div_size_unit', 'platforms': ['android', 'ios'], '$schema': 'http://json-schema.org/draft-07/schema'}}, 'required': ['value'], '$schema': 'http://json-schema.org/draft-07/schema'}, rule='type')
 data_is_dict = isinstance(data, dict)
 if data_is_dict:
  data__missing_keys = set(['value']) - data.keys()
  if data__missing_keys:
   if not (isinstance(data, str) and '@' in data):
    raise JsonSchemaValueException("" + (name_prefix or "data") + " must contain " + (str(sorted(data__missing_keys)) + " properties"), value=data, name="" + (name_prefix or "data") + "", definition={'type': 'object', '$description': 'translations.json#/div_dimension', 'codegen': {'divan': {'forced_properties_order': ['value']}}, 'properties': {'value': {'type': 'number', '$description': 'translations.json#/div_dimension_value'}, 'unit': {'type': 'string', 'enum': ['dp', 'sp', 'px'], '$description': 'translations.json#/div_size_unit', 'platforms': ['android', 'ios'], '$schema': 'http://json-schema.org/draft-07/schema'}}, 'required': ['value'], '$schema': 'http://json-schema.org/draft-07/schema'}, rule='required')
  data_keys = set(data.keys())
  if "value" in data_keys:
   data_keys.remove("value")
   data__value = data["value"]
   if not isinstance(data__value, (int, float, Decimal)) or isinstance(data__value, bool):
    if not (isinstance(data__value, str) and '@' in data__value):
     raise JsonSchemaValueException("" + (name_prefix or "data") + ".value must be number", value=data__value, name="" + (name_prefix or "data") + ".value", definition={'type': 'number', '$description': 'translations.json#/div_dimension_value'}, rule='type')
  if "unit" in data_keys:
   data_keys.remove("unit")
   data__unit = data["unit"]
   validate_div_size_unit_json(data__unit, custom_formats, (name_prefix or "data") + ".unit")
 return data

def validate_div_scale_transition_json(data, custom_formats={}, name_prefix=None):
 validate_div_transition_base_json(data, custom_formats, (name_prefix or "data") + "")
 data_is_dict = isinstance(data, dict)
 if data_is_dict:
  data_keys = set(data.keys())
  if "type" in data_keys:
   data_keys.remove("type")
   data__type = data["type"]
   if not isinstance(data__type, (str)):
    if not (isinstance(data__type, str) and '@' in data__type):
     raise JsonSchemaValueException("" + (name_prefix or "data") + ".type must be string", value=data__type, name="" + (name_prefix or "data") + ".type", definition={'type': 'string', 'enum': ['scale']}, rule='type')
   if data__type not in ['scale']:
    if not (isinstance(data__type, str) and '@' in data__type):
     raise JsonSchemaValueException("" + (name_prefix or "data") + ".type must be one of ['scale']", value=data__type, name="" + (name_prefix or "data") + ".type", definition={'type': 'string', 'enum': ['scale']}, rule='enum')
  if "scale" in data_keys:
   data_keys.remove("scale")
   data__scale = data["scale"]
   if not isinstance(data__scale, (int, float, Decimal)) or isinstance(data__scale, bool):
    if not (isinstance(data__scale, str) and '@' in data__scale):
     raise JsonSchemaValueException("" + (name_prefix or "data") + ".scale must be number", value=data__scale, name="" + (name_prefix or "data") + ".scale", definition={'type': 'number', 'constraint': 'number >= 0.0', 'default_value': '0.0', '$description': 'translations.json#/div_scale_transition_scale'}, rule='type')
  if "pivot_x" in data_keys:
   data_keys.remove("pivot_x")
   data__pivotx = data["pivot_x"]
   if not isinstance(data__pivotx, (int, float, Decimal)) or isinstance(data__pivotx, bool):
    if not (isinstance(data__pivotx, str) and '@' in data__pivotx):
     raise JsonSchemaValueException("" + (name_prefix or "data") + ".pivot_x must be number", value=data__pivotx, name="" + (name_prefix or "data") + ".pivot_x", definition={'type': 'number', 'constraint': 'number >= 0.0 && number <= 1.0', 'default_value': '0.5', '$description': 'translations.json#/div_scale_transition_pivot_x'}, rule='type')
  if "pivot_y" in data_keys:
   data_keys.remove("pivot_y")
   data__pivoty = data["pivot_y"]
   if not isinstance(data__pivoty, (int, float, Decimal)) or isinstance(data__pivoty, bool):
    if not (isinstance(data__pivoty, str) and '@' in data__pivoty):
     raise JsonSchemaValueException("" + (name_prefix or "data") + ".pivot_y must be number", value=data__pivoty, name="" + (name_prefix or "data") + ".pivot_y", definition={'type': 'number', 'constraint': 'number >= 0.0 && number <= 1.0', 'default_value': '0.5', '$description': 'translations.json#/div_scale_transition_pivot_y'}, rule='type')
 data_is_dict = isinstance(data, dict)
 if data_is_dict:
  data__missing_keys = set(['type']) - data.keys()
  if data__missing_keys:
   if not (isinstance(data, str) and '@' in data):
    raise JsonSchemaValueException("" + (name_prefix or "data") + " must contain " + (str(sorted(data__missing_keys)) + " properties"), value=data, name="" + (name_prefix or "data") + "", definition={'$description': 'translations.json#/div_scale_transition', 'allOf': [{'type': 'object', 'protocol_name': 'div-transition-base', 'codegen': {'documentation': {'include_in_toc': True}}, 'properties': {'start_delay': {'$ref': 'common.json#/non_negative_integer', 'default_value': '0', '$description': 'translations.json#/div_transition_base_start_delay'}, 'duration': {'$ref': 'common.json#/non_negative_integer', 'default_value': '200', '$description': 'translations.json#/div_transition_base_duration'}, 'interpolator': {'$ref': 'div-animation-interpolator.json', 'default_value': 'ease_in_out', '$description': 'translations.json#/div_transition_base_interpolator'}}, '$schema': 'http://json-schema.org/draft-07/schema'}, {'properties': {'type': {'type': 'string', 'enum': ['scale']}, 'scale': {'type': 'number', 'constraint': 'number >= 0.0', 'default_value': '0.0', '$description': 'translations.json#/div_scale_transition_scale'}, 'pivot_x': {'type': 'number', 'constraint': 'number >= 0.0 && number <= 1.0', 'default_value': '0.5', '$description': 'translations.json#/div_scale_transition_pivot_x'}, 'pivot_y': {'type': 'number', 'constraint': 'number >= 0.0 && number <= 1.0', 'default_value': '0.5', '$description': 'translations.json#/div_scale_transition_pivot_y'}}}], 'required': ['type'], '$schema': 'http://json-schema.org/draft-07/schema'}, rule='required')
 return data

def validate_div_fade_transition_json(data, custom_formats={}, name_prefix=None):
 validate_div_transition_base_json(data, custom_formats, (name_prefix or "data") + "")
 data_is_dict = isinstance(data, dict)
 if data_is_dict:
  data_keys = set(data.keys())
  if "type" in data_keys:
   data_keys.remove("type")
   data__type = data["type"]
   if not isinstance(data__type, (str)):
    if not (isinstance(data__type, str) and '@' in data__type):
     raise JsonSchemaValueException("" + (name_prefix or "data") + ".type must be string", value=data__type, name="" + (name_prefix or "data") + ".type", definition={'type': 'string', 'enum': ['fade']}, rule='type')
   if data__type not in ['fade']:
    if not (isinstance(data__type, str) and '@' in data__type):
     raise JsonSchemaValueException("" + (name_prefix or "data") + ".type must be one of ['fade']", value=data__type, name="" + (name_prefix or "data") + ".type", definition={'type': 'string', 'enum': ['fade']}, rule='enum')
  if "alpha" in data_keys:
   data_keys.remove("alpha")
   data__alpha = data["alpha"]
   if not isinstance(data__alpha, (int, float, Decimal)) or isinstance(data__alpha, bool):
    if not (isinstance(data__alpha, str) and '@' in data__alpha):
     raise JsonSchemaValueException("" + (name_prefix or "data") + ".alpha must be number", value=data__alpha, name="" + (name_prefix or "data") + ".alpha", definition={'type': 'number', 'constraint': 'number >= 0.0 && number <= 1.0', 'default_value': '0.0', '$description': 'translations.json#/div_fade_transition_alpha'}, rule='type')
 data_is_dict = isinstance(data, dict)
 if data_is_dict:
  data__missing_keys = set(['type']) - data.keys()
  if data__missing_keys:
   if not (isinstance(data, str) and '@' in data):
    raise JsonSchemaValueException("" + (name_prefix or "data") + " must contain " + (str(sorted(data__missing_keys)) + " properties"), value=data, name="" + (name_prefix or "data") + "", definition={'$description': 'translations.json#/div_fade_transition', 'allOf': [{'type': 'object', 'protocol_name': 'div-transition-base', 'codegen': {'documentation': {'include_in_toc': True}}, 'properties': {'start_delay': {'$ref': 'common.json#/non_negative_integer', 'default_value': '0', '$description': 'translations.json#/div_transition_base_start_delay'}, 'duration': {'$ref': 'common.json#/non_negative_integer', 'default_value': '200', '$description': 'translations.json#/div_transition_base_duration'}, 'interpolator': {'$ref': 'div-animation-interpolator.json', 'default_value': 'ease_in_out', '$description': 'translations.json#/div_transition_base_interpolator'}}, '$schema': 'http://json-schema.org/draft-07/schema'}, {'properties': {'type': {'type': 'string', 'enum': ['fade']}, 'alpha': {'type': 'number', 'constraint': 'number >= 0.0 && number <= 1.0', 'default_value': '0.0', '$description': 'translations.json#/div_fade_transition_alpha'}}}], 'required': ['type'], '$schema': 'http://json-schema.org/draft-07/schema'}, rule='required')
 return data

def validate_div_appearance_set_transition_json(data, custom_formats={}, name_prefix=None):
 if not isinstance(data, (dict)):
  if not (isinstance(data, str) and '@' in data):
   raise JsonSchemaValueException("" + (name_prefix or "data") + " must be object", value=data, name="" + (name_prefix or "data") + "", definition={'type': 'object', '$description': 'translations.json#/div_appearance_set_transition', 'properties': {'type': {'type': 'string', 'enum': ['set']}, 'items': {'type': 'array', 'items': {'$description': 'translations.json#/div_appearance_transition', 'anyOf': [{'$ref': 'div-appearance-set-transition.json', '$description': 'translations.json#/div_appearance_transition_set'}, {'$ref': 'div-fade-transition.json', '$description': 'translations.json#/div_appearance_transition_fade'}, {'$ref': 'div-scale-transition.json', '$description': 'translations.json#/div_appearance_transition_scale'}, {'$ref': 'div-slide-transition.json', '$description': 'translations.json#/div_appearance_transition_slide'}], '$schema': 'http://json-schema.org/draft-07/schema'}, 'minItems': 1, '$description': 'translations.json#/div_appearance_set_transition_items'}}, 'required': ['type', 'items'], '$schema': 'http://json-schema.org/draft-07/schema'}, rule='type')
 data_is_dict = isinstance(data, dict)
 if data_is_dict:
  data__missing_keys = set(['type', 'items']) - data.keys()
  if data__missing_keys:
   if not (isinstance(data, str) and '@' in data):
    raise JsonSchemaValueException("" + (name_prefix or "data") + " must contain " + (str(sorted(data__missing_keys)) + " properties"), value=data, name="" + (name_prefix or "data") + "", definition={'type': 'object', '$description': 'translations.json#/div_appearance_set_transition', 'properties': {'type': {'type': 'string', 'enum': ['set']}, 'items': {'type': 'array', 'items': {'$description': 'translations.json#/div_appearance_transition', 'anyOf': [{'$ref': 'div-appearance-set-transition.json', '$description': 'translations.json#/div_appearance_transition_set'}, {'$ref': 'div-fade-transition.json', '$description': 'translations.json#/div_appearance_transition_fade'}, {'$ref': 'div-scale-transition.json', '$description': 'translations.json#/div_appearance_transition_scale'}, {'$ref': 'div-slide-transition.json', '$description': 'translations.json#/div_appearance_transition_slide'}], '$schema': 'http://json-schema.org/draft-07/schema'}, 'minItems': 1, '$description': 'translations.json#/div_appearance_set_transition_items'}}, 'required': ['type', 'items'], '$schema': 'http://json-schema.org/draft-07/schema'}, rule='required')
  data_keys = set(data.keys())
  if "type" in data_keys:
   data_keys.remove("type")
   data__type = data["type"]
   if not isinstance(data__type, (str)):
    if not (isinstance(data__type, str) and '@' in data__type):
     raise JsonSchemaValueException("" + (name_prefix or "data") + ".type must be string", value=data__type, name="" + (name_prefix or "data") + ".type", definition={'type': 'string', 'enum': ['set']}, rule='type')
   if data__type not in ['set']:
    if not (isinstance(data__type, str) and '@' in data__type):
     raise JsonSchemaValueException("" + (name_prefix or "data") + ".type must be one of ['set']", value=data__type, name="" + (name_prefix or "data") + ".type", definition={'type': 'string', 'enum': ['set']}, rule='enum')
  if "items" in data_keys:
   data_keys.remove("items")
   data__items = data["items"]
   if not isinstance(data__items, (list, tuple)):
    if not (isinstance(data__items, str) and '@' in data__items):
     raise JsonSchemaValueException("" + (name_prefix or "data") + ".items must be array", value=data__items, name="" + (name_prefix or "data") + ".items", definition={'type': 'array', 'items': {'$description': 'translations.json#/div_appearance_transition', 'anyOf': [{'$ref': 'div-appearance-set-transition.json', '$description': 'translations.json#/div_appearance_transition_set'}, {'$ref': 'div-fade-transition.json', '$description': 'translations.json#/div_appearance_transition_fade'}, {'$ref': 'div-scale-transition.json', '$description': 'translations.json#/div_appearance_transition_scale'}, {'$ref': 'div-slide-transition.json', '$description': 'translations.json#/div_appearance_transition_slide'}], '$schema': 'http://json-schema.org/draft-07/schema'}, 'minItems': 1, '$description': 'translations.json#/div_appearance_set_transition_items'}, rule='type')
   data__items_is_list = isinstance(data__items, (list, tuple))
   if data__items_is_list:
    data__items_len = len(data__items)
    if data__items_len < 1:
     if not (isinstance(data__items, str) and '@' in data__items):
      raise JsonSchemaValueException("" + (name_prefix or "data") + ".items must contain at least 1 items", value=data__items, name="" + (name_prefix or "data") + ".items", definition={'type': 'array', 'items': {'$description': 'translations.json#/div_appearance_transition', 'anyOf': [{'$ref': 'div-appearance-set-transition.json', '$description': 'translations.json#/div_appearance_transition_set'}, {'$ref': 'div-fade-transition.json', '$description': 'translations.json#/div_appearance_transition_fade'}, {'$ref': 'div-scale-transition.json', '$description': 'translations.json#/div_appearance_transition_scale'}, {'$ref': 'div-slide-transition.json', '$description': 'translations.json#/div_appearance_transition_slide'}], '$schema': 'http://json-schema.org/draft-07/schema'}, 'minItems': 1, '$description': 'translations.json#/div_appearance_set_transition_items'}, rule='minItems')
    for data__items_x, data__items_item in enumerate(data__items):
     validate_div_appearance_transition_json(data__items_item, custom_formats, (name_prefix or "data") + ".items[{data__items_x}]".format(**locals()))
 return data

def validate_div_transition_trigger_json(data, custom_formats={}, name_prefix=None):
 if not isinstance(data, (str)):
  if not (isinstance(data, str) and '@' in data):
   raise JsonSchemaValueException("" + (name_prefix or "data") + " must be string", value=data, name="" + (name_prefix or "data") + "", definition={'type': 'string', 'enum': ['data_change', 'state_change', 'visibility_change'], '$description': 'translations.json#/div_transition_trigger', '$schema': 'http://json-schema.org/draft-07/schema'}, rule='type')
 if data not in ['data_change', 'state_change', 'visibility_change']:
  if not (isinstance(data, str) and '@' in data):
   raise JsonSchemaValueException("" + (name_prefix or "data") + " must be one of ['data_change', 'state_change', 'visibility_change']", value=data, name="" + (name_prefix or "data") + "", definition={'type': 'string', 'enum': ['data_change', 'state_change', 'visibility_change'], '$description': 'translations.json#/div_transition_trigger', '$schema': 'http://json-schema.org/draft-07/schema'}, rule='enum')
 return data

def validate_div_extension_json(data, custom_formats={}, name_prefix=None):
 if not isinstance(data, (dict)):
  if not (isinstance(data, str) and '@' in data):
   raise JsonSchemaValueException("" + (name_prefix or "data") + " must be object", value=data, name="" + (name_prefix or "data") + "", definition={'type': 'object', '$description': 'translations.json#/div_extension', 'properties': {'id': {'type': 'string', 'minLength': 1, 'clientMinLength': 1}, 'params': {'type': 'object', 'additionalProperties': True, '$description': 'translations.json#/div_extension_params'}}, 'required': ['id'], '$schema': 'http://json-schema.org/draft-07/schema'}, rule='type')
 data_is_dict = isinstance(data, dict)
 if data_is_dict:
  data__missing_keys = set(['id']) - data.keys()
  if data__missing_keys:
   if not (isinstance(data, str) and '@' in data):
    raise JsonSchemaValueException("" + (name_prefix or "data") + " must contain " + (str(sorted(data__missing_keys)) + " properties"), value=data, name="" + (name_prefix or "data") + "", definition={'type': 'object', '$description': 'translations.json#/div_extension', 'properties': {'id': {'type': 'string', 'minLength': 1, 'clientMinLength': 1}, 'params': {'type': 'object', 'additionalProperties': True, '$description': 'translations.json#/div_extension_params'}}, 'required': ['id'], '$schema': 'http://json-schema.org/draft-07/schema'}, rule='required')
  data_keys = set(data.keys())
  if "id" in data_keys:
   data_keys.remove("id")
   data__id = data["id"]
   validate_common_json__non_empty_string(data__id, custom_formats, (name_prefix or "data") + ".id")
  if "params" in data_keys:
   data_keys.remove("params")
   data__params = data["params"]
   if not isinstance(data__params, (dict)):
    if not (isinstance(data__params, str) and '@' in data__params):
     raise JsonSchemaValueException("" + (name_prefix or "data") + ".params must be object", value=data__params, name="" + (name_prefix or "data") + ".params", definition={'type': 'object', 'additionalProperties': True, '$description': 'translations.json#/div_extension_params'}, rule='type')
   data__params_is_dict = isinstance(data__params, dict)
   if data__params_is_dict:
    data__params_keys = set(data__params.keys())
 return data

def validate_div_accessibility_json(data, custom_formats={}, name_prefix=None):
 if not isinstance(data, (dict)):
  if not (isinstance(data, str) and '@' in data):
   raise JsonSchemaValueException("" + (name_prefix or "data") + " must be object", value=data, name="" + (name_prefix or "data") + "", definition={'type': 'object', '$description': 'translations.json#/div_accessibility', 'properties': {'description': {'type': 'string', 'minLength': 1, 'clientMinLength': 1}, 'type': {'type': 'string', 'enum': ['none', 'button', 'image', 'text', 'edit_text', 'header', 'tab_bar', 'list', 'select'], 'supports_expressions': False, '$description': 'translations.json#/div_accessibility_type', 'platforms': ['android', 'ios']}, 'state_description': {'type': 'string', 'minLength': 1, 'clientMinLength': 1}, 'hint': {'type': 'string', 'minLength': 1, 'clientMinLength': 1}, 'mode': {'type': 'string', 'enum': ['default', 'merge', 'exclude'], 'default_value': 'default', '$description': 'translations.json#/div_accessibility_mode', 'platforms': ['android', 'ios']}, 'mute_after_action': {'oneOf': [{'type': 'boolean'}, {'type': 'integer', 'enum': [0, 1]}]}}, '$schema': 'http://json-schema.org/draft-07/schema'}, rule='type')
 data_is_dict = isinstance(data, dict)
 if data_is_dict:
  data_keys = set(data.keys())
  if "description" in data_keys:
   data_keys.remove("description")
   data__description = data["description"]
   validate_common_json__non_empty_string(data__description, custom_formats, (name_prefix or "data") + ".description")
  if "type" in data_keys:
   data_keys.remove("type")
   data__type = data["type"]
   if not isinstance(data__type, (str)):
    if not (isinstance(data__type, str) and '@' in data__type):
     raise JsonSchemaValueException("" + (name_prefix or "data") + ".type must be string", value=data__type, name="" + (name_prefix or "data") + ".type", definition={'type': 'string', 'enum': ['none', 'button', 'image', 'text', 'edit_text', 'header', 'tab_bar', 'list', 'select'], 'supports_expressions': False, '$description': 'translations.json#/div_accessibility_type', 'platforms': ['android', 'ios']}, rule='type')
   if data__type not in ['none', 'button', 'image', 'text', 'edit_text', 'header', 'tab_bar', 'list', 'select']:
    if not (isinstance(data__type, str) and '@' in data__type):
     raise JsonSchemaValueException("" + (name_prefix or "data") + ".type must be one of ['none', 'button', 'image', 'text', 'edit_text', 'header', 'tab_bar', 'list', 'select']", value=data__type, name="" + (name_prefix or "data") + ".type", definition={'type': 'string', 'enum': ['none', 'button', 'image', 'text', 'edit_text', 'header', 'tab_bar', 'list', 'select'], 'supports_expressions': False, '$description': 'translations.json#/div_accessibility_type', 'platforms': ['android', 'ios']}, rule='enum')
  if "state_description" in data_keys:
   data_keys.remove("state_description")
   data__statedescription = data["state_description"]
   validate_common_json__non_empty_string(data__statedescription, custom_formats, (name_prefix or "data") + ".state_description")
  if "hint" in data_keys:
   data_keys.remove("hint")
   data__hint = data["hint"]
   validate_common_json__non_empty_string(data__hint, custom_formats, (name_prefix or "data") + ".hint")
  if "mode" in data_keys:
   data_keys.remove("mode")
   data__mode = data["mode"]
   if not isinstance(data__mode, (str)):
    if not (isinstance(data__mode, str) and '@' in data__mode):
     raise JsonSchemaValueException("" + (name_prefix or "data") + ".mode must be string", value=data__mode, name="" + (name_prefix or "data") + ".mode", definition={'type': 'string', 'enum': ['default', 'merge', 'exclude'], 'default_value': 'default', '$description': 'translations.json#/div_accessibility_mode', 'platforms': ['android', 'ios']}, rule='type')
   if data__mode not in ['default', 'merge', 'exclude']:
    if not (isinstance(data__mode, str) and '@' in data__mode):
     raise JsonSchemaValueException("" + (name_prefix or "data") + ".mode must be one of ['default', 'merge', 'exclude']", value=data__mode, name="" + (name_prefix or "data") + ".mode", definition={'type': 'string', 'enum': ['default', 'merge', 'exclude'], 'default_value': 'default', '$description': 'translations.json#/div_accessibility_mode', 'platforms': ['android', 'ios']}, rule='enum')
  if "mute_after_action" in data_keys:
   data_keys.remove("mute_after_action")
   data__muteafteraction = data["mute_after_action"]
   validate_common_json__boolean_int(data__muteafteraction, custom_formats, (name_prefix or "data") + ".mute_after_action")
 return data

def validate_div_tooltip_json(data, custom_formats={}, name_prefix=None):
 if not isinstance(data, (dict)):
  if not (isinstance(data, str) and '@' in data):
   raise JsonSchemaValueException("" + (name_prefix or "data") + " must be object", value=data, name="" + (name_prefix or "data") + "", definition={'type': 'object', '$description': 'translations.json#/div_tooltip', 'properties': {'id': {'type': 'string', 'minLength': 1, 'clientMinLength': 1}, 'div': {'generate_case_for_templates_kotlinDsl': True, 'generate_case_for_templates_typescript': True, 'anyOf': [{'$ref': 'div-image.json', '$description': 'translations.json#/div_image_short'}, {'$ref': 'div-gif-image.json', '$description': 'translations.json#/div_gif_image_short'}, {'$ref': 'div-text.json', '$description': 'translations.json#/div_text_short'}, {'$ref': 'div-separator.json', '$description': 'translations.json#/div_separator_short'}, {'$ref': 'div-container.json', '$description': 'translations.json#/div_container_short'}, {'$ref': 'div-grid.json', '$description': 'translations.json#/div_grid_short'}, {'$ref': 'div-gallery.json', '$description': 'translations.json#/div_gallery_short'}, {'$ref': 'div-pager.json', '$description': 'translations.json#/div_pager_short'}, {'$ref': 'div-tabs.json', '$description': 'translations.json#/div_tabs_short'}, {'$ref': 'div-state.json', '$description': 'translations.json#/div_state_short'}, {'$ref': 'div-custom.json', '$description': 'translations.json#/div_custom_short'}, {'$ref': 'div-indicator.json', '$description': 'translations.json#/div_indicator_short'}, {'$ref': 'div-slider.json', '$description': 'translations.json#/div_slider_short'}, {'$ref': 'div-input.json', '$description': 'translations.json#/div_input_short'}, {'$ref': 'div-select.json', '$description': 'translations.json#/div_select'}, {'$ref': 'div-video.json', '$description': 'translations.json#/div_video'}], '$schema': 'http://json-schema.org/draft-07/schema'}, 'position': {'type': 'string', 'enum': ['left', 'top-left', 'top', 'top-right', 'right', 'bottom-right', 'bottom', 'bottom-left', 'center'], '$description': 'translations.json#/div_tooltip_position'}, 'duration': {'type': 'integer', 'constraint': 'number >= 0'}, 'offset': {'type': 'object', '$description': 'translations.json#/div_point', 'properties': {'x': {'$ref': 'div-dimension.json', '$description': 'translations.json#/div_point_x'}, 'y': {'$ref': 'div-dimension.json', '$description': 'translations.json#/div_point_y'}}, 'required': ['x', 'y'], '$schema': 'http://json-schema.org/draft-07/schema'}, 'animation_in': {'type': 'object', '$description': 'translations.json#/div_animation', 'properties': {'name': {'type': 'string', 'enum': ['fade', 'translate', 'scale', 'native', 'set', 'no_animation'], '$description': 'translations.json#/div_animation_name'}, 'duration': {'$ref': 'common.json#/non_negative_integer', 'default_value': '300', '$description': 'translations.json#/div_animation_duration'}, 'start_delay': {'$ref': 'common.json#/non_negative_integer', 'default_value': '0', '$description': 'translations.json#/div_animation_start_delay'}, 'start_value': {'type': 'number', '$description': 'translations.json#/div_animation_start_value'}, 'end_value': {'type': 'number', '$description': 'translations.json#/div_animation_end_value'}, 'repeat': {'alias_swift': 'repeat_count', '$ref': 'div-count.json', 'default_value': '{ "type": "infinity" }', '$description': 'translations.json#/div_animation_repeat'}, 'interpolator': {'$ref': 'div-animation-interpolator.json', 'default_value': 'spring', '$description': 'translations.json#/div_animation_interpolator'}, 'items': {'type': 'array', 'items': {'$ref': 'div-animation.json'}, 'minItems': 1, '$description': 'translations.json#/div_animation_items'}}, 'required': ['name'], '$schema': 'http://json-schema.org/draft-07/schema'}, 'animation_out': {'type': 'object', '$description': 'translations.json#/div_animation', 'properties': {'name': {'type': 'string', 'enum': ['fade', 'translate', 'scale', 'native', 'set', 'no_animation'], '$description': 'translations.json#/div_animation_name'}, 'duration': {'$ref': 'common.json#/non_negative_integer', 'default_value': '300', '$description': 'translations.json#/div_animation_duration'}, 'start_delay': {'$ref': 'common.json#/non_negative_integer', 'default_value': '0', '$description': 'translations.json#/div_animation_start_delay'}, 'start_value': {'type': 'number', '$description': 'translations.json#/div_animation_start_value'}, 'end_value': {'type': 'number', '$description': 'translations.json#/div_animation_end_value'}, 'repeat': {'alias_swift': 'repeat_count', '$ref': 'div-count.json', 'default_value': '{ "type": "infinity" }', '$description': 'translations.json#/div_animation_repeat'}, 'interpolator': {'$ref': 'div-animation-interpolator.json', 'default_value': 'spring', '$description': 'translations.json#/div_animation_interpolator'}, 'items': {'type': 'array', 'items': {'$ref': 'div-animation.json'}, 'minItems': 1, '$description': 'translations.json#/div_animation_items'}}, 'required': ['name'], '$schema': 'http://json-schema.org/draft-07/schema'}}, 'required': ['id', 'div', 'position'], '$schema': 'http://json-schema.org/draft-07/schema'}, rule='type')
 data_is_dict = isinstance(data, dict)
 if data_is_dict:
  data__missing_keys = set(['id', 'div', 'position']) - data.keys()
  if data__missing_keys:
   if not (isinstance(data, str) and '@' in data):
    raise JsonSchemaValueException("" + (name_prefix or "data") + " must contain " + (str(sorted(data__missing_keys)) + " properties"), value=data, name="" + (name_prefix or "data") + "", definition={'type': 'object', '$description': 'translations.json#/div_tooltip', 'properties': {'id': {'type': 'string', 'minLength': 1, 'clientMinLength': 1}, 'div': {'generate_case_for_templates_kotlinDsl': True, 'generate_case_for_templates_typescript': True, 'anyOf': [{'$ref': 'div-image.json', '$description': 'translations.json#/div_image_short'}, {'$ref': 'div-gif-image.json', '$description': 'translations.json#/div_gif_image_short'}, {'$ref': 'div-text.json', '$description': 'translations.json#/div_text_short'}, {'$ref': 'div-separator.json', '$description': 'translations.json#/div_separator_short'}, {'$ref': 'div-container.json', '$description': 'translations.json#/div_container_short'}, {'$ref': 'div-grid.json', '$description': 'translations.json#/div_grid_short'}, {'$ref': 'div-gallery.json', '$description': 'translations.json#/div_gallery_short'}, {'$ref': 'div-pager.json', '$description': 'translations.json#/div_pager_short'}, {'$ref': 'div-tabs.json', '$description': 'translations.json#/div_tabs_short'}, {'$ref': 'div-state.json', '$description': 'translations.json#/div_state_short'}, {'$ref': 'div-custom.json', '$description': 'translations.json#/div_custom_short'}, {'$ref': 'div-indicator.json', '$description': 'translations.json#/div_indicator_short'}, {'$ref': 'div-slider.json', '$description': 'translations.json#/div_slider_short'}, {'$ref': 'div-input.json', '$description': 'translations.json#/div_input_short'}, {'$ref': 'div-select.json', '$description': 'translations.json#/div_select'}, {'$ref': 'div-video.json', '$description': 'translations.json#/div_video'}], '$schema': 'http://json-schema.org/draft-07/schema'}, 'position': {'type': 'string', 'enum': ['left', 'top-left', 'top', 'top-right', 'right', 'bottom-right', 'bottom', 'bottom-left', 'center'], '$description': 'translations.json#/div_tooltip_position'}, 'duration': {'type': 'integer', 'constraint': 'number >= 0'}, 'offset': {'type': 'object', '$description': 'translations.json#/div_point', 'properties': {'x': {'$ref': 'div-dimension.json', '$description': 'translations.json#/div_point_x'}, 'y': {'$ref': 'div-dimension.json', '$description': 'translations.json#/div_point_y'}}, 'required': ['x', 'y'], '$schema': 'http://json-schema.org/draft-07/schema'}, 'animation_in': {'type': 'object', '$description': 'translations.json#/div_animation', 'properties': {'name': {'type': 'string', 'enum': ['fade', 'translate', 'scale', 'native', 'set', 'no_animation'], '$description': 'translations.json#/div_animation_name'}, 'duration': {'$ref': 'common.json#/non_negative_integer', 'default_value': '300', '$description': 'translations.json#/div_animation_duration'}, 'start_delay': {'$ref': 'common.json#/non_negative_integer', 'default_value': '0', '$description': 'translations.json#/div_animation_start_delay'}, 'start_value': {'type': 'number', '$description': 'translations.json#/div_animation_start_value'}, 'end_value': {'type': 'number', '$description': 'translations.json#/div_animation_end_value'}, 'repeat': {'alias_swift': 'repeat_count', '$ref': 'div-count.json', 'default_value': '{ "type": "infinity" }', '$description': 'translations.json#/div_animation_repeat'}, 'interpolator': {'$ref': 'div-animation-interpolator.json', 'default_value': 'spring', '$description': 'translations.json#/div_animation_interpolator'}, 'items': {'type': 'array', 'items': {'$ref': 'div-animation.json'}, 'minItems': 1, '$description': 'translations.json#/div_animation_items'}}, 'required': ['name'], '$schema': 'http://json-schema.org/draft-07/schema'}, 'animation_out': {'type': 'object', '$description': 'translations.json#/div_animation', 'properties': {'name': {'type': 'string', 'enum': ['fade', 'translate', 'scale', 'native', 'set', 'no_animation'], '$description': 'translations.json#/div_animation_name'}, 'duration': {'$ref': 'common.json#/non_negative_integer', 'default_value': '300', '$description': 'translations.json#/div_animation_duration'}, 'start_delay': {'$ref': 'common.json#/non_negative_integer', 'default_value': '0', '$description': 'translations.json#/div_animation_start_delay'}, 'start_value': {'type': 'number', '$description': 'translations.json#/div_animation_start_value'}, 'end_value': {'type': 'number', '$description': 'translations.json#/div_animation_end_value'}, 'repeat': {'alias_swift': 'repeat_count', '$ref': 'div-count.json', 'default_value': '{ "type": "infinity" }', '$description': 'translations.json#/div_animation_repeat'}, 'interpolator': {'$ref': 'div-animation-interpolator.json', 'default_value': 'spring', '$description': 'translations.json#/div_animation_interpolator'}, 'items': {'type': 'array', 'items': {'$ref': 'div-animation.json'}, 'minItems': 1, '$description': 'translations.json#/div_animation_items'}}, 'required': ['name'], '$schema': 'http://json-schema.org/draft-07/schema'}}, 'required': ['id', 'div', 'position'], '$schema': 'http://json-schema.org/draft-07/schema'}, rule='required')
  data_keys = set(data.keys())
  if "id" in data_keys:
   data_keys.remove("id")
   data__id = data["id"]
   validate_common_json__non_empty_string(data__id, custom_formats, (name_prefix or "data") + ".id")
  if "div" in data_keys:
   data_keys.remove("div")
   data__div = data["div"]
   validate_div_json(data__div, custom_formats, (name_prefix or "data") + ".div")
  if "position" in data_keys:
   data_keys.remove("position")
   data__position = data["position"]
   if not isinstance(data__position, (str)):
    if not (isinstance(data__position, str) and '@' in data__position):
     raise JsonSchemaValueException("" + (name_prefix or "data") + ".position must be string", value=data__position, name="" + (name_prefix or "data") + ".position", definition={'type': 'string', 'enum': ['left', 'top-left', 'top', 'top-right', 'right', 'bottom-right', 'bottom', 'bottom-left', 'center'], '$description': 'translations.json#/div_tooltip_position'}, rule='type')
   if data__position not in ['left', 'top-left', 'top', 'top-right', 'right', 'bottom-right', 'bottom', 'bottom-left', 'center']:
    if not (isinstance(data__position, str) and '@' in data__position):
     raise JsonSchemaValueException("" + (name_prefix or "data") + ".position must be one of ['left', 'top-left', 'top', 'top-right', 'right', 'bottom-right', 'bottom', 'bottom-left', 'center']", value=data__position, name="" + (name_prefix or "data") + ".position", definition={'type': 'string', 'enum': ['left', 'top-left', 'top', 'top-right', 'right', 'bottom-right', 'bottom', 'bottom-left', 'center'], '$description': 'translations.json#/div_tooltip_position'}, rule='enum')
  if "duration" in data_keys:
   data_keys.remove("duration")
   data__duration = data["duration"]
   validate_common_json__non_negative_integer(data__duration, custom_formats, (name_prefix or "data") + ".duration")
  if "offset" in data_keys:
   data_keys.remove("offset")
   data__offset = data["offset"]
   validate_div_point_json(data__offset, custom_formats, (name_prefix or "data") + ".offset")
  if "animation_in" in data_keys:
   data_keys.remove("animation_in")
   data__animationin = data["animation_in"]
   validate_div_animation_json(data__animationin, custom_formats, (name_prefix or "data") + ".animation_in")
  if "animation_out" in data_keys:
   data_keys.remove("animation_out")
   data__animationout = data["animation_out"]
   validate_div_animation_json(data__animationout, custom_formats, (name_prefix or "data") + ".animation_out")
 return data

def validate_div_animation_json(data, custom_formats={}, name_prefix=None):
 if not isinstance(data, (dict)):
  if not (isinstance(data, str) and '@' in data):
   raise JsonSchemaValueException("" + (name_prefix or "data") + " must be object", value=data, name="" + (name_prefix or "data") + "", definition={'type': 'object', '$description': 'translations.json#/div_animation', 'properties': {'name': {'type': 'string', 'enum': ['fade', 'translate', 'scale', 'native', 'set', 'no_animation'], '$description': 'translations.json#/div_animation_name'}, 'duration': {'type': 'integer', 'constraint': 'number >= 0'}, 'start_delay': {'type': 'integer', 'constraint': 'number >= 0'}, 'start_value': {'type': 'number', '$description': 'translations.json#/div_animation_start_value'}, 'end_value': {'type': 'number', '$description': 'translations.json#/div_animation_end_value'}, 'repeat': {'anyOf': [{'$ref': 'div-infinity-count.json', '$description': 'translations.json#/div_count_infinity'}, {'$ref': 'div-fixed-count.json', '$description': 'translations.json#/div_count_fixed'}], '$schema': 'http://json-schema.org/draft-07/schema'}, 'interpolator': {'type': 'string', 'enum': ['linear', 'ease', 'ease_in', 'ease_out', 'ease_in_out', 'spring'], '$description': 'translations.json#/div_animation_interpolator', '$schema': 'http://json-schema.org/draft-07/schema'}, 'items': {'type': 'array', 'items': {'type': 'object', '$description': 'translations.json#/div_animation', 'properties': {'name': {'type': 'string', 'enum': ['fade', 'translate', 'scale', 'native', 'set', 'no_animation'], '$description': 'translations.json#/div_animation_name'}, 'duration': {'$ref': 'common.json#/non_negative_integer', 'default_value': '300', '$description': 'translations.json#/div_animation_duration'}, 'start_delay': {'$ref': 'common.json#/non_negative_integer', 'default_value': '0', '$description': 'translations.json#/div_animation_start_delay'}, 'start_value': {'type': 'number', '$description': 'translations.json#/div_animation_start_value'}, 'end_value': {'type': 'number', '$description': 'translations.json#/div_animation_end_value'}, 'repeat': {'alias_swift': 'repeat_count', '$ref': 'div-count.json', 'default_value': '{ "type": "infinity" }', '$description': 'translations.json#/div_animation_repeat'}, 'interpolator': {'$ref': 'div-animation-interpolator.json', 'default_value': 'spring', '$description': 'translations.json#/div_animation_interpolator'}, 'items': {'type': 'array', 'items': {'$ref': 'div-animation.json'}, 'minItems': 1, '$description': 'translations.json#/div_animation_items'}}, 'required': ['name'], '$schema': 'http://json-schema.org/draft-07/schema'}, 'minItems': 1, '$description': 'translations.json#/div_animation_items'}}, 'required': ['name'], '$schema': 'http://json-schema.org/draft-07/schema'}, rule='type')
 data_is_dict = isinstance(data, dict)
 if data_is_dict:
  data__missing_keys = set(['name']) - data.keys()
  if data__missing_keys:
   if not (isinstance(data, str) and '@' in data):
    raise JsonSchemaValueException("" + (name_prefix or "data") + " must contain " + (str(sorted(data__missing_keys)) + " properties"), value=data, name="" + (name_prefix or "data") + "", definition={'type': 'object', '$description': 'translations.json#/div_animation', 'properties': {'name': {'type': 'string', 'enum': ['fade', 'translate', 'scale', 'native', 'set', 'no_animation'], '$description': 'translations.json#/div_animation_name'}, 'duration': {'type': 'integer', 'constraint': 'number >= 0'}, 'start_delay': {'type': 'integer', 'constraint': 'number >= 0'}, 'start_value': {'type': 'number', '$description': 'translations.json#/div_animation_start_value'}, 'end_value': {'type': 'number', '$description': 'translations.json#/div_animation_end_value'}, 'repeat': {'anyOf': [{'$ref': 'div-infinity-count.json', '$description': 'translations.json#/div_count_infinity'}, {'$ref': 'div-fixed-count.json', '$description': 'translations.json#/div_count_fixed'}], '$schema': 'http://json-schema.org/draft-07/schema'}, 'interpolator': {'type': 'string', 'enum': ['linear', 'ease', 'ease_in', 'ease_out', 'ease_in_out', 'spring'], '$description': 'translations.json#/div_animation_interpolator', '$schema': 'http://json-schema.org/draft-07/schema'}, 'items': {'type': 'array', 'items': {'type': 'object', '$description': 'translations.json#/div_animation', 'properties': {'name': {'type': 'string', 'enum': ['fade', 'translate', 'scale', 'native', 'set', 'no_animation'], '$description': 'translations.json#/div_animation_name'}, 'duration': {'$ref': 'common.json#/non_negative_integer', 'default_value': '300', '$description': 'translations.json#/div_animation_duration'}, 'start_delay': {'$ref': 'common.json#/non_negative_integer', 'default_value': '0', '$description': 'translations.json#/div_animation_start_delay'}, 'start_value': {'type': 'number', '$description': 'translations.json#/div_animation_start_value'}, 'end_value': {'type': 'number', '$description': 'translations.json#/div_animation_end_value'}, 'repeat': {'alias_swift': 'repeat_count', '$ref': 'div-count.json', 'default_value': '{ "type": "infinity" }', '$description': 'translations.json#/div_animation_repeat'}, 'interpolator': {'$ref': 'div-animation-interpolator.json', 'default_value': 'spring', '$description': 'translations.json#/div_animation_interpolator'}, 'items': {'type': 'array', 'items': {'$ref': 'div-animation.json'}, 'minItems': 1, '$description': 'translations.json#/div_animation_items'}}, 'required': ['name'], '$schema': 'http://json-schema.org/draft-07/schema'}, 'minItems': 1, '$description': 'translations.json#/div_animation_items'}}, 'required': ['name'], '$schema': 'http://json-schema.org/draft-07/schema'}, rule='required')
  data_keys = set(data.keys())
  if "name" in data_keys:
   data_keys.remove("name")
   data__name = data["name"]
   if not isinstance(data__name, (str)):
    if not (isinstance(data__name, str) and '@' in data__name):
     raise JsonSchemaValueException("" + (name_prefix or "data") + ".name must be string", value=data__name, name="" + (name_prefix or "data") + ".name", definition={'type': 'string', 'enum': ['fade', 'translate', 'scale', 'native', 'set', 'no_animation'], '$description': 'translations.json#/div_animation_name'}, rule='type')
   if data__name not in ['fade', 'translate', 'scale', 'native', 'set', 'no_animation']:
    if not (isinstance(data__name, str) and '@' in data__name):
     raise JsonSchemaValueException("" + (name_prefix or "data") + ".name must be one of ['fade', 'translate', 'scale', 'native', 'set', 'no_animation']", value=data__name, name="" + (name_prefix or "data") + ".name", definition={'type': 'string', 'enum': ['fade', 'translate', 'scale', 'native', 'set', 'no_animation'], '$description': 'translations.json#/div_animation_name'}, rule='enum')
  if "duration" in data_keys:
   data_keys.remove("duration")
   data__duration = data["duration"]
   validate_common_json__non_negative_integer(data__duration, custom_formats, (name_prefix or "data") + ".duration")
  if "start_delay" in data_keys:
   data_keys.remove("start_delay")
   data__startdelay = data["start_delay"]
   validate_common_json__non_negative_integer(data__startdelay, custom_formats, (name_prefix or "data") + ".start_delay")
  if "start_value" in data_keys:
   data_keys.remove("start_value")
   data__startvalue = data["start_value"]
   if not isinstance(data__startvalue, (int, float, Decimal)) or isinstance(data__startvalue, bool):
    if not (isinstance(data__startvalue, str) and '@' in data__startvalue):
     raise JsonSchemaValueException("" + (name_prefix or "data") + ".start_value must be number", value=data__startvalue, name="" + (name_prefix or "data") + ".start_value", definition={'type': 'number', '$description': 'translations.json#/div_animation_start_value'}, rule='type')
  if "end_value" in data_keys:
   data_keys.remove("end_value")
   data__endvalue = data["end_value"]
   if not isinstance(data__endvalue, (int, float, Decimal)) or isinstance(data__endvalue, bool):
    if not (isinstance(data__endvalue, str) and '@' in data__endvalue):
     raise JsonSchemaValueException("" + (name_prefix or "data") + ".end_value must be number", value=data__endvalue, name="" + (name_prefix or "data") + ".end_value", definition={'type': 'number', '$description': 'translations.json#/div_animation_end_value'}, rule='type')
  if "repeat" in data_keys:
   data_keys.remove("repeat")
   data__repeat = data["repeat"]
   validate_div_count_json(data__repeat, custom_formats, (name_prefix or "data") + ".repeat")
  if "interpolator" in data_keys:
   data_keys.remove("interpolator")
   data__interpolator = data["interpolator"]
   validate_div_animation_interpolator_json(data__interpolator, custom_formats, (name_prefix or "data") + ".interpolator")
  if "items" in data_keys:
   data_keys.remove("items")
   data__items = data["items"]
   if not isinstance(data__items, (list, tuple)):
    if not (isinstance(data__items, str) and '@' in data__items):
     raise JsonSchemaValueException("" + (name_prefix or "data") + ".items must be array", value=data__items, name="" + (name_prefix or "data") + ".items", definition={'type': 'array', 'items': {'type': 'object', '$description': 'translations.json#/div_animation', 'properties': {'name': {'type': 'string', 'enum': ['fade', 'translate', 'scale', 'native', 'set', 'no_animation'], '$description': 'translations.json#/div_animation_name'}, 'duration': {'$ref': 'common.json#/non_negative_integer', 'default_value': '300', '$description': 'translations.json#/div_animation_duration'}, 'start_delay': {'$ref': 'common.json#/non_negative_integer', 'default_value': '0', '$description': 'translations.json#/div_animation_start_delay'}, 'start_value': {'type': 'number', '$description': 'translations.json#/div_animation_start_value'}, 'end_value': {'type': 'number', '$description': 'translations.json#/div_animation_end_value'}, 'repeat': {'alias_swift': 'repeat_count', '$ref': 'div-count.json', 'default_value': '{ "type": "infinity" }', '$description': 'translations.json#/div_animation_repeat'}, 'interpolator': {'$ref': 'div-animation-interpolator.json', 'default_value': 'spring', '$description': 'translations.json#/div_animation_interpolator'}, 'items': {'type': 'array', 'items': {'$ref': 'div-animation.json'}, 'minItems': 1, '$description': 'translations.json#/div_animation_items'}}, 'required': ['name'], '$schema': 'http://json-schema.org/draft-07/schema'}, 'minItems': 1, '$description': 'translations.json#/div_animation_items'}, rule='type')
   data__items_is_list = isinstance(data__items, (list, tuple))
   if data__items_is_list:
    data__items_len = len(data__items)
    if data__items_len < 1:
     if not (isinstance(data__items, str) and '@' in data__items):
      raise JsonSchemaValueException("" + (name_prefix or "data") + ".items must contain at least 1 items", value=data__items, name="" + (name_prefix or "data") + ".items", definition={'type': 'array', 'items': {'type': 'object', '$description': 'translations.json#/div_animation', 'properties': {'name': {'type': 'string', 'enum': ['fade', 'translate', 'scale', 'native', 'set', 'no_animation'], '$description': 'translations.json#/div_animation_name'}, 'duration': {'$ref': 'common.json#/non_negative_integer', 'default_value': '300', '$description': 'translations.json#/div_animation_duration'}, 'start_delay': {'$ref': 'common.json#/non_negative_integer', 'default_value': '0', '$description': 'translations.json#/div_animation_start_delay'}, 'start_value': {'type': 'number', '$description': 'translations.json#/div_animation_start_value'}, 'end_value': {'type': 'number', '$description': 'translations.json#/div_animation_end_value'}, 'repeat': {'alias_swift': 'repeat_count', '$ref': 'div-count.json', 'default_value': '{ "type": "infinity" }', '$description': 'translations.json#/div_animation_repeat'}, 'interpolator': {'$ref': 'div-animation-interpolator.json', 'default_value': 'spring', '$description': 'translations.json#/div_animation_interpolator'}, 'items': {'type': 'array', 'items': {'$ref': 'div-animation.json'}, 'minItems': 1, '$description': 'translations.json#/div_animation_items'}}, 'required': ['name'], '$schema': 'http://json-schema.org/draft-07/schema'}, 'minItems': 1, '$description': 'translations.json#/div_animation_items'}, rule='minItems')
    for data__items_x, data__items_item in enumerate(data__items):
     validate_div_animation_json(data__items_item, custom_formats, (name_prefix or "data") + ".items[{data__items_x}]".format(**locals()))
 return data

def validate_div_count_json(data, custom_formats={}, name_prefix=None):
 data_any_of_count9 = 0
 if not data_any_of_count9:
  try:
   validate_div_infinity_count_json(data, custom_formats, (name_prefix or "data") + "")
   data_any_of_count9 += 1
  except JsonSchemaValueException: pass
 if not data_any_of_count9:
  try:
   validate_div_fixed_count_json(data, custom_formats, (name_prefix or "data") + "")
   data_any_of_count9 += 1
  except JsonSchemaValueException: pass
 if not data_any_of_count9:
  if not (isinstance(data, str) and '@' in data):
   raise JsonSchemaValueException("" + (name_prefix or "data") + " cannot be validated by any definition", value=data, name="" + (name_prefix or "data") + "", definition={'anyOf': [{'type': 'object', '$description': 'translations.json#/div_infinity_count', 'properties': {'type': {'type': 'string', 'enum': ['infinity']}}, 'required': ['type'], '$schema': 'http://json-schema.org/draft-07/schema'}, {'type': 'object', '$description': 'translations.json#/div_fixed_count', 'properties': {'value': {'$ref': 'common.json#/non_negative_integer', '$description': 'translations.json#/div_fixed_count_value'}, 'type': {'type': 'string', 'enum': ['fixed']}}, 'required': ['value', 'type'], '$schema': 'http://json-schema.org/draft-07/schema'}], '$schema': 'http://json-schema.org/draft-07/schema'}, rule='anyOf')
 return data

def validate_div_fixed_count_json(data, custom_formats={}, name_prefix=None):
 if not isinstance(data, (dict)):
  if not (isinstance(data, str) and '@' in data):
   raise JsonSchemaValueException("" + (name_prefix or "data") + " must be object", value=data, name="" + (name_prefix or "data") + "", definition={'type': 'object', '$description': 'translations.json#/div_fixed_count', 'properties': {'value': {'type': 'integer', 'constraint': 'number >= 0'}, 'type': {'type': 'string', 'enum': ['fixed']}}, 'required': ['value', 'type'], '$schema': 'http://json-schema.org/draft-07/schema'}, rule='type')
 data_is_dict = isinstance(data, dict)
 if data_is_dict:
  data__missing_keys = set(['value', 'type']) - data.keys()
  if data__missing_keys:
   if not (isinstance(data, str) and '@' in data):
    raise JsonSchemaValueException("" + (name_prefix or "data") + " must contain " + (str(sorted(data__missing_keys)) + " properties"), value=data, name="" + (name_prefix or "data") + "", definition={'type': 'object', '$description': 'translations.json#/div_fixed_count', 'properties': {'value': {'type': 'integer', 'constraint': 'number >= 0'}, 'type': {'type': 'string', 'enum': ['fixed']}}, 'required': ['value', 'type'], '$schema': 'http://json-schema.org/draft-07/schema'}, rule='required')
  data_keys = set(data.keys())
  if "value" in data_keys:
   data_keys.remove("value")
   data__value = data["value"]
   validate_common_json__non_negative_integer(data__value, custom_formats, (name_prefix or "data") + ".value")
  if "type" in data_keys:
   data_keys.remove("type")
   data__type = data["type"]
   if not isinstance(data__type, (str)):
    if not (isinstance(data__type, str) and '@' in data__type):
     raise JsonSchemaValueException("" + (name_prefix or "data") + ".type must be string", value=data__type, name="" + (name_prefix or "data") + ".type", definition={'type': 'string', 'enum': ['fixed']}, rule='type')
   if data__type not in ['fixed']:
    if not (isinstance(data__type, str) and '@' in data__type):
     raise JsonSchemaValueException("" + (name_prefix or "data") + ".type must be one of ['fixed']", value=data__type, name="" + (name_prefix or "data") + ".type", definition={'type': 'string', 'enum': ['fixed']}, rule='enum')
 return data

def validate_div_infinity_count_json(data, custom_formats={}, name_prefix=None):
 if not isinstance(data, (dict)):
  if not (isinstance(data, str) and '@' in data):
   raise JsonSchemaValueException("" + (name_prefix or "data") + " must be object", value=data, name="" + (name_prefix or "data") + "", definition={'type': 'object', '$description': 'translations.json#/div_infinity_count', 'properties': {'type': {'type': 'string', 'enum': ['infinity']}}, 'required': ['type'], '$schema': 'http://json-schema.org/draft-07/schema'}, rule='type')
 data_is_dict = isinstance(data, dict)
 if data_is_dict:
  data__missing_keys = set(['type']) - data.keys()
  if data__missing_keys:
   if not (isinstance(data, str) and '@' in data):
    raise JsonSchemaValueException("" + (name_prefix or "data") + " must contain " + (str(sorted(data__missing_keys)) + " properties"), value=data, name="" + (name_prefix or "data") + "", definition={'type': 'object', '$description': 'translations.json#/div_infinity_count', 'properties': {'type': {'type': 'string', 'enum': ['infinity']}}, 'required': ['type'], '$schema': 'http://json-schema.org/draft-07/schema'}, rule='required')
  data_keys = set(data.keys())
  if "type" in data_keys:
   data_keys.remove("type")
   data__type = data["type"]
   if not isinstance(data__type, (str)):
    if not (isinstance(data__type, str) and '@' in data__type):
     raise JsonSchemaValueException("" + (name_prefix or "data") + ".type must be string", value=data__type, name="" + (name_prefix or "data") + ".type", definition={'type': 'string', 'enum': ['infinity']}, rule='type')
   if data__type not in ['infinity']:
    if not (isinstance(data__type, str) and '@' in data__type):
     raise JsonSchemaValueException("" + (name_prefix or "data") + ".type must be one of ['infinity']", value=data__type, name="" + (name_prefix or "data") + ".type", definition={'type': 'string', 'enum': ['infinity']}, rule='enum')
 return data

def validate_div_point_json(data, custom_formats={}, name_prefix=None):
 if not isinstance(data, (dict)):
  if not (isinstance(data, str) and '@' in data):
   raise JsonSchemaValueException("" + (name_prefix or "data") + " must be object", value=data, name="" + (name_prefix or "data") + "", definition={'type': 'object', '$description': 'translations.json#/div_point', 'properties': {'x': {'type': 'object', '$description': 'translations.json#/div_dimension', 'codegen': {'divan': {'forced_properties_order': ['value']}}, 'properties': {'value': {'type': 'number', '$description': 'translations.json#/div_dimension_value'}, 'unit': {'$ref': 'div-size-unit.json', 'default_value': 'dp'}}, 'required': ['value'], '$schema': 'http://json-schema.org/draft-07/schema'}, 'y': {'type': 'object', '$description': 'translations.json#/div_dimension', 'codegen': {'divan': {'forced_properties_order': ['value']}}, 'properties': {'value': {'type': 'number', '$description': 'translations.json#/div_dimension_value'}, 'unit': {'$ref': 'div-size-unit.json', 'default_value': 'dp'}}, 'required': ['value'], '$schema': 'http://json-schema.org/draft-07/schema'}}, 'required': ['x', 'y'], '$schema': 'http://json-schema.org/draft-07/schema'}, rule='type')
 data_is_dict = isinstance(data, dict)
 if data_is_dict:
  data__missing_keys = set(['x', 'y']) - data.keys()
  if data__missing_keys:
   if not (isinstance(data, str) and '@' in data):
    raise JsonSchemaValueException("" + (name_prefix or "data") + " must contain " + (str(sorted(data__missing_keys)) + " properties"), value=data, name="" + (name_prefix or "data") + "", definition={'type': 'object', '$description': 'translations.json#/div_point', 'properties': {'x': {'type': 'object', '$description': 'translations.json#/div_dimension', 'codegen': {'divan': {'forced_properties_order': ['value']}}, 'properties': {'value': {'type': 'number', '$description': 'translations.json#/div_dimension_value'}, 'unit': {'$ref': 'div-size-unit.json', 'default_value': 'dp'}}, 'required': ['value'], '$schema': 'http://json-schema.org/draft-07/schema'}, 'y': {'type': 'object', '$description': 'translations.json#/div_dimension', 'codegen': {'divan': {'forced_properties_order': ['value']}}, 'properties': {'value': {'type': 'number', '$description': 'translations.json#/div_dimension_value'}, 'unit': {'$ref': 'div-size-unit.json', 'default_value': 'dp'}}, 'required': ['value'], '$schema': 'http://json-schema.org/draft-07/schema'}}, 'required': ['x', 'y'], '$schema': 'http://json-schema.org/draft-07/schema'}, rule='required')
  data_keys = set(data.keys())
  if "x" in data_keys:
   data_keys.remove("x")
   data__x = data["x"]
   validate_div_dimension_json(data__x, custom_formats, (name_prefix or "data") + ".x")
  if "y" in data_keys:
   data_keys.remove("y")
   data__y = data["y"]
   validate_div_dimension_json(data__y, custom_formats, (name_prefix or "data") + ".y")
 return data

def validate_div_disappear_action_json(data, custom_formats={}, name_prefix=None):
 validate_div_sight_action_json(data, custom_formats, (name_prefix or "data") + "")
 data_is_dict = isinstance(data, dict)
 if data_is_dict:
  data_keys = set(data.keys())
  if "visibility_percentage" in data_keys:
   data_keys.remove("visibility_percentage")
   data__visibilitypercentage = data["visibility_percentage"]
   if not isinstance(data__visibilitypercentage, (int)) and not (isinstance(data__visibilitypercentage, float) and data__visibilitypercentage.is_integer()) or isinstance(data__visibilitypercentage, bool):
    if not (isinstance(data__visibilitypercentage, str) and '@' in data__visibilitypercentage):
     raise JsonSchemaValueException("" + (name_prefix or "data") + ".visibility_percentage must be integer", value=data__visibilitypercentage, name="" + (name_prefix or "data") + ".visibility_percentage", definition={'type': 'integer', 'constraint': 'number >= 0 && number < 100', 'default_value': '0', '$description': 'translations.json#/div_disappear_action_visibility_percentage'}, rule='type')
  if "disappear_duration" in data_keys:
   data_keys.remove("disappear_duration")
   data__disappearduration = data["disappear_duration"]
   validate_common_json__non_negative_integer(data__disappearduration, custom_formats, (name_prefix or "data") + ".disappear_duration")
 return data

def validate_div_sight_action_json(data, custom_formats={}, name_prefix=None):
 if not isinstance(data, (dict)):
  if not (isinstance(data, str) and '@' in data):
   raise JsonSchemaValueException("" + (name_prefix or "data") + " must be object", value=data, name="" + (name_prefix or "data") + "", definition={'protocol_name': 'div-sight-action', 'type': 'object', 'codegen': {'documentation': {'include_in_toc': False}}, 'allOf': [{'properties': {'log_id': {'$ref': 'common.json#/non_empty_string', 'supports_expressions': False, '$description': 'translations.json#/div_action_base_log_id'}, 'url': {'$ref': 'common.json#/url', '$description': 'translations.json#/div_action_base_url'}, 'referer': {'$ref': 'common.json#/url', '$description': 'translations.json#/div_action_base_referer'}, 'payload': {'type': 'object', 'additionalProperties': True, '$description': 'translations.json#/div_action_base_payload'}, 'download_callbacks': {'$ref': 'div-download-callbacks.json', '$description': 'translations.json#/div_action_base_download_callbacks'}, 'typed': {'$ref': 'div-action-typed.json'}}, '$schema': 'http://json-schema.org/draft-07/schema'}, {'properties': {'log_limit': {'type': 'integer', 'constraint': 'number >= 0'}}}], 'required': ['log_id'], '$schema': 'http://json-schema.org/draft-07/schema'}, rule='type')
 validate_div_action_base_json(data, custom_formats, (name_prefix or "data") + "")
 data_is_dict = isinstance(data, dict)
 if data_is_dict:
  data_keys = set(data.keys())
  if "log_limit" in data_keys:
   data_keys.remove("log_limit")
   data__loglimit = data["log_limit"]
   validate_common_json__non_negative_integer(data__loglimit, custom_formats, (name_prefix or "data") + ".log_limit")
 data_is_dict = isinstance(data, dict)
 if data_is_dict:
  data__missing_keys = set(['log_id']) - data.keys()
  if data__missing_keys:
   if not (isinstance(data, str) and '@' in data):
    raise JsonSchemaValueException("" + (name_prefix or "data") + " must contain " + (str(sorted(data__missing_keys)) + " properties"), value=data, name="" + (name_prefix or "data") + "", definition={'protocol_name': 'div-sight-action', 'type': 'object', 'codegen': {'documentation': {'include_in_toc': False}}, 'allOf': [{'properties': {'log_id': {'$ref': 'common.json#/non_empty_string', 'supports_expressions': False, '$description': 'translations.json#/div_action_base_log_id'}, 'url': {'$ref': 'common.json#/url', '$description': 'translations.json#/div_action_base_url'}, 'referer': {'$ref': 'common.json#/url', '$description': 'translations.json#/div_action_base_referer'}, 'payload': {'type': 'object', 'additionalProperties': True, '$description': 'translations.json#/div_action_base_payload'}, 'download_callbacks': {'$ref': 'div-download-callbacks.json', '$description': 'translations.json#/div_action_base_download_callbacks'}, 'typed': {'$ref': 'div-action-typed.json'}}, '$schema': 'http://json-schema.org/draft-07/schema'}, {'properties': {'log_limit': {'type': 'integer', 'constraint': 'number >= 0'}}}], 'required': ['log_id'], '$schema': 'http://json-schema.org/draft-07/schema'}, rule='required')
 return data

def validate_div_visibility_action_json(data, custom_formats={}, name_prefix=None):
 validate_div_sight_action_json(data, custom_formats, (name_prefix or "data") + "")
 data_is_dict = isinstance(data, dict)
 if data_is_dict:
  data_keys = set(data.keys())
  if "visibility_percentage" in data_keys:
   data_keys.remove("visibility_percentage")
   data__visibilitypercentage = data["visibility_percentage"]
   if not isinstance(data__visibilitypercentage, (int)) and not (isinstance(data__visibilitypercentage, float) and data__visibilitypercentage.is_integer()) or isinstance(data__visibilitypercentage, bool):
    if not (isinstance(data__visibilitypercentage, str) and '@' in data__visibilitypercentage):
     raise JsonSchemaValueException("" + (name_prefix or "data") + ".visibility_percentage must be integer", value=data__visibilitypercentage, name="" + (name_prefix or "data") + ".visibility_percentage", definition={'type': 'integer', 'constraint': 'number > 0 && number <= 100', 'default_value': '50', '$description': 'translations.json#/div_visibility_action_visibility_percentage'}, rule='type')
  if "visibility_duration" in data_keys:
   data_keys.remove("visibility_duration")
   data__visibilityduration = data["visibility_duration"]
   validate_common_json__non_negative_integer(data__visibilityduration, custom_formats, (name_prefix or "data") + ".visibility_duration")
 return data

def validate_common_json__non_negative_integer(data, custom_formats={}, name_prefix=None):
 if not isinstance(data, (int)) and not (isinstance(data, float) and data.is_integer()) or isinstance(data, bool):
  if not (isinstance(data, str) and '@' in data):
   raise JsonSchemaValueException("" + (name_prefix or "data") + " must be integer", value=data, name="" + (name_prefix or "data") + "", definition={'type': 'integer', 'constraint': 'number >= 0'}, rule='type')
 return data

def validate_div_alignment_horizontal_json(data, custom_formats={}, name_prefix=None):
 if not isinstance(data, (str)):
  if not (isinstance(data, str) and '@' in data):
   raise JsonSchemaValueException("" + (name_prefix or "data") + " must be string", value=data, name="" + (name_prefix or "data") + "", definition={'type': 'string', 'enum': ['left', 'center', 'right', 'start', 'end'], '$schema': 'http://json-schema.org/draft-07/schema'}, rule='type')
 if data not in ['left', 'center', 'right', 'start', 'end']:
  if not (isinstance(data, str) and '@' in data):
   raise JsonSchemaValueException("" + (name_prefix or "data") + " must be one of ['left', 'center', 'right', 'start', 'end']", value=data, name="" + (name_prefix or "data") + "", definition={'type': 'string', 'enum': ['left', 'center', 'right', 'start', 'end'], '$schema': 'http://json-schema.org/draft-07/schema'}, rule='enum')
 return data

def validate_div_alignment_vertical_json(data, custom_formats={}, name_prefix=None):
 if not isinstance(data, (str)):
  if not (isinstance(data, str) and '@' in data):
   raise JsonSchemaValueException("" + (name_prefix or "data") + " must be string", value=data, name="" + (name_prefix or "data") + "", definition={'type': 'string', 'enum': ['top', 'center', 'bottom', 'baseline'], '$schema': 'http://json-schema.org/draft-07/schema'}, rule='type')
 if data not in ['top', 'center', 'bottom', 'baseline']:
  if not (isinstance(data, str) and '@' in data):
   raise JsonSchemaValueException("" + (name_prefix or "data") + " must be one of ['top', 'center', 'bottom', 'baseline']", value=data, name="" + (name_prefix or "data") + "", definition={'type': 'string', 'enum': ['top', 'center', 'bottom', 'baseline'], '$schema': 'http://json-schema.org/draft-07/schema'}, rule='enum')
 return data

def validate_div_edge_insets_json(data, custom_formats={}, name_prefix=None):
 if not isinstance(data, (dict)):
  if not (isinstance(data, str) and '@' in data):
   raise JsonSchemaValueException("" + (name_prefix or "data") + " must be object", value=data, name="" + (name_prefix or "data") + "", definition={'type': 'object', '$description': 'translations.json#/div_edge_insets', 'properties': {'left': {'type': 'integer', 'constraint': 'number >= 0'}, 'right': {'type': 'integer', 'constraint': 'number >= 0'}, 'top': {'type': 'integer', 'constraint': 'number >= 0'}, 'bottom': {'type': 'integer', 'constraint': 'number >= 0'}, 'start': {'type': 'integer', 'constraint': 'number >= 0'}, 'end': {'type': 'integer', 'constraint': 'number >= 0'}, 'unit': {'type': 'string', 'enum': ['dp', 'sp', 'px'], '$description': 'translations.json#/div_size_unit', 'platforms': ['android', 'ios'], '$schema': 'http://json-schema.org/draft-07/schema'}}, '$schema': 'http://json-schema.org/draft-07/schema'}, rule='type')
 data_is_dict = isinstance(data, dict)
 if data_is_dict:
  data_keys = set(data.keys())
  if "left" in data_keys:
   data_keys.remove("left")
   data__left = data["left"]
   validate_common_json__non_negative_integer(data__left, custom_formats, (name_prefix or "data") + ".left")
  if "right" in data_keys:
   data_keys.remove("right")
   data__right = data["right"]
   validate_common_json__non_negative_integer(data__right, custom_formats, (name_prefix or "data") + ".right")
  if "top" in data_keys:
   data_keys.remove("top")
   data__top = data["top"]
   validate_common_json__non_negative_integer(data__top, custom_formats, (name_prefix or "data") + ".top")
  if "bottom" in data_keys:
   data_keys.remove("bottom")
   data__bottom = data["bottom"]
   validate_common_json__non_negative_integer(data__bottom, custom_formats, (name_prefix or "data") + ".bottom")
  if "start" in data_keys:
   data_keys.remove("start")
   data__start = data["start"]
   validate_common_json__non_negative_integer(data__start, custom_formats, (name_prefix or "data") + ".start")
  if "end" in data_keys:
   data_keys.remove("end")
   data__end = data["end"]
   validate_common_json__non_negative_integer(data__end, custom_formats, (name_prefix or "data") + ".end")
  if "unit" in data_keys:
   data_keys.remove("unit")
   data__unit = data["unit"]
   validate_div_size_unit_json(data__unit, custom_formats, (name_prefix or "data") + ".unit")
 return data

def validate_div_background_json(data, custom_formats={}, name_prefix=None):
 data_any_of_count10 = 0
 if not data_any_of_count10:
  try:
   validate_div_linear_gradient_json(data, custom_formats, (name_prefix or "data") + "")
   data_any_of_count10 += 1
  except JsonSchemaValueException: pass
 if not data_any_of_count10:
  try:
   validate_div_radial_gradient_json(data, custom_formats, (name_prefix or "data") + "")
   data_any_of_count10 += 1
  except JsonSchemaValueException: pass
 if not data_any_of_count10:
  try:
   validate_div_image_background_json(data, custom_formats, (name_prefix or "data") + "")
   data_any_of_count10 += 1
  except JsonSchemaValueException: pass
 if not data_any_of_count10:
  try:
   validate_div_solid_background_json(data, custom_formats, (name_prefix or "data") + "")
   data_any_of_count10 += 1
  except JsonSchemaValueException: pass
 if not data_any_of_count10:
  try:
   validate_div_nine_patch_background_json(data, custom_formats, (name_prefix or "data") + "")
   data_any_of_count10 += 1
  except JsonSchemaValueException: pass
 if not data_any_of_count10:
  if not (isinstance(data, str) and '@' in data):
   raise JsonSchemaValueException("" + (name_prefix or "data") + " cannot be validated by any definition", value=data, name="" + (name_prefix or "data") + "", definition={'anyOf': [{'type': 'object', '$description': 'translations.json#/div_gradient_linear', 'properties': {'colors': {'type': 'array', 'items': {'$ref': 'common.json#/color'}, 'minItems': 2, '$description': 'translations.json#/div_gradient_colors'}, 'angle': {'type': 'integer', 'constraint': 'number >= 0 && number <= 360', 'default_value': '0', '$description': 'translations.json#/div_gradient_linear_angle'}, 'type': {'type': 'string', 'enum': ['gradient']}}, 'required': ['colors', 'type'], '$schema': 'http://json-schema.org/draft-07/schema'}, {'type': 'object', '$description': 'translations.json#/div_gradient_radial', 'properties': {'colors': {'type': 'array', 'items': {'$ref': 'common.json#/color'}, 'minItems': 2, '$description': 'translations.json#/div_gradient_colors'}, 'radius': {'$ref': 'div-radial-gradient-radius.json', 'default_value': '{"type": "relative", "value": "farthest_corner" }', '$description': 'translations.json#/div_gradient_radial_radius'}, 'center_x': {'$ref': 'div-radial-gradient-center.json', 'default_value': '{"type": "relative", "value": 0.5 }', '$description': 'translations.json#/div_gradient_radial_center_x'}, 'center_y': {'$ref': 'div-radial-gradient-center.json', 'default_value': '{"type": "relative", "value": 0.5 }', '$description': 'translations.json#/div_gradient_radial_center_y'}, 'type': {'type': 'string', 'enum': ['radial_gradient']}}, 'required': ['colors', 'type'], '$schema': 'http://json-schema.org/draft-07/schema'}, {'type': 'object', '$description': 'translations.json#/div_image_background', 'properties': {'image_url': {'$ref': 'common.json#/url', '$description': 'translations.json#/div_image_background_image_url'}, 'content_alignment_vertical': {'$ref': 'div-alignment-vertical.json', 'default_value': 'center', '$description': 'translations.json#/div_image_background_content_alignment_vertical'}, 'content_alignment_horizontal': {'$ref': 'div-alignment-horizontal.json', 'default_value': 'center', '$description': 'translations.json#/div_image_background_content_alignment_horizontal'}, 'scale': {'$ref': 'div-image-scale.json', 'default_value': 'fill', '$description': 'translations.json#/div_image_background_scale'}, 'alpha': {'type': 'number', 'default_value': '1.0', 'constraint': 'number >= 0.0 && number <= 1.0', '$description': 'translations.json#/div_image_background_alpha'}, 'preload_required': {'$ref': 'common.json#/boolean_int', 'default_value': 'false', '$description': 'translations.json#/div_image_background_preload_required', 'platforms': ['android']}, 'filters': {'type': 'array', 'items': {'$ref': 'div-filter.json'}, 'minItems': 1, '$description': 'translations.json#/div_filter'}, 'type': {'type': 'string', 'enum': ['image']}}, 'required': ['image_url', 'type'], '$schema': 'http://json-schema.org/draft-07/schema'}, {'type': 'object', '$description': 'translations.json#/div_solid_background', 'codegen': {'divan': {'forced_properties_order': ['color']}}, 'properties': {'color': {'$ref': 'common.json#/color', '$description': 'translations.json#/div_solid_background_color'}, 'type': {'type': 'string', 'enum': ['solid']}}, 'required': ['color', 'type'], '$schema': 'http://json-schema.org/draft-07/schema'}, {'type': 'object', '$description': 'translations.json#/div_nine_patch_background', 'properties': {'image_url': {'$ref': 'common.json#/url', '$description': 'translations.json#/div_image_background_image_url'}, 'insets': {'$ref': 'div-absolute-edge-insets.json', '$description': 'translations.json#/div_nine_patch_background_insets'}, 'type': {'type': 'string', 'enum': ['nine_patch_image']}}, 'required': ['image_url', 'type', 'insets'], '$schema': 'http://json-schema.org/draft-07/schema'}], '$schema': 'http://json-schema.org/draft-07/schema'}, rule='anyOf')
 return data

def validate_div_nine_patch_background_json(data, custom_formats={}, name_prefix=None):
 if not isinstance(data, (dict)):
  if not (isinstance(data, str) and '@' in data):
   raise JsonSchemaValueException("" + (name_prefix or "data") + " must be object", value=data, name="" + (name_prefix or "data") + "", definition={'type': 'object', '$description': 'translations.json#/div_nine_patch_background', 'properties': {'image_url': {'type': 'string', 'format': 'uri'}, 'insets': {'type': 'object', '$description': 'translations.json#/div_absolute_edge_insets', 'properties': {'left': {'$ref': 'common.json#/non_negative_integer', 'default_value': '0', '$description': 'translations.json#/div_edge_insets_left'}, 'right': {'$ref': 'common.json#/non_negative_integer', 'default_value': '0', '$description': 'translations.json#/div_edge_insets_right'}, 'top': {'$ref': 'common.json#/non_negative_integer', 'default_value': '0', '$description': 'translations.json#/div_edge_insets_top'}, 'bottom': {'$ref': 'common.json#/non_negative_integer', 'default_value': '0', '$description': 'translations.json#/div_edge_insets_bottom'}}, '$schema': 'http://json-schema.org/draft-07/schema'}, 'type': {'type': 'string', 'enum': ['nine_patch_image']}}, 'required': ['image_url', 'type', 'insets'], '$schema': 'http://json-schema.org/draft-07/schema'}, rule='type')
 data_is_dict = isinstance(data, dict)
 if data_is_dict:
  data__missing_keys = set(['image_url', 'type', 'insets']) - data.keys()
  if data__missing_keys:
   if not (isinstance(data, str) and '@' in data):
    raise JsonSchemaValueException("" + (name_prefix or "data") + " must contain " + (str(sorted(data__missing_keys)) + " properties"), value=data, name="" + (name_prefix or "data") + "", definition={'type': 'object', '$description': 'translations.json#/div_nine_patch_background', 'properties': {'image_url': {'type': 'string', 'format': 'uri'}, 'insets': {'type': 'object', '$description': 'translations.json#/div_absolute_edge_insets', 'properties': {'left': {'$ref': 'common.json#/non_negative_integer', 'default_value': '0', '$description': 'translations.json#/div_edge_insets_left'}, 'right': {'$ref': 'common.json#/non_negative_integer', 'default_value': '0', '$description': 'translations.json#/div_edge_insets_right'}, 'top': {'$ref': 'common.json#/non_negative_integer', 'default_value': '0', '$description': 'translations.json#/div_edge_insets_top'}, 'bottom': {'$ref': 'common.json#/non_negative_integer', 'default_value': '0', '$description': 'translations.json#/div_edge_insets_bottom'}}, '$schema': 'http://json-schema.org/draft-07/schema'}, 'type': {'type': 'string', 'enum': ['nine_patch_image']}}, 'required': ['image_url', 'type', 'insets'], '$schema': 'http://json-schema.org/draft-07/schema'}, rule='required')
  data_keys = set(data.keys())
  if "image_url" in data_keys:
   data_keys.remove("image_url")
   data__imageurl = data["image_url"]
   validate_common_json__url(data__imageurl, custom_formats, (name_prefix or "data") + ".image_url")
  if "insets" in data_keys:
   data_keys.remove("insets")
   data__insets = data["insets"]
   validate_div_absolute_edge_insets_json(data__insets, custom_formats, (name_prefix or "data") + ".insets")
  if "type" in data_keys:
   data_keys.remove("type")
   data__type = data["type"]
   if not isinstance(data__type, (str)):
    if not (isinstance(data__type, str) and '@' in data__type):
     raise JsonSchemaValueException("" + (name_prefix or "data") + ".type must be string", value=data__type, name="" + (name_prefix or "data") + ".type", definition={'type': 'string', 'enum': ['nine_patch_image']}, rule='type')
   if data__type not in ['nine_patch_image']:
    if not (isinstance(data__type, str) and '@' in data__type):
     raise JsonSchemaValueException("" + (name_prefix or "data") + ".type must be one of ['nine_patch_image']", value=data__type, name="" + (name_prefix or "data") + ".type", definition={'type': 'string', 'enum': ['nine_patch_image']}, rule='enum')
 return data

def validate_div_absolute_edge_insets_json(data, custom_formats={}, name_prefix=None):
 if not isinstance(data, (dict)):
  if not (isinstance(data, str) and '@' in data):
   raise JsonSchemaValueException("" + (name_prefix or "data") + " must be object", value=data, name="" + (name_prefix or "data") + "", definition={'type': 'object', '$description': 'translations.json#/div_absolute_edge_insets', 'properties': {'left': {'type': 'integer', 'constraint': 'number >= 0'}, 'right': {'type': 'integer', 'constraint': 'number >= 0'}, 'top': {'type': 'integer', 'constraint': 'number >= 0'}, 'bottom': {'type': 'integer', 'constraint': 'number >= 0'}}, '$schema': 'http://json-schema.org/draft-07/schema'}, rule='type')
 data_is_dict = isinstance(data, dict)
 if data_is_dict:
  data_keys = set(data.keys())
  if "left" in data_keys:
   data_keys.remove("left")
   data__left = data["left"]
   validate_common_json__non_negative_integer(data__left, custom_formats, (name_prefix or "data") + ".left")
  if "right" in data_keys:
   data_keys.remove("right")
   data__right = data["right"]
   validate_common_json__non_negative_integer(data__right, custom_formats, (name_prefix or "data") + ".right")
  if "top" in data_keys:
   data_keys.remove("top")
   data__top = data["top"]
   validate_common_json__non_negative_integer(data__top, custom_formats, (name_prefix or "data") + ".top")
  if "bottom" in data_keys:
   data_keys.remove("bottom")
   data__bottom = data["bottom"]
   validate_common_json__non_negative_integer(data__bottom, custom_formats, (name_prefix or "data") + ".bottom")
 return data

def validate_div_solid_background_json(data, custom_formats={}, name_prefix=None):
 if not isinstance(data, (dict)):
  if not (isinstance(data, str) and '@' in data):
   raise JsonSchemaValueException("" + (name_prefix or "data") + " must be object", value=data, name="" + (name_prefix or "data") + "", definition={'type': 'object', '$description': 'translations.json#/div_solid_background', 'codegen': {'divan': {'forced_properties_order': ['color']}}, 'properties': {'color': {'type': 'string', 'format': 'color'}, 'type': {'type': 'string', 'enum': ['solid']}}, 'required': ['color', 'type'], '$schema': 'http://json-schema.org/draft-07/schema'}, rule='type')
 data_is_dict = isinstance(data, dict)
 if data_is_dict:
  data__missing_keys = set(['color', 'type']) - data.keys()
  if data__missing_keys:
   if not (isinstance(data, str) and '@' in data):
    raise JsonSchemaValueException("" + (name_prefix or "data") + " must contain " + (str(sorted(data__missing_keys)) + " properties"), value=data, name="" + (name_prefix or "data") + "", definition={'type': 'object', '$description': 'translations.json#/div_solid_background', 'codegen': {'divan': {'forced_properties_order': ['color']}}, 'properties': {'color': {'type': 'string', 'format': 'color'}, 'type': {'type': 'string', 'enum': ['solid']}}, 'required': ['color', 'type'], '$schema': 'http://json-schema.org/draft-07/schema'}, rule='required')
  data_keys = set(data.keys())
  if "color" in data_keys:
   data_keys.remove("color")
   data__color = data["color"]
   validate_common_json__color(data__color, custom_formats, (name_prefix or "data") + ".color")
  if "type" in data_keys:
   data_keys.remove("type")
   data__type = data["type"]
   if not isinstance(data__type, (str)):
    if not (isinstance(data__type, str) and '@' in data__type):
     raise JsonSchemaValueException("" + (name_prefix or "data") + ".type must be string", value=data__type, name="" + (name_prefix or "data") + ".type", definition={'type': 'string', 'enum': ['solid']}, rule='type')
   if data__type not in ['solid']:
    if not (isinstance(data__type, str) and '@' in data__type):
     raise JsonSchemaValueException("" + (name_prefix or "data") + ".type must be one of ['solid']", value=data__type, name="" + (name_prefix or "data") + ".type", definition={'type': 'string', 'enum': ['solid']}, rule='enum')
 return data

def validate_div_image_background_json(data, custom_formats={}, name_prefix=None):
 if not isinstance(data, (dict)):
  if not (isinstance(data, str) and '@' in data):
   raise JsonSchemaValueException("" + (name_prefix or "data") + " must be object", value=data, name="" + (name_prefix or "data") + "", definition={'type': 'object', '$description': 'translations.json#/div_image_background', 'properties': {'image_url': {'type': 'string', 'format': 'uri'}, 'content_alignment_vertical': {'type': 'string', 'enum': ['top', 'center', 'bottom', 'baseline'], '$schema': 'http://json-schema.org/draft-07/schema'}, 'content_alignment_horizontal': {'type': 'string', 'enum': ['left', 'center', 'right', 'start', 'end'], '$schema': 'http://json-schema.org/draft-07/schema'}, 'scale': {'type': 'string', 'enum': ['fill', 'no_scale', 'fit', 'stretch'], '$schema': 'http://json-schema.org/draft-07/schema'}, 'alpha': {'type': 'number', 'default_value': '1.0', 'constraint': 'number >= 0.0 && number <= 1.0', '$description': 'translations.json#/div_image_background_alpha'}, 'preload_required': {'oneOf': [{'type': 'boolean'}, {'type': 'integer', 'enum': [0, 1]}]}, 'filters': {'type': 'array', 'items': {'anyOf': [{'$ref': 'div-blur.json', '$description': 'translations.json#/div_filter'}, {'$ref': 'div-filter-rtl-mirror.json', '$description': 'translations.json#/div_filter_rtl_mirror', 'platforms': ['android']}], '$schema': 'http://json-schema.org/draft-07/schema'}, 'minItems': 1, '$description': 'translations.json#/div_filter'}, 'type': {'type': 'string', 'enum': ['image']}}, 'required': ['image_url', 'type'], '$schema': 'http://json-schema.org/draft-07/schema'}, rule='type')
 data_is_dict = isinstance(data, dict)
 if data_is_dict:
  data__missing_keys = set(['image_url', 'type']) - data.keys()
  if data__missing_keys:
   if not (isinstance(data, str) and '@' in data):
    raise JsonSchemaValueException("" + (name_prefix or "data") + " must contain " + (str(sorted(data__missing_keys)) + " properties"), value=data, name="" + (name_prefix or "data") + "", definition={'type': 'object', '$description': 'translations.json#/div_image_background', 'properties': {'image_url': {'type': 'string', 'format': 'uri'}, 'content_alignment_vertical': {'type': 'string', 'enum': ['top', 'center', 'bottom', 'baseline'], '$schema': 'http://json-schema.org/draft-07/schema'}, 'content_alignment_horizontal': {'type': 'string', 'enum': ['left', 'center', 'right', 'start', 'end'], '$schema': 'http://json-schema.org/draft-07/schema'}, 'scale': {'type': 'string', 'enum': ['fill', 'no_scale', 'fit', 'stretch'], '$schema': 'http://json-schema.org/draft-07/schema'}, 'alpha': {'type': 'number', 'default_value': '1.0', 'constraint': 'number >= 0.0 && number <= 1.0', '$description': 'translations.json#/div_image_background_alpha'}, 'preload_required': {'oneOf': [{'type': 'boolean'}, {'type': 'integer', 'enum': [0, 1]}]}, 'filters': {'type': 'array', 'items': {'anyOf': [{'$ref': 'div-blur.json', '$description': 'translations.json#/div_filter'}, {'$ref': 'div-filter-rtl-mirror.json', '$description': 'translations.json#/div_filter_rtl_mirror', 'platforms': ['android']}], '$schema': 'http://json-schema.org/draft-07/schema'}, 'minItems': 1, '$description': 'translations.json#/div_filter'}, 'type': {'type': 'string', 'enum': ['image']}}, 'required': ['image_url', 'type'], '$schema': 'http://json-schema.org/draft-07/schema'}, rule='required')
  data_keys = set(data.keys())
  if "image_url" in data_keys:
   data_keys.remove("image_url")
   data__imageurl = data["image_url"]
   validate_common_json__url(data__imageurl, custom_formats, (name_prefix or "data") + ".image_url")
  if "content_alignment_vertical" in data_keys:
   data_keys.remove("content_alignment_vertical")
   data__contentalignmentvertical = data["content_alignment_vertical"]
   validate_div_alignment_vertical_json(data__contentalignmentvertical, custom_formats, (name_prefix or "data") + ".content_alignment_vertical")
  if "content_alignment_horizontal" in data_keys:
   data_keys.remove("content_alignment_horizontal")
   data__contentalignmenthorizontal = data["content_alignment_horizontal"]
   validate_div_alignment_horizontal_json(data__contentalignmenthorizontal, custom_formats, (name_prefix or "data") + ".content_alignment_horizontal")
  if "scale" in data_keys:
   data_keys.remove("scale")
   data__scale = data["scale"]
   validate_div_image_scale_json(data__scale, custom_formats, (name_prefix or "data") + ".scale")
  if "alpha" in data_keys:
   data_keys.remove("alpha")
   data__alpha = data["alpha"]
   if not isinstance(data__alpha, (int, float, Decimal)) or isinstance(data__alpha, bool):
    if not (isinstance(data__alpha, str) and '@' in data__alpha):
     raise JsonSchemaValueException("" + (name_prefix or "data") + ".alpha must be number", value=data__alpha, name="" + (name_prefix or "data") + ".alpha", definition={'type': 'number', 'default_value': '1.0', 'constraint': 'number >= 0.0 && number <= 1.0', '$description': 'translations.json#/div_image_background_alpha'}, rule='type')
  if "preload_required" in data_keys:
   data_keys.remove("preload_required")
   data__preloadrequired = data["preload_required"]
   validate_common_json__boolean_int(data__preloadrequired, custom_formats, (name_prefix or "data") + ".preload_required")
  if "filters" in data_keys:
   data_keys.remove("filters")
   data__filters = data["filters"]
   if not isinstance(data__filters, (list, tuple)):
    if not (isinstance(data__filters, str) and '@' in data__filters):
     raise JsonSchemaValueException("" + (name_prefix or "data") + ".filters must be array", value=data__filters, name="" + (name_prefix or "data") + ".filters", definition={'type': 'array', 'items': {'anyOf': [{'$ref': 'div-blur.json', '$description': 'translations.json#/div_filter'}, {'$ref': 'div-filter-rtl-mirror.json', '$description': 'translations.json#/div_filter_rtl_mirror', 'platforms': ['android']}], '$schema': 'http://json-schema.org/draft-07/schema'}, 'minItems': 1, '$description': 'translations.json#/div_filter'}, rule='type')
   data__filters_is_list = isinstance(data__filters, (list, tuple))
   if data__filters_is_list:
    data__filters_len = len(data__filters)
    if data__filters_len < 1:
     if not (isinstance(data__filters, str) and '@' in data__filters):
      raise JsonSchemaValueException("" + (name_prefix or "data") + ".filters must contain at least 1 items", value=data__filters, name="" + (name_prefix or "data") + ".filters", definition={'type': 'array', 'items': {'anyOf': [{'$ref': 'div-blur.json', '$description': 'translations.json#/div_filter'}, {'$ref': 'div-filter-rtl-mirror.json', '$description': 'translations.json#/div_filter_rtl_mirror', 'platforms': ['android']}], '$schema': 'http://json-schema.org/draft-07/schema'}, 'minItems': 1, '$description': 'translations.json#/div_filter'}, rule='minItems')
    for data__filters_x, data__filters_item in enumerate(data__filters):
     validate_div_filter_json(data__filters_item, custom_formats, (name_prefix or "data") + ".filters[{data__filters_x}]".format(**locals()))
  if "type" in data_keys:
   data_keys.remove("type")
   data__type = data["type"]
   if not isinstance(data__type, (str)):
    if not (isinstance(data__type, str) and '@' in data__type):
     raise JsonSchemaValueException("" + (name_prefix or "data") + ".type must be string", value=data__type, name="" + (name_prefix or "data") + ".type", definition={'type': 'string', 'enum': ['image']}, rule='type')
   if data__type not in ['image']:
    if not (isinstance(data__type, str) and '@' in data__type):
     raise JsonSchemaValueException("" + (name_prefix or "data") + ".type must be one of ['image']", value=data__type, name="" + (name_prefix or "data") + ".type", definition={'type': 'string', 'enum': ['image']}, rule='enum')
 return data

def validate_div_filter_json(data, custom_formats={}, name_prefix=None):
 data_any_of_count11 = 0
 if not data_any_of_count11:
  try:
   validate_div_blur_json(data, custom_formats, (name_prefix or "data") + "")
   data_any_of_count11 += 1
  except JsonSchemaValueException: pass
 if not data_any_of_count11:
  try:
   validate_div_filter_rtl_mirror_json(data, custom_formats, (name_prefix or "data") + "")
   data_any_of_count11 += 1
  except JsonSchemaValueException: pass
 if not data_any_of_count11:
  if not (isinstance(data, str) and '@' in data):
   raise JsonSchemaValueException("" + (name_prefix or "data") + " cannot be validated by any definition", value=data, name="" + (name_prefix or "data") + "", definition={'anyOf': [{'type': 'object', '$description': 'translations.json#/div_blur', 'properties': {'radius': {'$ref': 'common.json#/non_negative_integer', '$description': 'translations.json#/div_blur_radius'}, 'type': {'type': 'string', 'enum': ['blur']}}, 'required': ['radius', 'type'], '$schema': 'http://json-schema.org/draft-07/schema'}, {'type': 'object', '$description': 'translations.json#/div_filter_rtl_mirror', 'properties': {'type': {'type': 'string', 'enum': ['rtl_mirror']}}, 'required': ['type'], '$schema': 'http://json-schema.org/draft-07/schema'}], '$schema': 'http://json-schema.org/draft-07/schema'}, rule='anyOf')
 return data

def validate_div_filter_rtl_mirror_json(data, custom_formats={}, name_prefix=None):
 if not isinstance(data, (dict)):
  if not (isinstance(data, str) and '@' in data):
   raise JsonSchemaValueException("" + (name_prefix or "data") + " must be object", value=data, name="" + (name_prefix or "data") + "", definition={'type': 'object', '$description': 'translations.json#/div_filter_rtl_mirror', 'properties': {'type': {'type': 'string', 'enum': ['rtl_mirror']}}, 'required': ['type'], '$schema': 'http://json-schema.org/draft-07/schema'}, rule='type')
 data_is_dict = isinstance(data, dict)
 if data_is_dict:
  data__missing_keys = set(['type']) - data.keys()
  if data__missing_keys:
   if not (isinstance(data, str) and '@' in data):
    raise JsonSchemaValueException("" + (name_prefix or "data") + " must contain " + (str(sorted(data__missing_keys)) + " properties"), value=data, name="" + (name_prefix or "data") + "", definition={'type': 'object', '$description': 'translations.json#/div_filter_rtl_mirror', 'properties': {'type': {'type': 'string', 'enum': ['rtl_mirror']}}, 'required': ['type'], '$schema': 'http://json-schema.org/draft-07/schema'}, rule='required')
  data_keys = set(data.keys())
  if "type" in data_keys:
   data_keys.remove("type")
   data__type = data["type"]
   if not isinstance(data__type, (str)):
    if not (isinstance(data__type, str) and '@' in data__type):
     raise JsonSchemaValueException("" + (name_prefix or "data") + ".type must be string", value=data__type, name="" + (name_prefix or "data") + ".type", definition={'type': 'string', 'enum': ['rtl_mirror']}, rule='type')
   if data__type not in ['rtl_mirror']:
    if not (isinstance(data__type, str) and '@' in data__type):
     raise JsonSchemaValueException("" + (name_prefix or "data") + ".type must be one of ['rtl_mirror']", value=data__type, name="" + (name_prefix or "data") + ".type", definition={'type': 'string', 'enum': ['rtl_mirror']}, rule='enum')
 return data

def validate_div_blur_json(data, custom_formats={}, name_prefix=None):
 if not isinstance(data, (dict)):
  if not (isinstance(data, str) and '@' in data):
   raise JsonSchemaValueException("" + (name_prefix or "data") + " must be object", value=data, name="" + (name_prefix or "data") + "", definition={'type': 'object', '$description': 'translations.json#/div_blur', 'properties': {'radius': {'type': 'integer', 'constraint': 'number >= 0'}, 'type': {'type': 'string', 'enum': ['blur']}}, 'required': ['radius', 'type'], '$schema': 'http://json-schema.org/draft-07/schema'}, rule='type')
 data_is_dict = isinstance(data, dict)
 if data_is_dict:
  data__missing_keys = set(['radius', 'type']) - data.keys()
  if data__missing_keys:
   if not (isinstance(data, str) and '@' in data):
    raise JsonSchemaValueException("" + (name_prefix or "data") + " must contain " + (str(sorted(data__missing_keys)) + " properties"), value=data, name="" + (name_prefix or "data") + "", definition={'type': 'object', '$description': 'translations.json#/div_blur', 'properties': {'radius': {'type': 'integer', 'constraint': 'number >= 0'}, 'type': {'type': 'string', 'enum': ['blur']}}, 'required': ['radius', 'type'], '$schema': 'http://json-schema.org/draft-07/schema'}, rule='required')
  data_keys = set(data.keys())
  if "radius" in data_keys:
   data_keys.remove("radius")
   data__radius = data["radius"]
   validate_common_json__non_negative_integer(data__radius, custom_formats, (name_prefix or "data") + ".radius")
  if "type" in data_keys:
   data_keys.remove("type")
   data__type = data["type"]
   if not isinstance(data__type, (str)):
    if not (isinstance(data__type, str) and '@' in data__type):
     raise JsonSchemaValueException("" + (name_prefix or "data") + ".type must be string", value=data__type, name="" + (name_prefix or "data") + ".type", definition={'type': 'string', 'enum': ['blur']}, rule='type')
   if data__type not in ['blur']:
    if not (isinstance(data__type, str) and '@' in data__type):
     raise JsonSchemaValueException("" + (name_prefix or "data") + ".type must be one of ['blur']", value=data__type, name="" + (name_prefix or "data") + ".type", definition={'type': 'string', 'enum': ['blur']}, rule='enum')
 return data

def validate_div_image_scale_json(data, custom_formats={}, name_prefix=None):
 if not isinstance(data, (str)):
  if not (isinstance(data, str) and '@' in data):
   raise JsonSchemaValueException("" + (name_prefix or "data") + " must be string", value=data, name="" + (name_prefix or "data") + "", definition={'type': 'string', 'enum': ['fill', 'no_scale', 'fit', 'stretch'], '$schema': 'http://json-schema.org/draft-07/schema'}, rule='type')
 if data not in ['fill', 'no_scale', 'fit', 'stretch']:
  if not (isinstance(data, str) and '@' in data):
   raise JsonSchemaValueException("" + (name_prefix or "data") + " must be one of ['fill', 'no_scale', 'fit', 'stretch']", value=data, name="" + (name_prefix or "data") + "", definition={'type': 'string', 'enum': ['fill', 'no_scale', 'fit', 'stretch'], '$schema': 'http://json-schema.org/draft-07/schema'}, rule='enum')
 return data

def validate_div_radial_gradient_json(data, custom_formats={}, name_prefix=None):
 if not isinstance(data, (dict)):
  if not (isinstance(data, str) and '@' in data):
   raise JsonSchemaValueException("" + (name_prefix or "data") + " must be object", value=data, name="" + (name_prefix or "data") + "", definition={'type': 'object', '$description': 'translations.json#/div_gradient_radial', 'properties': {'colors': {'type': 'array', 'items': {'type': 'string', 'format': 'color'}, 'minItems': 2, '$description': 'translations.json#/div_gradient_colors'}, 'radius': {'anyOf': [{'$ref': 'div-fixed-size.json', '$description': 'translations.json#/div_size_fixed'}, {'$ref': 'div-radial-gradient-relative-radius.json', '$description': 'translations.json#/div_radial_gradient_relative_radius'}], '$schema': 'http://json-schema.org/draft-07/schema'}, 'center_x': {'anyOf': [{'$ref': 'div-radial-gradient-fixed-center.json', '$description': 'translations.json#/div_radial_gradient_fixed_center'}, {'$ref': 'div-radial-gradient-relative-center.json', '$description': 'translations.json#/div_radial_gradient_relative_center'}], '$schema': 'http://json-schema.org/draft-07/schema'}, 'center_y': {'anyOf': [{'$ref': 'div-radial-gradient-fixed-center.json', '$description': 'translations.json#/div_radial_gradient_fixed_center'}, {'$ref': 'div-radial-gradient-relative-center.json', '$description': 'translations.json#/div_radial_gradient_relative_center'}], '$schema': 'http://json-schema.org/draft-07/schema'}, 'type': {'type': 'string', 'enum': ['radial_gradient']}}, 'required': ['colors', 'type'], '$schema': 'http://json-schema.org/draft-07/schema'}, rule='type')
 data_is_dict = isinstance(data, dict)
 if data_is_dict:
  data__missing_keys = set(['colors', 'type']) - data.keys()
  if data__missing_keys:
   if not (isinstance(data, str) and '@' in data):
    raise JsonSchemaValueException("" + (name_prefix or "data") + " must contain " + (str(sorted(data__missing_keys)) + " properties"), value=data, name="" + (name_prefix or "data") + "", definition={'type': 'object', '$description': 'translations.json#/div_gradient_radial', 'properties': {'colors': {'type': 'array', 'items': {'type': 'string', 'format': 'color'}, 'minItems': 2, '$description': 'translations.json#/div_gradient_colors'}, 'radius': {'anyOf': [{'$ref': 'div-fixed-size.json', '$description': 'translations.json#/div_size_fixed'}, {'$ref': 'div-radial-gradient-relative-radius.json', '$description': 'translations.json#/div_radial_gradient_relative_radius'}], '$schema': 'http://json-schema.org/draft-07/schema'}, 'center_x': {'anyOf': [{'$ref': 'div-radial-gradient-fixed-center.json', '$description': 'translations.json#/div_radial_gradient_fixed_center'}, {'$ref': 'div-radial-gradient-relative-center.json', '$description': 'translations.json#/div_radial_gradient_relative_center'}], '$schema': 'http://json-schema.org/draft-07/schema'}, 'center_y': {'anyOf': [{'$ref': 'div-radial-gradient-fixed-center.json', '$description': 'translations.json#/div_radial_gradient_fixed_center'}, {'$ref': 'div-radial-gradient-relative-center.json', '$description': 'translations.json#/div_radial_gradient_relative_center'}], '$schema': 'http://json-schema.org/draft-07/schema'}, 'type': {'type': 'string', 'enum': ['radial_gradient']}}, 'required': ['colors', 'type'], '$schema': 'http://json-schema.org/draft-07/schema'}, rule='required')
  data_keys = set(data.keys())
  if "colors" in data_keys:
   data_keys.remove("colors")
   data__colors = data["colors"]
   if not isinstance(data__colors, (list, tuple)):
    if not (isinstance(data__colors, str) and '@' in data__colors):
     raise JsonSchemaValueException("" + (name_prefix or "data") + ".colors must be array", value=data__colors, name="" + (name_prefix or "data") + ".colors", definition={'type': 'array', 'items': {'type': 'string', 'format': 'color'}, 'minItems': 2, '$description': 'translations.json#/div_gradient_colors'}, rule='type')
   data__colors_is_list = isinstance(data__colors, (list, tuple))
   if data__colors_is_list:
    data__colors_len = len(data__colors)
    if data__colors_len < 2:
     if not (isinstance(data__colors, str) and '@' in data__colors):
      raise JsonSchemaValueException("" + (name_prefix or "data") + ".colors must contain at least 2 items", value=data__colors, name="" + (name_prefix or "data") + ".colors", definition={'type': 'array', 'items': {'type': 'string', 'format': 'color'}, 'minItems': 2, '$description': 'translations.json#/div_gradient_colors'}, rule='minItems')
    for data__colors_x, data__colors_item in enumerate(data__colors):
     validate_common_json__color(data__colors_item, custom_formats, (name_prefix or "data") + ".colors[{data__colors_x}]".format(**locals()))
  if "radius" in data_keys:
   data_keys.remove("radius")
   data__radius = data["radius"]
   validate_div_radial_gradient_radius_json(data__radius, custom_formats, (name_prefix or "data") + ".radius")
  if "center_x" in data_keys:
   data_keys.remove("center_x")
   data__centerx = data["center_x"]
   validate_div_radial_gradient_center_json(data__centerx, custom_formats, (name_prefix or "data") + ".center_x")
  if "center_y" in data_keys:
   data_keys.remove("center_y")
   data__centery = data["center_y"]
   validate_div_radial_gradient_center_json(data__centery, custom_formats, (name_prefix or "data") + ".center_y")
  if "type" in data_keys:
   data_keys.remove("type")
   data__type = data["type"]
   if not isinstance(data__type, (str)):
    if not (isinstance(data__type, str) and '@' in data__type):
     raise JsonSchemaValueException("" + (name_prefix or "data") + ".type must be string", value=data__type, name="" + (name_prefix or "data") + ".type", definition={'type': 'string', 'enum': ['radial_gradient']}, rule='type')
   if data__type not in ['radial_gradient']:
    if not (isinstance(data__type, str) and '@' in data__type):
     raise JsonSchemaValueException("" + (name_prefix or "data") + ".type must be one of ['radial_gradient']", value=data__type, name="" + (name_prefix or "data") + ".type", definition={'type': 'string', 'enum': ['radial_gradient']}, rule='enum')
 return data

def validate_div_radial_gradient_center_json(data, custom_formats={}, name_prefix=None):
 data_any_of_count12 = 0
 if not data_any_of_count12:
  try:
   validate_div_radial_gradient_fixed_center_json(data, custom_formats, (name_prefix or "data") + "")
   data_any_of_count12 += 1
  except JsonSchemaValueException: pass
 if not data_any_of_count12:
  try:
   validate_div_radial_gradient_relative_center_json(data, custom_formats, (name_prefix or "data") + "")
   data_any_of_count12 += 1
  except JsonSchemaValueException: pass
 if not data_any_of_count12:
  if not (isinstance(data, str) and '@' in data):
   raise JsonSchemaValueException("" + (name_prefix or "data") + " cannot be validated by any definition", value=data, name="" + (name_prefix or "data") + "", definition={'anyOf': [{'type': 'object', '$description': 'translations.json#/div_radial_gradient_fixed_center', 'properties': {'value': {'type': 'integer', '$description': 'translations.json#/div_radial_gradient_fixed_center_value'}, 'unit': {'$ref': 'div-size-unit.json', '$description': 'translations.json#/div_fixed_size_unit', 'default_value': 'dp'}, 'type': {'type': 'string', 'enum': ['fixed']}}, 'required': ['value', 'type'], '$schema': 'http://json-schema.org/draft-07/schema'}, {'type': 'object', '$description': 'translations.json#/div_radial_gradient_relative_center', 'properties': {'value': {'type': 'number', '$description': 'translations.json#/div_radial_gradient_relative_center_value'}, 'type': {'type': 'string', 'enum': ['relative']}}, 'required': ['value', 'type'], '$schema': 'http://json-schema.org/draft-07/schema'}], '$schema': 'http://json-schema.org/draft-07/schema'}, rule='anyOf')
 return data

def validate_div_radial_gradient_relative_center_json(data, custom_formats={}, name_prefix=None):
 if not isinstance(data, (dict)):
  if not (isinstance(data, str) and '@' in data):
   raise JsonSchemaValueException("" + (name_prefix or "data") + " must be object", value=data, name="" + (name_prefix or "data") + "", definition={'type': 'object', '$description': 'translations.json#/div_radial_gradient_relative_center', 'properties': {'value': {'type': 'number', '$description': 'translations.json#/div_radial_gradient_relative_center_value'}, 'type': {'type': 'string', 'enum': ['relative']}}, 'required': ['value', 'type'], '$schema': 'http://json-schema.org/draft-07/schema'}, rule='type')
 data_is_dict = isinstance(data, dict)
 if data_is_dict:
  data__missing_keys = set(['value', 'type']) - data.keys()
  if data__missing_keys:
   if not (isinstance(data, str) and '@' in data):
    raise JsonSchemaValueException("" + (name_prefix or "data") + " must contain " + (str(sorted(data__missing_keys)) + " properties"), value=data, name="" + (name_prefix or "data") + "", definition={'type': 'object', '$description': 'translations.json#/div_radial_gradient_relative_center', 'properties': {'value': {'type': 'number', '$description': 'translations.json#/div_radial_gradient_relative_center_value'}, 'type': {'type': 'string', 'enum': ['relative']}}, 'required': ['value', 'type'], '$schema': 'http://json-schema.org/draft-07/schema'}, rule='required')
  data_keys = set(data.keys())
  if "value" in data_keys:
   data_keys.remove("value")
   data__value = data["value"]
   if not isinstance(data__value, (int, float, Decimal)) or isinstance(data__value, bool):
    if not (isinstance(data__value, str) and '@' in data__value):
     raise JsonSchemaValueException("" + (name_prefix or "data") + ".value must be number", value=data__value, name="" + (name_prefix or "data") + ".value", definition={'type': 'number', '$description': 'translations.json#/div_radial_gradient_relative_center_value'}, rule='type')
  if "type" in data_keys:
   data_keys.remove("type")
   data__type = data["type"]
   if not isinstance(data__type, (str)):
    if not (isinstance(data__type, str) and '@' in data__type):
     raise JsonSchemaValueException("" + (name_prefix or "data") + ".type must be string", value=data__type, name="" + (name_prefix or "data") + ".type", definition={'type': 'string', 'enum': ['relative']}, rule='type')
   if data__type not in ['relative']:
    if not (isinstance(data__type, str) and '@' in data__type):
     raise JsonSchemaValueException("" + (name_prefix or "data") + ".type must be one of ['relative']", value=data__type, name="" + (name_prefix or "data") + ".type", definition={'type': 'string', 'enum': ['relative']}, rule='enum')
 return data

def validate_div_radial_gradient_fixed_center_json(data, custom_formats={}, name_prefix=None):
 if not isinstance(data, (dict)):
  if not (isinstance(data, str) and '@' in data):
   raise JsonSchemaValueException("" + (name_prefix or "data") + " must be object", value=data, name="" + (name_prefix or "data") + "", definition={'type': 'object', '$description': 'translations.json#/div_radial_gradient_fixed_center', 'properties': {'value': {'type': 'integer', '$description': 'translations.json#/div_radial_gradient_fixed_center_value'}, 'unit': {'type': 'string', 'enum': ['dp', 'sp', 'px'], '$description': 'translations.json#/div_size_unit', 'platforms': ['android', 'ios'], '$schema': 'http://json-schema.org/draft-07/schema'}, 'type': {'type': 'string', 'enum': ['fixed']}}, 'required': ['value', 'type'], '$schema': 'http://json-schema.org/draft-07/schema'}, rule='type')
 data_is_dict = isinstance(data, dict)
 if data_is_dict:
  data__missing_keys = set(['value', 'type']) - data.keys()
  if data__missing_keys:
   if not (isinstance(data, str) and '@' in data):
    raise JsonSchemaValueException("" + (name_prefix or "data") + " must contain " + (str(sorted(data__missing_keys)) + " properties"), value=data, name="" + (name_prefix or "data") + "", definition={'type': 'object', '$description': 'translations.json#/div_radial_gradient_fixed_center', 'properties': {'value': {'type': 'integer', '$description': 'translations.json#/div_radial_gradient_fixed_center_value'}, 'unit': {'type': 'string', 'enum': ['dp', 'sp', 'px'], '$description': 'translations.json#/div_size_unit', 'platforms': ['android', 'ios'], '$schema': 'http://json-schema.org/draft-07/schema'}, 'type': {'type': 'string', 'enum': ['fixed']}}, 'required': ['value', 'type'], '$schema': 'http://json-schema.org/draft-07/schema'}, rule='required')
  data_keys = set(data.keys())
  if "value" in data_keys:
   data_keys.remove("value")
   data__value = data["value"]
   if not isinstance(data__value, (int)) and not (isinstance(data__value, float) and data__value.is_integer()) or isinstance(data__value, bool):
    if not (isinstance(data__value, str) and '@' in data__value):
     raise JsonSchemaValueException("" + (name_prefix or "data") + ".value must be integer", value=data__value, name="" + (name_prefix or "data") + ".value", definition={'type': 'integer', '$description': 'translations.json#/div_radial_gradient_fixed_center_value'}, rule='type')
  if "unit" in data_keys:
   data_keys.remove("unit")
   data__unit = data["unit"]
   validate_div_size_unit_json(data__unit, custom_formats, (name_prefix or "data") + ".unit")
  if "type" in data_keys:
   data_keys.remove("type")
   data__type = data["type"]
   if not isinstance(data__type, (str)):
    if not (isinstance(data__type, str) and '@' in data__type):
     raise JsonSchemaValueException("" + (name_prefix or "data") + ".type must be string", value=data__type, name="" + (name_prefix or "data") + ".type", definition={'type': 'string', 'enum': ['fixed']}, rule='type')
   if data__type not in ['fixed']:
    if not (isinstance(data__type, str) and '@' in data__type):
     raise JsonSchemaValueException("" + (name_prefix or "data") + ".type must be one of ['fixed']", value=data__type, name="" + (name_prefix or "data") + ".type", definition={'type': 'string', 'enum': ['fixed']}, rule='enum')
 return data

def validate_div_radial_gradient_radius_json(data, custom_formats={}, name_prefix=None):
 data_any_of_count13 = 0
 if not data_any_of_count13:
  try:
   validate_div_fixed_size_json(data, custom_formats, (name_prefix or "data") + "")
   data_any_of_count13 += 1
  except JsonSchemaValueException: pass
 if not data_any_of_count13:
  try:
   validate_div_radial_gradient_relative_radius_json(data, custom_formats, (name_prefix or "data") + "")
   data_any_of_count13 += 1
  except JsonSchemaValueException: pass
 if not data_any_of_count13:
  if not (isinstance(data, str) and '@' in data):
   raise JsonSchemaValueException("" + (name_prefix or "data") + " cannot be validated by any definition", value=data, name="" + (name_prefix or "data") + "", definition={'anyOf': [{'type': 'object', '$description': 'translations.json#/div_fixed_size', 'codegen': {'divan': {'forced_properties_order': ['value']}}, 'properties': {'value': {'$ref': 'common.json#/non_negative_integer', '$description': 'translations.json#/div_fixed_size_value'}, 'unit': {'$ref': 'div-size-unit.json', '$description': 'translations.json#/div_fixed_size_unit', 'default_value': 'dp'}, 'type': {'type': 'string', 'enum': ['fixed']}}, 'required': ['value', 'type'], '$schema': 'http://json-schema.org/draft-07/schema'}, {'type': 'object', '$description': 'translations.json#/div_radial_gradient_relative_radius', 'properties': {'value': {'type': 'string', '$description': 'translations.json#/div_radial_gradient_relative_radius_value', 'enum': ['nearest_corner', 'farthest_corner', 'nearest_side', 'farthest_side']}, 'type': {'type': 'string', 'enum': ['relative']}}, 'required': ['value', 'type'], '$schema': 'http://json-schema.org/draft-07/schema'}], '$schema': 'http://json-schema.org/draft-07/schema'}, rule='anyOf')
 return data

def validate_div_radial_gradient_relative_radius_json(data, custom_formats={}, name_prefix=None):
 if not isinstance(data, (dict)):
  if not (isinstance(data, str) and '@' in data):
   raise JsonSchemaValueException("" + (name_prefix or "data") + " must be object", value=data, name="" + (name_prefix or "data") + "", definition={'type': 'object', '$description': 'translations.json#/div_radial_gradient_relative_radius', 'properties': {'value': {'type': 'string', '$description': 'translations.json#/div_radial_gradient_relative_radius_value', 'enum': ['nearest_corner', 'farthest_corner', 'nearest_side', 'farthest_side']}, 'type': {'type': 'string', 'enum': ['relative']}}, 'required': ['value', 'type'], '$schema': 'http://json-schema.org/draft-07/schema'}, rule='type')
 data_is_dict = isinstance(data, dict)
 if data_is_dict:
  data__missing_keys = set(['value', 'type']) - data.keys()
  if data__missing_keys:
   if not (isinstance(data, str) and '@' in data):
    raise JsonSchemaValueException("" + (name_prefix or "data") + " must contain " + (str(sorted(data__missing_keys)) + " properties"), value=data, name="" + (name_prefix or "data") + "", definition={'type': 'object', '$description': 'translations.json#/div_radial_gradient_relative_radius', 'properties': {'value': {'type': 'string', '$description': 'translations.json#/div_radial_gradient_relative_radius_value', 'enum': ['nearest_corner', 'farthest_corner', 'nearest_side', 'farthest_side']}, 'type': {'type': 'string', 'enum': ['relative']}}, 'required': ['value', 'type'], '$schema': 'http://json-schema.org/draft-07/schema'}, rule='required')
  data_keys = set(data.keys())
  if "value" in data_keys:
   data_keys.remove("value")
   data__value = data["value"]
   if not isinstance(data__value, (str)):
    if not (isinstance(data__value, str) and '@' in data__value):
     raise JsonSchemaValueException("" + (name_prefix or "data") + ".value must be string", value=data__value, name="" + (name_prefix or "data") + ".value", definition={'type': 'string', '$description': 'translations.json#/div_radial_gradient_relative_radius_value', 'enum': ['nearest_corner', 'farthest_corner', 'nearest_side', 'farthest_side']}, rule='type')
   if data__value not in ['nearest_corner', 'farthest_corner', 'nearest_side', 'farthest_side']:
    if not (isinstance(data__value, str) and '@' in data__value):
     raise JsonSchemaValueException("" + (name_prefix or "data") + ".value must be one of ['nearest_corner', 'farthest_corner', 'nearest_side', 'farthest_side']", value=data__value, name="" + (name_prefix or "data") + ".value", definition={'type': 'string', '$description': 'translations.json#/div_radial_gradient_relative_radius_value', 'enum': ['nearest_corner', 'farthest_corner', 'nearest_side', 'farthest_side']}, rule='enum')
  if "type" in data_keys:
   data_keys.remove("type")
   data__type = data["type"]
   if not isinstance(data__type, (str)):
    if not (isinstance(data__type, str) and '@' in data__type):
     raise JsonSchemaValueException("" + (name_prefix or "data") + ".type must be string", value=data__type, name="" + (name_prefix or "data") + ".type", definition={'type': 'string', 'enum': ['relative']}, rule='type')
   if data__type not in ['relative']:
    if not (isinstance(data__type, str) and '@' in data__type):
     raise JsonSchemaValueException("" + (name_prefix or "data") + ".type must be one of ['relative']", value=data__type, name="" + (name_prefix or "data") + ".type", definition={'type': 'string', 'enum': ['relative']}, rule='enum')
 return data

def validate_div_fixed_size_json(data, custom_formats={}, name_prefix=None):
 if not isinstance(data, (dict)):
  if not (isinstance(data, str) and '@' in data):
   raise JsonSchemaValueException("" + (name_prefix or "data") + " must be object", value=data, name="" + (name_prefix or "data") + "", definition={'type': 'object', '$description': 'translations.json#/div_fixed_size', 'codegen': {'divan': {'forced_properties_order': ['value']}}, 'properties': {'value': {'type': 'integer', 'constraint': 'number >= 0'}, 'unit': {'type': 'string', 'enum': ['dp', 'sp', 'px'], '$description': 'translations.json#/div_size_unit', 'platforms': ['android', 'ios'], '$schema': 'http://json-schema.org/draft-07/schema'}, 'type': {'type': 'string', 'enum': ['fixed']}}, 'required': ['value', 'type'], '$schema': 'http://json-schema.org/draft-07/schema'}, rule='type')
 data_is_dict = isinstance(data, dict)
 if data_is_dict:
  data__missing_keys = set(['value', 'type']) - data.keys()
  if data__missing_keys:
   if not (isinstance(data, str) and '@' in data):
    raise JsonSchemaValueException("" + (name_prefix or "data") + " must contain " + (str(sorted(data__missing_keys)) + " properties"), value=data, name="" + (name_prefix or "data") + "", definition={'type': 'object', '$description': 'translations.json#/div_fixed_size', 'codegen': {'divan': {'forced_properties_order': ['value']}}, 'properties': {'value': {'type': 'integer', 'constraint': 'number >= 0'}, 'unit': {'type': 'string', 'enum': ['dp', 'sp', 'px'], '$description': 'translations.json#/div_size_unit', 'platforms': ['android', 'ios'], '$schema': 'http://json-schema.org/draft-07/schema'}, 'type': {'type': 'string', 'enum': ['fixed']}}, 'required': ['value', 'type'], '$schema': 'http://json-schema.org/draft-07/schema'}, rule='required')
  data_keys = set(data.keys())
  if "value" in data_keys:
   data_keys.remove("value")
   data__value = data["value"]
   validate_common_json__non_negative_integer(data__value, custom_formats, (name_prefix or "data") + ".value")
  if "unit" in data_keys:
   data_keys.remove("unit")
   data__unit = data["unit"]
   validate_div_size_unit_json(data__unit, custom_formats, (name_prefix or "data") + ".unit")
  if "type" in data_keys:
   data_keys.remove("type")
   data__type = data["type"]
   if not isinstance(data__type, (str)):
    if not (isinstance(data__type, str) and '@' in data__type):
     raise JsonSchemaValueException("" + (name_prefix or "data") + ".type must be string", value=data__type, name="" + (name_prefix or "data") + ".type", definition={'type': 'string', 'enum': ['fixed']}, rule='type')
   if data__type not in ['fixed']:
    if not (isinstance(data__type, str) and '@' in data__type):
     raise JsonSchemaValueException("" + (name_prefix or "data") + ".type must be one of ['fixed']", value=data__type, name="" + (name_prefix or "data") + ".type", definition={'type': 'string', 'enum': ['fixed']}, rule='enum')
 return data

def validate_div_linear_gradient_json(data, custom_formats={}, name_prefix=None):
 if not isinstance(data, (dict)):
  if not (isinstance(data, str) and '@' in data):
   raise JsonSchemaValueException("" + (name_prefix or "data") + " must be object", value=data, name="" + (name_prefix or "data") + "", definition={'type': 'object', '$description': 'translations.json#/div_gradient_linear', 'properties': {'colors': {'type': 'array', 'items': {'type': 'string', 'format': 'color'}, 'minItems': 2, '$description': 'translations.json#/div_gradient_colors'}, 'angle': {'type': 'integer', 'constraint': 'number >= 0 && number <= 360', 'default_value': '0', '$description': 'translations.json#/div_gradient_linear_angle'}, 'type': {'type': 'string', 'enum': ['gradient']}}, 'required': ['colors', 'type'], '$schema': 'http://json-schema.org/draft-07/schema'}, rule='type')
 data_is_dict = isinstance(data, dict)
 if data_is_dict:
  data__missing_keys = set(['colors', 'type']) - data.keys()
  if data__missing_keys:
   if not (isinstance(data, str) and '@' in data):
    raise JsonSchemaValueException("" + (name_prefix or "data") + " must contain " + (str(sorted(data__missing_keys)) + " properties"), value=data, name="" + (name_prefix or "data") + "", definition={'type': 'object', '$description': 'translations.json#/div_gradient_linear', 'properties': {'colors': {'type': 'array', 'items': {'type': 'string', 'format': 'color'}, 'minItems': 2, '$description': 'translations.json#/div_gradient_colors'}, 'angle': {'type': 'integer', 'constraint': 'number >= 0 && number <= 360', 'default_value': '0', '$description': 'translations.json#/div_gradient_linear_angle'}, 'type': {'type': 'string', 'enum': ['gradient']}}, 'required': ['colors', 'type'], '$schema': 'http://json-schema.org/draft-07/schema'}, rule='required')
  data_keys = set(data.keys())
  if "colors" in data_keys:
   data_keys.remove("colors")
   data__colors = data["colors"]
   if not isinstance(data__colors, (list, tuple)):
    if not (isinstance(data__colors, str) and '@' in data__colors):
     raise JsonSchemaValueException("" + (name_prefix or "data") + ".colors must be array", value=data__colors, name="" + (name_prefix or "data") + ".colors", definition={'type': 'array', 'items': {'type': 'string', 'format': 'color'}, 'minItems': 2, '$description': 'translations.json#/div_gradient_colors'}, rule='type')
   data__colors_is_list = isinstance(data__colors, (list, tuple))
   if data__colors_is_list:
    data__colors_len = len(data__colors)
    if data__colors_len < 2:
     if not (isinstance(data__colors, str) and '@' in data__colors):
      raise JsonSchemaValueException("" + (name_prefix or "data") + ".colors must contain at least 2 items", value=data__colors, name="" + (name_prefix or "data") + ".colors", definition={'type': 'array', 'items': {'type': 'string', 'format': 'color'}, 'minItems': 2, '$description': 'translations.json#/div_gradient_colors'}, rule='minItems')
    for data__colors_x, data__colors_item in enumerate(data__colors):
     validate_common_json__color(data__colors_item, custom_formats, (name_prefix or "data") + ".colors[{data__colors_x}]".format(**locals()))
  if "angle" in data_keys:
   data_keys.remove("angle")
   data__angle = data["angle"]
   if not isinstance(data__angle, (int)) and not (isinstance(data__angle, float) and data__angle.is_integer()) or isinstance(data__angle, bool):
    if not (isinstance(data__angle, str) and '@' in data__angle):
     raise JsonSchemaValueException("" + (name_prefix or "data") + ".angle must be integer", value=data__angle, name="" + (name_prefix or "data") + ".angle", definition={'type': 'integer', 'constraint': 'number >= 0 && number <= 360', 'default_value': '0', '$description': 'translations.json#/div_gradient_linear_angle'}, rule='type')
  if "type" in data_keys:
   data_keys.remove("type")
   data__type = data["type"]
   if not isinstance(data__type, (str)):
    if not (isinstance(data__type, str) and '@' in data__type):
     raise JsonSchemaValueException("" + (name_prefix or "data") + ".type must be string", value=data__type, name="" + (name_prefix or "data") + ".type", definition={'type': 'string', 'enum': ['gradient']}, rule='type')
   if data__type not in ['gradient']:
    if not (isinstance(data__type, str) and '@' in data__type):
     raise JsonSchemaValueException("" + (name_prefix or "data") + ".type must be one of ['gradient']", value=data__type, name="" + (name_prefix or "data") + ".type", definition={'type': 'string', 'enum': ['gradient']}, rule='enum')
 return data

def validate_div_size_json(data, custom_formats={}, name_prefix=None):
 data_any_of_count14 = 0
 if not data_any_of_count14:
  try:
   validate_div_fixed_size_json(data, custom_formats, (name_prefix or "data") + "")
   data_any_of_count14 += 1
  except JsonSchemaValueException: pass
 if not data_any_of_count14:
  try:
   validate_div_match_parent_size_json(data, custom_formats, (name_prefix or "data") + "")
   data_any_of_count14 += 1
  except JsonSchemaValueException: pass
 if not data_any_of_count14:
  try:
   validate_div_wrap_content_size_json(data, custom_formats, (name_prefix or "data") + "")
   data_any_of_count14 += 1
  except JsonSchemaValueException: pass
 if not data_any_of_count14:
  if not (isinstance(data, str) and '@' in data):
   raise JsonSchemaValueException("" + (name_prefix or "data") + " cannot be validated by any definition", value=data, name="" + (name_prefix or "data") + "", definition={'anyOf': [{'type': 'object', '$description': 'translations.json#/div_fixed_size', 'codegen': {'divan': {'forced_properties_order': ['value']}}, 'properties': {'value': {'$ref': 'common.json#/non_negative_integer', '$description': 'translations.json#/div_fixed_size_value'}, 'unit': {'$ref': 'div-size-unit.json', '$description': 'translations.json#/div_fixed_size_unit', 'default_value': 'dp'}, 'type': {'type': 'string', 'enum': ['fixed']}}, 'required': ['value', 'type'], '$schema': 'http://json-schema.org/draft-07/schema'}, {'type': 'object', '$description': 'translations.json#/div_match_parent_size', 'properties': {'weight': {'$ref': 'common.json#/positive_number', '$description': 'translations.json#/div_match_parent_size_weight'}, 'type': {'type': 'string', 'enum': ['match_parent']}}, 'required': ['type'], '$schema': 'http://json-schema.org/draft-07/schema'}, {'type': 'object', '$description': 'translations.json#/div_wrap_content_size', 'definitions': {'constraint_size': {'type': 'object', 'properties': {'value': {'$ref': 'common.json#/non_negative_integer'}, 'unit': {'$ref': 'div-size-unit.json', '$description': 'translations.json#/div_size_unit', 'default_value': 'dp'}}, 'required': ['value']}}, 'properties': {'type': {'type': 'string', 'enum': ['wrap_content']}, 'constrained': {'$ref': 'common.json#/boolean_int', '$description': 'translations.json#/div_wrap_content_size_constrained'}, 'min_size': {'$ref': '#/definitions/constraint_size', '$description': 'translations.json#/div_size_min'}, 'max_size': {'$ref': '#/definitions/constraint_size', '$description': 'translations.json#/div_size_max'}}, 'required': ['type'], '$schema': 'http://json-schema.org/draft-07/schema'}], '$schema': 'http://json-schema.org/draft-07/schema'}, rule='anyOf')
 return data

def validate_div_wrap_content_size_json(data, custom_formats={}, name_prefix=None):
 if not isinstance(data, (dict)):
  if not (isinstance(data, str) and '@' in data):
   raise JsonSchemaValueException("" + (name_prefix or "data") + " must be object", value=data, name="" + (name_prefix or "data") + "", definition={'type': 'object', '$description': 'translations.json#/div_wrap_content_size', 'definitions': {'constraint_size': {'type': 'object', 'properties': {'value': {'type': 'integer', 'constraint': 'number >= 0'}, 'unit': {'type': 'string', 'enum': ['dp', 'sp', 'px'], '$description': 'translations.json#/div_size_unit', 'platforms': ['android', 'ios'], '$schema': 'http://json-schema.org/draft-07/schema'}}, 'required': ['value']}}, 'properties': {'type': {'type': 'string', 'enum': ['wrap_content']}, 'constrained': {'oneOf': [{'type': 'boolean'}, {'type': 'integer', 'enum': [0, 1]}]}, 'min_size': {'type': 'object', 'properties': {'value': {'$ref': 'common.json#/non_negative_integer'}, 'unit': {'$ref': 'div-size-unit.json', '$description': 'translations.json#/div_size_unit', 'default_value': 'dp'}}, 'required': ['value']}, 'max_size': {'type': 'object', 'properties': {'value': {'$ref': 'common.json#/non_negative_integer'}, 'unit': {'$ref': 'div-size-unit.json', '$description': 'translations.json#/div_size_unit', 'default_value': 'dp'}}, 'required': ['value']}}, 'required': ['type'], '$schema': 'http://json-schema.org/draft-07/schema'}, rule='type')
 data_is_dict = isinstance(data, dict)
 if data_is_dict:
  data__missing_keys = set(['type']) - data.keys()
  if data__missing_keys:
   if not (isinstance(data, str) and '@' in data):
    raise JsonSchemaValueException("" + (name_prefix or "data") + " must contain " + (str(sorted(data__missing_keys)) + " properties"), value=data, name="" + (name_prefix or "data") + "", definition={'type': 'object', '$description': 'translations.json#/div_wrap_content_size', 'definitions': {'constraint_size': {'type': 'object', 'properties': {'value': {'type': 'integer', 'constraint': 'number >= 0'}, 'unit': {'type': 'string', 'enum': ['dp', 'sp', 'px'], '$description': 'translations.json#/div_size_unit', 'platforms': ['android', 'ios'], '$schema': 'http://json-schema.org/draft-07/schema'}}, 'required': ['value']}}, 'properties': {'type': {'type': 'string', 'enum': ['wrap_content']}, 'constrained': {'oneOf': [{'type': 'boolean'}, {'type': 'integer', 'enum': [0, 1]}]}, 'min_size': {'type': 'object', 'properties': {'value': {'$ref': 'common.json#/non_negative_integer'}, 'unit': {'$ref': 'div-size-unit.json', '$description': 'translations.json#/div_size_unit', 'default_value': 'dp'}}, 'required': ['value']}, 'max_size': {'type': 'object', 'properties': {'value': {'$ref': 'common.json#/non_negative_integer'}, 'unit': {'$ref': 'div-size-unit.json', '$description': 'translations.json#/div_size_unit', 'default_value': 'dp'}}, 'required': ['value']}}, 'required': ['type'], '$schema': 'http://json-schema.org/draft-07/schema'}, rule='required')
  data_keys = set(data.keys())
  if "type" in data_keys:
   data_keys.remove("type")
   data__type = data["type"]
   if not isinstance(data__type, (str)):
    if not (isinstance(data__type, str) and '@' in data__type):
     raise JsonSchemaValueException("" + (name_prefix or "data") + ".type must be string", value=data__type, name="" + (name_prefix or "data") + ".type", definition={'type': 'string', 'enum': ['wrap_content']}, rule='type')
   if data__type not in ['wrap_content']:
    if not (isinstance(data__type, str) and '@' in data__type):
     raise JsonSchemaValueException("" + (name_prefix or "data") + ".type must be one of ['wrap_content']", value=data__type, name="" + (name_prefix or "data") + ".type", definition={'type': 'string', 'enum': ['wrap_content']}, rule='enum')
  if "constrained" in data_keys:
   data_keys.remove("constrained")
   data__constrained = data["constrained"]
   validate_common_json__boolean_int(data__constrained, custom_formats, (name_prefix or "data") + ".constrained")
  if "min_size" in data_keys:
   data_keys.remove("min_size")
   data__minsize = data["min_size"]
   validate_div_wrap_content_size_json__definitions_constraint_size(data__minsize, custom_formats, (name_prefix or "data") + ".min_size")
  if "max_size" in data_keys:
   data_keys.remove("max_size")
   data__maxsize = data["max_size"]
   validate_div_wrap_content_size_json__definitions_constraint_size(data__maxsize, custom_formats, (name_prefix or "data") + ".max_size")
 return data

def validate_div_wrap_content_size_json__definitions_constraint_size(data, custom_formats={}, name_prefix=None):
 if not isinstance(data, (dict)):
  if not (isinstance(data, str) and '@' in data):
   raise JsonSchemaValueException("" + (name_prefix or "data") + " must be object", value=data, name="" + (name_prefix or "data") + "", definition={'type': 'object', 'properties': {'value': {'type': 'integer', 'constraint': 'number >= 0'}, 'unit': {'type': 'string', 'enum': ['dp', 'sp', 'px'], '$description': 'translations.json#/div_size_unit', 'platforms': ['android', 'ios'], '$schema': 'http://json-schema.org/draft-07/schema'}}, 'required': ['value']}, rule='type')
 data_is_dict = isinstance(data, dict)
 if data_is_dict:
  data__missing_keys = set(['value']) - data.keys()
  if data__missing_keys:
   if not (isinstance(data, str) and '@' in data):
    raise JsonSchemaValueException("" + (name_prefix or "data") + " must contain " + (str(sorted(data__missing_keys)) + " properties"), value=data, name="" + (name_prefix or "data") + "", definition={'type': 'object', 'properties': {'value': {'type': 'integer', 'constraint': 'number >= 0'}, 'unit': {'type': 'string', 'enum': ['dp', 'sp', 'px'], '$description': 'translations.json#/div_size_unit', 'platforms': ['android', 'ios'], '$schema': 'http://json-schema.org/draft-07/schema'}}, 'required': ['value']}, rule='required')
  data_keys = set(data.keys())
  if "value" in data_keys:
   data_keys.remove("value")
   data__value = data["value"]
   validate_common_json__non_negative_integer(data__value, custom_formats, (name_prefix or "data") + ".value")
  if "unit" in data_keys:
   data_keys.remove("unit")
   data__unit = data["unit"]
   validate_div_size_unit_json(data__unit, custom_formats, (name_prefix or "data") + ".unit")
 return data

def validate_div_match_parent_size_json(data, custom_formats={}, name_prefix=None):
 if not isinstance(data, (dict)):
  if not (isinstance(data, str) and '@' in data):
   raise JsonSchemaValueException("" + (name_prefix or "data") + " must be object", value=data, name="" + (name_prefix or "data") + "", definition={'type': 'object', '$description': 'translations.json#/div_match_parent_size', 'properties': {'weight': {'type': 'number', 'constraint': 'number > 0'}, 'type': {'type': 'string', 'enum': ['match_parent']}}, 'required': ['type'], '$schema': 'http://json-schema.org/draft-07/schema'}, rule='type')
 data_is_dict = isinstance(data, dict)
 if data_is_dict:
  data__missing_keys = set(['type']) - data.keys()
  if data__missing_keys:
   if not (isinstance(data, str) and '@' in data):
    raise JsonSchemaValueException("" + (name_prefix or "data") + " must contain " + (str(sorted(data__missing_keys)) + " properties"), value=data, name="" + (name_prefix or "data") + "", definition={'type': 'object', '$description': 'translations.json#/div_match_parent_size', 'properties': {'weight': {'type': 'number', 'constraint': 'number > 0'}, 'type': {'type': 'string', 'enum': ['match_parent']}}, 'required': ['type'], '$schema': 'http://json-schema.org/draft-07/schema'}, rule='required')
  data_keys = set(data.keys())
  if "weight" in data_keys:
   data_keys.remove("weight")
   data__weight = data["weight"]
   validate_common_json__positive_number(data__weight, custom_formats, (name_prefix or "data") + ".weight")
  if "type" in data_keys:
   data_keys.remove("type")
   data__type = data["type"]
   if not isinstance(data__type, (str)):
    if not (isinstance(data__type, str) and '@' in data__type):
     raise JsonSchemaValueException("" + (name_prefix or "data") + ".type must be string", value=data__type, name="" + (name_prefix or "data") + ".type", definition={'type': 'string', 'enum': ['match_parent']}, rule='type')
   if data__type not in ['match_parent']:
    if not (isinstance(data__type, str) and '@' in data__type):
     raise JsonSchemaValueException("" + (name_prefix or "data") + ".type must be one of ['match_parent']", value=data__type, name="" + (name_prefix or "data") + ".type", definition={'type': 'string', 'enum': ['match_parent']}, rule='enum')
 return data

def validate_div_border_json(data, custom_formats={}, name_prefix=None):
 if not isinstance(data, (dict)):
  if not (isinstance(data, str) and '@' in data):
   raise JsonSchemaValueException("" + (name_prefix or "data") + " must be object", value=data, name="" + (name_prefix or "data") + "", definition={'type': 'object', '$description': 'translations.json#/div_border', 'properties': {'has_shadow': {'oneOf': [{'type': 'boolean'}, {'type': 'integer', 'enum': [0, 1]}]}, 'shadow': {'type': 'object', '$description': 'translations.json#/div_shadow', 'properties': {'color': {'$ref': 'common.json#/color', '$description': 'translations.json#/div_shadow_color', 'default_value': '#000000'}, 'offset': {'$ref': 'div-point.json', '$description': 'translations.json#/div_shadow_offset'}, 'blur': {'$ref': 'common.json#/non_negative_integer', '$description': 'translations.json#/div_shadow_blur', 'default_value': '2'}, 'alpha': {'type': 'number', 'default_value': '0.19', 'constraint': 'number >= 0.0 && number <= 1.0', '$description': 'translations.json#/div_shadow_alpha'}}, 'required': ['offset'], '$schema': 'http://json-schema.org/draft-07/schema'}, 'stroke': {'type': 'object', '$description': 'translations.json#/div_stroke', 'properties': {'width': {'$ref': 'common.json#/non_negative_integer', 'default_value': '1', '$description': 'translations.json#/div_stroke_width'}, 'color': {'$ref': 'common.json#/color', '$description': 'translations.json#/div_stroke_color'}, 'unit': {'$ref': 'div-size-unit.json', 'default_value': 'dp'}}, 'required': ['color'], '$schema': 'http://json-schema.org/draft-07/schema'}, 'corner_radius': {'type': 'integer', 'constraint': 'number >= 0'}, 'corners_radius': {'type': 'object', '$description': 'translations.json#/div_corners_radius', 'properties': {'top-left': {'$ref': 'common.json#/non_negative_integer', '$description': 'translations.json#/div_corners_radius_top_left'}, 'top-right': {'$ref': 'common.json#/non_negative_integer', '$description': 'translations.json#/div_corners_radius_top_right'}, 'bottom-left': {'$ref': 'common.json#/non_negative_integer', '$description': 'translations.json#/div_corners_radius_bottom_left'}, 'bottom-right': {'$ref': 'common.json#/non_negative_integer', '$description': 'translations.json#/div_corners_radius_bottom_right'}}, '$schema': 'http://json-schema.org/draft-07/schema'}}, '$schema': 'http://json-schema.org/draft-07/schema'}, rule='type')
 data_is_dict = isinstance(data, dict)
 if data_is_dict:
  data_keys = set(data.keys())
  if "has_shadow" in data_keys:
   data_keys.remove("has_shadow")
   data__hasshadow = data["has_shadow"]
   validate_common_json__boolean_int(data__hasshadow, custom_formats, (name_prefix or "data") + ".has_shadow")
  if "shadow" in data_keys:
   data_keys.remove("shadow")
   data__shadow = data["shadow"]
   validate_div_shadow_json(data__shadow, custom_formats, (name_prefix or "data") + ".shadow")
  if "stroke" in data_keys:
   data_keys.remove("stroke")
   data__stroke = data["stroke"]
   validate_div_stroke_json(data__stroke, custom_formats, (name_prefix or "data") + ".stroke")
  if "corner_radius" in data_keys:
   data_keys.remove("corner_radius")
   data__cornerradius = data["corner_radius"]
   validate_common_json__non_negative_integer(data__cornerradius, custom_formats, (name_prefix or "data") + ".corner_radius")
  if "corners_radius" in data_keys:
   data_keys.remove("corners_radius")
   data__cornersradius = data["corners_radius"]
   validate_div_corners_radius_json(data__cornersradius, custom_formats, (name_prefix or "data") + ".corners_radius")
 return data

def validate_div_corners_radius_json(data, custom_formats={}, name_prefix=None):
 if not isinstance(data, (dict)):
  if not (isinstance(data, str) and '@' in data):
   raise JsonSchemaValueException("" + (name_prefix or "data") + " must be object", value=data, name="" + (name_prefix or "data") + "", definition={'type': 'object', '$description': 'translations.json#/div_corners_radius', 'properties': {'top-left': {'type': 'integer', 'constraint': 'number >= 0'}, 'top-right': {'type': 'integer', 'constraint': 'number >= 0'}, 'bottom-left': {'type': 'integer', 'constraint': 'number >= 0'}, 'bottom-right': {'type': 'integer', 'constraint': 'number >= 0'}}, '$schema': 'http://json-schema.org/draft-07/schema'}, rule='type')
 data_is_dict = isinstance(data, dict)
 if data_is_dict:
  data_keys = set(data.keys())
  if "top-left" in data_keys:
   data_keys.remove("top-left")
   data__topleft = data["top-left"]
   validate_common_json__non_negative_integer(data__topleft, custom_formats, (name_prefix or "data") + ".top-left")
  if "top-right" in data_keys:
   data_keys.remove("top-right")
   data__topright = data["top-right"]
   validate_common_json__non_negative_integer(data__topright, custom_formats, (name_prefix or "data") + ".top-right")
  if "bottom-left" in data_keys:
   data_keys.remove("bottom-left")
   data__bottomleft = data["bottom-left"]
   validate_common_json__non_negative_integer(data__bottomleft, custom_formats, (name_prefix or "data") + ".bottom-left")
  if "bottom-right" in data_keys:
   data_keys.remove("bottom-right")
   data__bottomright = data["bottom-right"]
   validate_common_json__non_negative_integer(data__bottomright, custom_formats, (name_prefix or "data") + ".bottom-right")
 return data

def validate_div_stroke_json(data, custom_formats={}, name_prefix=None):
 if not isinstance(data, (dict)):
  if not (isinstance(data, str) and '@' in data):
   raise JsonSchemaValueException("" + (name_prefix or "data") + " must be object", value=data, name="" + (name_prefix or "data") + "", definition={'type': 'object', '$description': 'translations.json#/div_stroke', 'properties': {'width': {'type': 'integer', 'constraint': 'number >= 0'}, 'color': {'type': 'string', 'format': 'color'}, 'unit': {'type': 'string', 'enum': ['dp', 'sp', 'px'], '$description': 'translations.json#/div_size_unit', 'platforms': ['android', 'ios'], '$schema': 'http://json-schema.org/draft-07/schema'}}, 'required': ['color'], '$schema': 'http://json-schema.org/draft-07/schema'}, rule='type')
 data_is_dict = isinstance(data, dict)
 if data_is_dict:
  data__missing_keys = set(['color']) - data.keys()
  if data__missing_keys:
   if not (isinstance(data, str) and '@' in data):
    raise JsonSchemaValueException("" + (name_prefix or "data") + " must contain " + (str(sorted(data__missing_keys)) + " properties"), value=data, name="" + (name_prefix or "data") + "", definition={'type': 'object', '$description': 'translations.json#/div_stroke', 'properties': {'width': {'type': 'integer', 'constraint': 'number >= 0'}, 'color': {'type': 'string', 'format': 'color'}, 'unit': {'type': 'string', 'enum': ['dp', 'sp', 'px'], '$description': 'translations.json#/div_size_unit', 'platforms': ['android', 'ios'], '$schema': 'http://json-schema.org/draft-07/schema'}}, 'required': ['color'], '$schema': 'http://json-schema.org/draft-07/schema'}, rule='required')
  data_keys = set(data.keys())
  if "width" in data_keys:
   data_keys.remove("width")
   data__width = data["width"]
   validate_common_json__non_negative_integer(data__width, custom_formats, (name_prefix or "data") + ".width")
  if "color" in data_keys:
   data_keys.remove("color")
   data__color = data["color"]
   validate_common_json__color(data__color, custom_formats, (name_prefix or "data") + ".color")
  if "unit" in data_keys:
   data_keys.remove("unit")
   data__unit = data["unit"]
   validate_div_size_unit_json(data__unit, custom_formats, (name_prefix or "data") + ".unit")
 return data

def validate_div_shadow_json(data, custom_formats={}, name_prefix=None):
 if not isinstance(data, (dict)):
  if not (isinstance(data, str) and '@' in data):
   raise JsonSchemaValueException("" + (name_prefix or "data") + " must be object", value=data, name="" + (name_prefix or "data") + "", definition={'type': 'object', '$description': 'translations.json#/div_shadow', 'properties': {'color': {'type': 'string', 'format': 'color'}, 'offset': {'type': 'object', '$description': 'translations.json#/div_point', 'properties': {'x': {'$ref': 'div-dimension.json', '$description': 'translations.json#/div_point_x'}, 'y': {'$ref': 'div-dimension.json', '$description': 'translations.json#/div_point_y'}}, 'required': ['x', 'y'], '$schema': 'http://json-schema.org/draft-07/schema'}, 'blur': {'type': 'integer', 'constraint': 'number >= 0'}, 'alpha': {'type': 'number', 'default_value': '0.19', 'constraint': 'number >= 0.0 && number <= 1.0', '$description': 'translations.json#/div_shadow_alpha'}}, 'required': ['offset'], '$schema': 'http://json-schema.org/draft-07/schema'}, rule='type')
 data_is_dict = isinstance(data, dict)
 if data_is_dict:
  data__missing_keys = set(['offset']) - data.keys()
  if data__missing_keys:
   if not (isinstance(data, str) and '@' in data):
    raise JsonSchemaValueException("" + (name_prefix or "data") + " must contain " + (str(sorted(data__missing_keys)) + " properties"), value=data, name="" + (name_prefix or "data") + "", definition={'type': 'object', '$description': 'translations.json#/div_shadow', 'properties': {'color': {'type': 'string', 'format': 'color'}, 'offset': {'type': 'object', '$description': 'translations.json#/div_point', 'properties': {'x': {'$ref': 'div-dimension.json', '$description': 'translations.json#/div_point_x'}, 'y': {'$ref': 'div-dimension.json', '$description': 'translations.json#/div_point_y'}}, 'required': ['x', 'y'], '$schema': 'http://json-schema.org/draft-07/schema'}, 'blur': {'type': 'integer', 'constraint': 'number >= 0'}, 'alpha': {'type': 'number', 'default_value': '0.19', 'constraint': 'number >= 0.0 && number <= 1.0', '$description': 'translations.json#/div_shadow_alpha'}}, 'required': ['offset'], '$schema': 'http://json-schema.org/draft-07/schema'}, rule='required')
  data_keys = set(data.keys())
  if "color" in data_keys:
   data_keys.remove("color")
   data__color = data["color"]
   validate_common_json__color(data__color, custom_formats, (name_prefix or "data") + ".color")
  if "offset" in data_keys:
   data_keys.remove("offset")
   data__offset = data["offset"]
   validate_div_point_json(data__offset, custom_formats, (name_prefix or "data") + ".offset")
  if "blur" in data_keys:
   data_keys.remove("blur")
   data__blur = data["blur"]
   validate_common_json__non_negative_integer(data__blur, custom_formats, (name_prefix or "data") + ".blur")
  if "alpha" in data_keys:
   data_keys.remove("alpha")
   data__alpha = data["alpha"]
   if not isinstance(data__alpha, (int, float, Decimal)) or isinstance(data__alpha, bool):
    if not (isinstance(data__alpha, str) and '@' in data__alpha):
     raise JsonSchemaValueException("" + (name_prefix or "data") + ".alpha must be number", value=data__alpha, name="" + (name_prefix or "data") + ".alpha", definition={'type': 'number', 'default_value': '0.19', 'constraint': 'number >= 0.0 && number <= 1.0', '$description': 'translations.json#/div_shadow_alpha'}, rule='type')
 return data

def validate_div_select_json(data, custom_formats={}, name_prefix=None):
 validate_div_base_json(data, custom_formats, (name_prefix or "data") + "")
 data_is_dict = isinstance(data, dict)
 if data_is_dict:
  data_keys = set(data.keys())
  if "type" in data_keys:
   data_keys.remove("type")
   data__type = data["type"]
   if not isinstance(data__type, (str)):
    if not (isinstance(data__type, str) and '@' in data__type):
     raise JsonSchemaValueException("" + (name_prefix or "data") + ".type must be string", value=data__type, name="" + (name_prefix or "data") + ".type", definition={'type': 'string', 'enum': ['select']}, rule='type')
   if data__type not in ['select']:
    if not (isinstance(data__type, str) and '@' in data__type):
     raise JsonSchemaValueException("" + (name_prefix or "data") + ".type must be one of ['select']", value=data__type, name="" + (name_prefix or "data") + ".type", definition={'type': 'string', 'enum': ['select']}, rule='enum')
  if "options" in data_keys:
   data_keys.remove("options")
   data__options = data["options"]
   if not isinstance(data__options, (list, tuple)):
    if not (isinstance(data__options, str) and '@' in data__options):
     raise JsonSchemaValueException("" + (name_prefix or "data") + ".options must be array", value=data__options, name="" + (name_prefix or "data") + ".options", definition={'type': 'array', 'items': {'type': 'object', 'properties': {'text': {'type': 'string', '$description': 'translations.json#/div_select_option_text'}, 'value': {'type': 'string', '$description': 'translations.json#/div_select_option_value'}}, 'required': ['value']}, 'minItems': 1}, rule='type')
   data__options_is_list = isinstance(data__options, (list, tuple))
   if data__options_is_list:
    data__options_len = len(data__options)
    if data__options_len < 1:
     if not (isinstance(data__options, str) and '@' in data__options):
      raise JsonSchemaValueException("" + (name_prefix or "data") + ".options must contain at least 1 items", value=data__options, name="" + (name_prefix or "data") + ".options", definition={'type': 'array', 'items': {'type': 'object', 'properties': {'text': {'type': 'string', '$description': 'translations.json#/div_select_option_text'}, 'value': {'type': 'string', '$description': 'translations.json#/div_select_option_value'}}, 'required': ['value']}, 'minItems': 1}, rule='minItems')
    for data__options_x, data__options_item in enumerate(data__options):
     validate_div_select_json__definitions_option(data__options_item, custom_formats, (name_prefix or "data") + ".options[{data__options_x}]".format(**locals()))
  if "value_variable" in data_keys:
   data_keys.remove("value_variable")
   data__valuevariable = data["value_variable"]
   validate_div_variable_name_json(data__valuevariable, custom_formats, (name_prefix or "data") + ".value_variable")
  if "font_size" in data_keys:
   data_keys.remove("font_size")
   data__fontsize = data["font_size"]
   validate_common_json__non_negative_integer(data__fontsize, custom_formats, (name_prefix or "data") + ".font_size")
  if "font_size_unit" in data_keys:
   data_keys.remove("font_size_unit")
   data__fontsizeunit = data["font_size_unit"]
   validate_div_size_unit_json(data__fontsizeunit, custom_formats, (name_prefix or "data") + ".font_size_unit")
  if "font_family" in data_keys:
   data_keys.remove("font_family")
   data__fontfamily = data["font_family"]
   validate_common_json__non_empty_string(data__fontfamily, custom_formats, (name_prefix or "data") + ".font_family")
  if "font_weight" in data_keys:
   data_keys.remove("font_weight")
   data__fontweight = data["font_weight"]
   validate_div_font_weight_json(data__fontweight, custom_formats, (name_prefix or "data") + ".font_weight")
  if "hint_text" in data_keys:
   data_keys.remove("hint_text")
   data__hinttext = data["hint_text"]
   validate_common_json__non_empty_string(data__hinttext, custom_formats, (name_prefix or "data") + ".hint_text")
  if "hint_color" in data_keys:
   data_keys.remove("hint_color")
   data__hintcolor = data["hint_color"]
   validate_common_json__color(data__hintcolor, custom_formats, (name_prefix or "data") + ".hint_color")
  if "line_height" in data_keys:
   data_keys.remove("line_height")
   data__lineheight = data["line_height"]
   validate_common_json__non_negative_integer(data__lineheight, custom_formats, (name_prefix or "data") + ".line_height")
  if "text_color" in data_keys:
   data_keys.remove("text_color")
   data__textcolor = data["text_color"]
   validate_common_json__color(data__textcolor, custom_formats, (name_prefix or "data") + ".text_color")
  if "letter_spacing" in data_keys:
   data_keys.remove("letter_spacing")
   data__letterspacing = data["letter_spacing"]
   if not isinstance(data__letterspacing, (int, float, Decimal)) or isinstance(data__letterspacing, bool):
    if not (isinstance(data__letterspacing, str) and '@' in data__letterspacing):
     raise JsonSchemaValueException("" + (name_prefix or "data") + ".letter_spacing must be number", value=data__letterspacing, name="" + (name_prefix or "data") + ".letter_spacing", definition={'type': 'number', 'default_value': '0', '$description': 'translations.json#/div_select_letter_spacing'}, rule='type')
 data_is_dict = isinstance(data, dict)
 if data_is_dict:
  data__missing_keys = set(['type', 'options', 'value_variable']) - data.keys()
  if data__missing_keys:
   if not (isinstance(data, str) and '@' in data):
    raise JsonSchemaValueException("" + (name_prefix or "data") + " must contain " + (str(sorted(data__missing_keys)) + " properties"), value=data, name="" + (name_prefix or "data") + "", definition={'java_extends': 'DivBlockWithId', '$description': 'translations.json#/div_select', 'definitions': {'option': {'type': 'object', 'properties': {'text': {'type': 'string', '$description': 'translations.json#/div_select_option_text'}, 'value': {'type': 'string', '$description': 'translations.json#/div_select_option_value'}}, 'required': ['value']}}, 'allOf': [{'protocol_name': 'div-base', 'codegen': {'swift': {'super_protocol': 'DivBlockModeling'}, 'documentation': {'include_in_toc': True}}, 'type': 'object', 'properties': {'id': {'$ref': 'common.json#/non_empty_string', 'supports_expressions': False, '$description': 'translations.json#/div_base_id'}, 'border': {'$ref': 'div-border.json', '$description': 'translations.json#/div_base_border'}, 'width': {'$ref': 'div-size.json', 'default_value': '{"type": "match_parent"}', '$description': 'translations.json#/div_base_width'}, 'height': {'$ref': 'div-size.json', 'default_value': '{"type": "wrap_content"}', '$description': 'translations.json#/div_base_height'}, 'background': {'type': 'array', 'items': {'$ref': 'div-background.json'}, 'minItems': 1, '$description': 'translations.json#/div_base_background'}, 'paddings': {'$ref': 'div-edge-insets.json', '$description': 'translations.json#/div_base_paddings'}, 'margins': {'$ref': 'div-edge-insets.json', '$description': 'translations.json#/div_base_margins'}, 'alpha': {'type': 'number', 'default_value': '1.0', 'constraint': 'number >= 0.0 && number <= 1.0', '$description': 'translations.json#/div_base_alpha'}, 'alignment_vertical': {'$ref': 'div-alignment-vertical.json', '$description': 'translations.json#/div_base_alignment_vertical'}, 'alignment_horizontal': {'$ref': 'div-alignment-horizontal.json', '$description': 'translations.json#/div_base_alignment_horizontal'}, 'row_span': {'$ref': 'common.json#/non_negative_integer', '$description': 'translations.json#/div_base_row_span'}, 'column_span': {'$ref': 'common.json#/non_negative_integer', '$description': 'translations.json#/div_base_column_span'}, 'visibility_action': {'$ref': 'div-visibility-action.json', '$description': 'translations.json#/div_base_visibility_action'}, 'visibility_actions': {'type': 'array', 'items': {'$ref': 'div-visibility-action.json'}, 'minItems': 1, '$description': 'translations.json#/div_base_visibility_actions'}, 'disappear_actions': {'type': 'array', 'items': {'$ref': 'div-disappear-action.json'}, 'minItems': 1, '$description': 'translations.json#/div_base_disappear_actions'}, 'tooltips': {'type': 'array', 'items': {'$ref': 'div-tooltip.json'}, 'minItems': 1, '$description': 'translations.json#/div_base_tooltips'}, 'accessibility': {'$ref': 'div-accessibility.json', '$description': 'translations.json#/div_base_accessibility'}, 'extensions': {'type': 'array', 'items': {'$ref': 'div-extension.json'}, 'minItems': 1, '$description': 'translations.json#/div_base_extensions'}, 'transition_triggers': {'type': 'array', 'items': {'$ref': 'div-transition-trigger.json'}, 'minItems': 1, 'supports_expressions': False, '$description': 'translations.json#/div_base_transition_triggers'}, 'transition_in': {'$ref': 'div-appearance-transition.json', '$description': 'translations.json#/div_base_transition_in'}, 'transition_change': {'$ref': 'div-change-transition.json', '$description': 'translations.json#/div_base_transition_change'}, 'transition_out': {'$ref': 'div-appearance-transition.json', '$description': 'translations.json#/div_base_transition_out'}, 'selected_actions': {'type': 'array', 'items': {'$ref': 'div-action.json'}, 'minItems': 1, '$description': 'translations.json#/div_base_selected_actions'}, 'focus': {'$ref': 'div-focus.json', '$description': 'translations.json#/div_base_focus', 'platforms': ['android', 'ios']}, 'visibility': {'$ref': 'div-visibility.json', '$description': 'translations.json#/div_base_visibility', 'default_value': 'visible'}, 'transform': {'$ref': 'div-transform.json', '$description': 'translations.json#/div_base_transform'}}, '$schema': 'http://json-schema.org/draft-07/schema'}, {'properties': {'type': {'type': 'string', 'enum': ['select']}, 'options': {'type': 'array', 'items': {'type': 'object', 'properties': {'text': {'type': 'string', '$description': 'translations.json#/div_select_option_text'}, 'value': {'type': 'string', '$description': 'translations.json#/div_select_option_value'}}, 'required': ['value']}, 'minItems': 1}, 'value_variable': {'supports_expressions': False, '$ref': 'common.json#/non_empty_string', '$schema': 'http://json-schema.org/draft-07/schema'}, 'font_size': {'type': 'integer', 'constraint': 'number >= 0'}, 'font_size_unit': {'type': 'string', 'enum': ['dp', 'sp', 'px'], '$description': 'translations.json#/div_size_unit', 'platforms': ['android', 'ios'], '$schema': 'http://json-schema.org/draft-07/schema'}, 'font_family': {'type': 'string', 'minLength': 1, 'clientMinLength': 1}, 'font_weight': {'type': 'string', 'enum': ['light', 'medium', 'regular', 'bold'], '$schema': 'http://json-schema.org/draft-07/schema'}, 'hint_text': {'type': 'string', 'minLength': 1, 'clientMinLength': 1}, 'hint_color': {'type': 'string', 'format': 'color'}, 'line_height': {'type': 'integer', 'constraint': 'number >= 0'}, 'text_color': {'type': 'string', 'format': 'color'}, 'letter_spacing': {'type': 'number', 'default_value': '0', '$description': 'translations.json#/div_select_letter_spacing'}}}], 'required': ['type', 'options', 'value_variable'], '$schema': 'http://json-schema.org/draft-07/schema'}, rule='required')
 return data

def validate_div_font_weight_json(data, custom_formats={}, name_prefix=None):
 if not isinstance(data, (str)):
  if not (isinstance(data, str) and '@' in data):
   raise JsonSchemaValueException("" + (name_prefix or "data") + " must be string", value=data, name="" + (name_prefix or "data") + "", definition={'type': 'string', 'enum': ['light', 'medium', 'regular', 'bold'], '$schema': 'http://json-schema.org/draft-07/schema'}, rule='type')
 if data not in ['light', 'medium', 'regular', 'bold']:
  if not (isinstance(data, str) and '@' in data):
   raise JsonSchemaValueException("" + (name_prefix or "data") + " must be one of ['light', 'medium', 'regular', 'bold']", value=data, name="" + (name_prefix or "data") + "", definition={'type': 'string', 'enum': ['light', 'medium', 'regular', 'bold'], '$schema': 'http://json-schema.org/draft-07/schema'}, rule='enum')
 return data

def validate_div_select_json__definitions_option(data, custom_formats={}, name_prefix=None):
 if not isinstance(data, (dict)):
  if not (isinstance(data, str) and '@' in data):
   raise JsonSchemaValueException("" + (name_prefix or "data") + " must be object", value=data, name="" + (name_prefix or "data") + "", definition={'type': 'object', 'properties': {'text': {'type': 'string', '$description': 'translations.json#/div_select_option_text'}, 'value': {'type': 'string', '$description': 'translations.json#/div_select_option_value'}}, 'required': ['value']}, rule='type')
 data_is_dict = isinstance(data, dict)
 if data_is_dict:
  data__missing_keys = set(['value']) - data.keys()
  if data__missing_keys:
   if not (isinstance(data, str) and '@' in data):
    raise JsonSchemaValueException("" + (name_prefix or "data") + " must contain " + (str(sorted(data__missing_keys)) + " properties"), value=data, name="" + (name_prefix or "data") + "", definition={'type': 'object', 'properties': {'text': {'type': 'string', '$description': 'translations.json#/div_select_option_text'}, 'value': {'type': 'string', '$description': 'translations.json#/div_select_option_value'}}, 'required': ['value']}, rule='required')
  data_keys = set(data.keys())
  if "text" in data_keys:
   data_keys.remove("text")
   data__text = data["text"]
   if not isinstance(data__text, (str)):
    if not (isinstance(data__text, str) and '@' in data__text):
     raise JsonSchemaValueException("" + (name_prefix or "data") + ".text must be string", value=data__text, name="" + (name_prefix or "data") + ".text", definition={'type': 'string', '$description': 'translations.json#/div_select_option_text'}, rule='type')
  if "value" in data_keys:
   data_keys.remove("value")
   data__value = data["value"]
   if not isinstance(data__value, (str)):
    if not (isinstance(data__value, str) and '@' in data__value):
     raise JsonSchemaValueException("" + (name_prefix or "data") + ".value must be string", value=data__value, name="" + (name_prefix or "data") + ".value", definition={'type': 'string', '$description': 'translations.json#/div_select_option_value'}, rule='type')
 return data

def validate_div_input_json(data, custom_formats={}, name_prefix=None):
 validate_div_base_json(data, custom_formats, (name_prefix or "data") + "")
 data_is_dict = isinstance(data, dict)
 if data_is_dict:
  data_keys = set(data.keys())
  if "type" in data_keys:
   data_keys.remove("type")
   data__type = data["type"]
   if not isinstance(data__type, (str)):
    if not (isinstance(data__type, str) and '@' in data__type):
     raise JsonSchemaValueException("" + (name_prefix or "data") + ".type must be string", value=data__type, name="" + (name_prefix or "data") + ".type", definition={'type': 'string', 'enum': ['input']}, rule='type')
   if data__type not in ['input']:
    if not (isinstance(data__type, str) and '@' in data__type):
     raise JsonSchemaValueException("" + (name_prefix or "data") + ".type must be one of ['input']", value=data__type, name="" + (name_prefix or "data") + ".type", definition={'type': 'string', 'enum': ['input']}, rule='enum')
  if "font_size" in data_keys:
   data_keys.remove("font_size")
   data__fontsize = data["font_size"]
   validate_common_json__non_negative_integer(data__fontsize, custom_formats, (name_prefix or "data") + ".font_size")
  if "font_size_unit" in data_keys:
   data_keys.remove("font_size_unit")
   data__fontsizeunit = data["font_size_unit"]
   validate_div_size_unit_json(data__fontsizeunit, custom_formats, (name_prefix or "data") + ".font_size_unit")
  if "font_family" in data_keys:
   data_keys.remove("font_family")
   data__fontfamily = data["font_family"]
   validate_common_json__non_empty_string(data__fontfamily, custom_formats, (name_prefix or "data") + ".font_family")
  if "font_weight" in data_keys:
   data_keys.remove("font_weight")
   data__fontweight = data["font_weight"]
   validate_div_font_weight_json(data__fontweight, custom_formats, (name_prefix or "data") + ".font_weight")
  if "text_color" in data_keys:
   data_keys.remove("text_color")
   data__textcolor = data["text_color"]
   validate_common_json__color(data__textcolor, custom_formats, (name_prefix or "data") + ".text_color")
  if "text_variable" in data_keys:
   data_keys.remove("text_variable")
   data__textvariable = data["text_variable"]
   validate_div_variable_name_json(data__textvariable, custom_formats, (name_prefix or "data") + ".text_variable")
  if "text_alignment_horizontal" in data_keys:
   data_keys.remove("text_alignment_horizontal")
   data__textalignmenthorizontal = data["text_alignment_horizontal"]
   validate_div_alignment_horizontal_json(data__textalignmenthorizontal, custom_formats, (name_prefix or "data") + ".text_alignment_horizontal")
  if "text_alignment_vertical" in data_keys:
   data_keys.remove("text_alignment_vertical")
   data__textalignmentvertical = data["text_alignment_vertical"]
   validate_div_alignment_vertical_json(data__textalignmentvertical, custom_formats, (name_prefix or "data") + ".text_alignment_vertical")
  if "line_height" in data_keys:
   data_keys.remove("line_height")
   data__lineheight = data["line_height"]
   validate_common_json__non_negative_integer(data__lineheight, custom_formats, (name_prefix or "data") + ".line_height")
  if "max_visible_lines" in data_keys:
   data_keys.remove("max_visible_lines")
   data__maxvisiblelines = data["max_visible_lines"]
   validate_common_json__positive_integer(data__maxvisiblelines, custom_formats, (name_prefix or "data") + ".max_visible_lines")
  if "letter_spacing" in data_keys:
   data_keys.remove("letter_spacing")
   data__letterspacing = data["letter_spacing"]
   if not isinstance(data__letterspacing, (int, float, Decimal)) or isinstance(data__letterspacing, bool):
    if not (isinstance(data__letterspacing, str) and '@' in data__letterspacing):
     raise JsonSchemaValueException("" + (name_prefix or "data") + ".letter_spacing must be number", value=data__letterspacing, name="" + (name_prefix or "data") + ".letter_spacing", definition={'type': 'number', 'default_value': '0', '$description': 'translations.json#/div_input_letter_spacing'}, rule='type')
  if "hint_text" in data_keys:
   data_keys.remove("hint_text")
   data__hinttext = data["hint_text"]
   validate_common_json__non_empty_string(data__hinttext, custom_formats, (name_prefix or "data") + ".hint_text")
  if "hint_color" in data_keys:
   data_keys.remove("hint_color")
   data__hintcolor = data["hint_color"]
   validate_common_json__color(data__hintcolor, custom_formats, (name_prefix or "data") + ".hint_color")
  if "highlight_color" in data_keys:
   data_keys.remove("highlight_color")
   data__highlightcolor = data["highlight_color"]
   validate_common_json__color(data__highlightcolor, custom_formats, (name_prefix or "data") + ".highlight_color")
  if "native_interface" in data_keys:
   data_keys.remove("native_interface")
   data__nativeinterface = data["native_interface"]
   validate_div_input_json__definitions_native_interface(data__nativeinterface, custom_formats, (name_prefix or "data") + ".native_interface")
  if "keyboard_type" in data_keys:
   data_keys.remove("keyboard_type")
   data__keyboardtype = data["keyboard_type"]
   if not isinstance(data__keyboardtype, (str)):
    if not (isinstance(data__keyboardtype, str) and '@' in data__keyboardtype):
     raise JsonSchemaValueException("" + (name_prefix or "data") + ".keyboard_type must be string", value=data__keyboardtype, name="" + (name_prefix or "data") + ".keyboard_type", definition={'type': 'string', 'enum': ['single_line_text', 'multi_line_text', 'phone', 'number', 'email', 'uri'], 'default_value': 'multi_line_text', '$description': 'translations.json#/div_input_keyboard_type'}, rule='type')
   if data__keyboardtype not in ['single_line_text', 'multi_line_text', 'phone', 'number', 'email', 'uri']:
    if not (isinstance(data__keyboardtype, str) and '@' in data__keyboardtype):
     raise JsonSchemaValueException("" + (name_prefix or "data") + ".keyboard_type must be one of ['single_line_text', 'multi_line_text', 'phone', 'number', 'email', 'uri']", value=data__keyboardtype, name="" + (name_prefix or "data") + ".keyboard_type", definition={'type': 'string', 'enum': ['single_line_text', 'multi_line_text', 'phone', 'number', 'email', 'uri'], 'default_value': 'multi_line_text', '$description': 'translations.json#/div_input_keyboard_type'}, rule='enum')
  if "select_all_on_focus" in data_keys:
   data_keys.remove("select_all_on_focus")
   data__selectallonfocus = data["select_all_on_focus"]
   validate_common_json__boolean_int(data__selectallonfocus, custom_formats, (name_prefix or "data") + ".select_all_on_focus")
  if "mask" in data_keys:
   data_keys.remove("mask")
   data__mask = data["mask"]
   validate_div_input_mask_json(data__mask, custom_formats, (name_prefix or "data") + ".mask")
  if "validators" in data_keys:
   data_keys.remove("validators")
   data__validators = data["validators"]
   if not isinstance(data__validators, (list, tuple)):
    if not (isinstance(data__validators, str) and '@' in data__validators):
     raise JsonSchemaValueException("" + (name_prefix or "data") + ".validators must be array", value=data__validators, name="" + (name_prefix or "data") + ".validators", definition={'type': 'array', '$description': 'translations.json#/div_input_validators', 'platforms': ['android', 'ios'], 'items': {'anyOf': [{'$ref': 'div-input-validator-regex.json', '$description': 'translations.json#/div_input_validators_regex'}, {'$ref': 'div-input-validator-expression.json', '$description': 'translations.json#/div_input_validators_expression'}], '$schema': 'http://json-schema.org/draft-07/schema'}}, rule='type')
   data__validators_is_list = isinstance(data__validators, (list, tuple))
   if data__validators_is_list:
    data__validators_len = len(data__validators)
    for data__validators_x, data__validators_item in enumerate(data__validators):
     validate_div_input_validator_json(data__validators_item, custom_formats, (name_prefix or "data") + ".validators[{data__validators_x}]".format(**locals()))
 data_is_dict = isinstance(data, dict)
 if data_is_dict:
  data__missing_keys = set(['type', 'text_variable']) - data.keys()
  if data__missing_keys:
   if not (isinstance(data, str) and '@' in data):
    raise JsonSchemaValueException("" + (name_prefix or "data") + " must contain " + (str(sorted(data__missing_keys)) + " properties"), value=data, name="" + (name_prefix or "data") + "", definition={'java_extends': 'DivBlockWithId', '$description': 'translations.json#/div_input', 'definitions': {'native_interface': {'type': 'object', 'properties': {'color': {'type': 'string', 'format': 'color'}}, 'required': ['color']}}, 'allOf': [{'protocol_name': 'div-base', 'codegen': {'swift': {'super_protocol': 'DivBlockModeling'}, 'documentation': {'include_in_toc': True}}, 'type': 'object', 'properties': {'id': {'$ref': 'common.json#/non_empty_string', 'supports_expressions': False, '$description': 'translations.json#/div_base_id'}, 'border': {'$ref': 'div-border.json', '$description': 'translations.json#/div_base_border'}, 'width': {'$ref': 'div-size.json', 'default_value': '{"type": "match_parent"}', '$description': 'translations.json#/div_base_width'}, 'height': {'$ref': 'div-size.json', 'default_value': '{"type": "wrap_content"}', '$description': 'translations.json#/div_base_height'}, 'background': {'type': 'array', 'items': {'$ref': 'div-background.json'}, 'minItems': 1, '$description': 'translations.json#/div_base_background'}, 'paddings': {'$ref': 'div-edge-insets.json', '$description': 'translations.json#/div_base_paddings'}, 'margins': {'$ref': 'div-edge-insets.json', '$description': 'translations.json#/div_base_margins'}, 'alpha': {'type': 'number', 'default_value': '1.0', 'constraint': 'number >= 0.0 && number <= 1.0', '$description': 'translations.json#/div_base_alpha'}, 'alignment_vertical': {'$ref': 'div-alignment-vertical.json', '$description': 'translations.json#/div_base_alignment_vertical'}, 'alignment_horizontal': {'$ref': 'div-alignment-horizontal.json', '$description': 'translations.json#/div_base_alignment_horizontal'}, 'row_span': {'$ref': 'common.json#/non_negative_integer', '$description': 'translations.json#/div_base_row_span'}, 'column_span': {'$ref': 'common.json#/non_negative_integer', '$description': 'translations.json#/div_base_column_span'}, 'visibility_action': {'$ref': 'div-visibility-action.json', '$description': 'translations.json#/div_base_visibility_action'}, 'visibility_actions': {'type': 'array', 'items': {'$ref': 'div-visibility-action.json'}, 'minItems': 1, '$description': 'translations.json#/div_base_visibility_actions'}, 'disappear_actions': {'type': 'array', 'items': {'$ref': 'div-disappear-action.json'}, 'minItems': 1, '$description': 'translations.json#/div_base_disappear_actions'}, 'tooltips': {'type': 'array', 'items': {'$ref': 'div-tooltip.json'}, 'minItems': 1, '$description': 'translations.json#/div_base_tooltips'}, 'accessibility': {'$ref': 'div-accessibility.json', '$description': 'translations.json#/div_base_accessibility'}, 'extensions': {'type': 'array', 'items': {'$ref': 'div-extension.json'}, 'minItems': 1, '$description': 'translations.json#/div_base_extensions'}, 'transition_triggers': {'type': 'array', 'items': {'$ref': 'div-transition-trigger.json'}, 'minItems': 1, 'supports_expressions': False, '$description': 'translations.json#/div_base_transition_triggers'}, 'transition_in': {'$ref': 'div-appearance-transition.json', '$description': 'translations.json#/div_base_transition_in'}, 'transition_change': {'$ref': 'div-change-transition.json', '$description': 'translations.json#/div_base_transition_change'}, 'transition_out': {'$ref': 'div-appearance-transition.json', '$description': 'translations.json#/div_base_transition_out'}, 'selected_actions': {'type': 'array', 'items': {'$ref': 'div-action.json'}, 'minItems': 1, '$description': 'translations.json#/div_base_selected_actions'}, 'focus': {'$ref': 'div-focus.json', '$description': 'translations.json#/div_base_focus', 'platforms': ['android', 'ios']}, 'visibility': {'$ref': 'div-visibility.json', '$description': 'translations.json#/div_base_visibility', 'default_value': 'visible'}, 'transform': {'$ref': 'div-transform.json', '$description': 'translations.json#/div_base_transform'}}, '$schema': 'http://json-schema.org/draft-07/schema'}, {'properties': {'type': {'type': 'string', 'enum': ['input']}, 'font_size': {'type': 'integer', 'constraint': 'number >= 0'}, 'font_size_unit': {'type': 'string', 'enum': ['dp', 'sp', 'px'], '$description': 'translations.json#/div_size_unit', 'platforms': ['android', 'ios'], '$schema': 'http://json-schema.org/draft-07/schema'}, 'font_family': {'type': 'string', 'minLength': 1, 'clientMinLength': 1}, 'font_weight': {'type': 'string', 'enum': ['light', 'medium', 'regular', 'bold'], '$schema': 'http://json-schema.org/draft-07/schema'}, 'text_color': {'type': 'string', 'format': 'color'}, 'text_variable': {'supports_expressions': False, '$ref': 'common.json#/non_empty_string', '$schema': 'http://json-schema.org/draft-07/schema'}, 'text_alignment_horizontal': {'type': 'string', 'enum': ['left', 'center', 'right', 'start', 'end'], '$schema': 'http://json-schema.org/draft-07/schema'}, 'text_alignment_vertical': {'type': 'string', 'enum': ['top', 'center', 'bottom', 'baseline'], '$schema': 'http://json-schema.org/draft-07/schema'}, 'line_height': {'type': 'integer', 'constraint': 'number >= 0'}, 'max_visible_lines': {'type': 'integer', 'constraint': 'number > 0'}, 'letter_spacing': {'type': 'number', 'default_value': '0', '$description': 'translations.json#/div_input_letter_spacing'}, 'hint_text': {'type': 'string', 'minLength': 1, 'clientMinLength': 1}, 'hint_color': {'type': 'string', 'format': 'color'}, 'highlight_color': {'type': 'string', 'format': 'color'}, 'native_interface': {'type': 'object', 'properties': {'color': {'$ref': 'common.json#/color', '$description': 'translations.json#/div_input_native_interface_color'}}, 'required': ['color']}, 'keyboard_type': {'type': 'string', 'enum': ['single_line_text', 'multi_line_text', 'phone', 'number', 'email', 'uri'], 'default_value': 'multi_line_text', '$description': 'translations.json#/div_input_keyboard_type'}, 'select_all_on_focus': {'oneOf': [{'type': 'boolean'}, {'type': 'integer', 'enum': [0, 1]}]}, 'mask': {'anyOf': [{'$ref': 'div-fixed-length-input-mask.json', '$description': 'translations.json#/div_input_mask_fixed_length'}, {'$ref': 'div-currency-input-mask.json', '$description': 'translations.json#/div_input_mask_currency'}, {'$ref': 'div-phone-input-mask.json', '$description': 'translations.json#/div_input_mask_phone', 'platforms': ['android', 'ios']}], '$schema': 'http://json-schema.org/draft-07/schema'}, 'validators': {'type': 'array', '$description': 'translations.json#/div_input_validators', 'platforms': ['android', 'ios'], 'items': {'anyOf': [{'$ref': 'div-input-validator-regex.json', '$description': 'translations.json#/div_input_validators_regex'}, {'$ref': 'div-input-validator-expression.json', '$description': 'translations.json#/div_input_validators_expression'}], '$schema': 'http://json-schema.org/draft-07/schema'}}}}], 'required': ['type', 'text_variable'], '$schema': 'http://json-schema.org/draft-07/schema'}, rule='required')
 return data

def validate_div_input_validator_json(data, custom_formats={}, name_prefix=None):
 data_any_of_count15 = 0
 if not data_any_of_count15:
  try:
   validate_div_input_validator_regex_json(data, custom_formats, (name_prefix or "data") + "")
   data_any_of_count15 += 1
  except JsonSchemaValueException: pass
 if not data_any_of_count15:
  try:
   validate_div_input_validator_expression_json(data, custom_formats, (name_prefix or "data") + "")
   data_any_of_count15 += 1
  except JsonSchemaValueException: pass
 if not data_any_of_count15:
  if not (isinstance(data, str) and '@' in data):
   raise JsonSchemaValueException("" + (name_prefix or "data") + " cannot be validated by any definition", value=data, name="" + (name_prefix or "data") + "", definition={'anyOf': [{'$description': 'translations.json#/div_input_validators_regex', 'allOf': [{'$ref': 'div-input-validator-base.json'}, {'properties': {'type': {'type': 'string', 'enum': ['regex']}, 'pattern': {'$ref': 'common.json#/non_empty_string', '$description': 'translations.json#/div_input_validators_regex_pattern'}}}], 'required': ['type', 'pattern', 'label_id', 'variable'], '$schema': 'http://json-schema.org/draft-07/schema'}, {'$description': 'translations.json#/div_input_validators_expression', 'allOf': [{'$ref': 'div-input-validator-base.json'}, {'properties': {'type': {'type': 'string', 'enum': ['expression']}, 'condition': {'$ref': 'common.json#/boolean_int', '$description': 'translations.json#/div_input_validators_expression_condition'}}}], 'required': ['type', 'condition', 'label_id', 'variable'], '$schema': 'http://json-schema.org/draft-07/schema'}], '$schema': 'http://json-schema.org/draft-07/schema'}, rule='anyOf')
 return data

def validate_div_input_validator_expression_json(data, custom_formats={}, name_prefix=None):
 validate_div_input_validator_base_json(data, custom_formats, (name_prefix or "data") + "")
 data_is_dict = isinstance(data, dict)
 if data_is_dict:
  data_keys = set(data.keys())
  if "type" in data_keys:
   data_keys.remove("type")
   data__type = data["type"]
   if not isinstance(data__type, (str)):
    if not (isinstance(data__type, str) and '@' in data__type):
     raise JsonSchemaValueException("" + (name_prefix or "data") + ".type must be string", value=data__type, name="" + (name_prefix or "data") + ".type", definition={'type': 'string', 'enum': ['expression']}, rule='type')
   if data__type not in ['expression']:
    if not (isinstance(data__type, str) and '@' in data__type):
     raise JsonSchemaValueException("" + (name_prefix or "data") + ".type must be one of ['expression']", value=data__type, name="" + (name_prefix or "data") + ".type", definition={'type': 'string', 'enum': ['expression']}, rule='enum')
  if "condition" in data_keys:
   data_keys.remove("condition")
   data__condition = data["condition"]
   validate_common_json__boolean_int(data__condition, custom_formats, (name_prefix or "data") + ".condition")
 data_is_dict = isinstance(data, dict)
 if data_is_dict:
  data__missing_keys = set(['type', 'condition', 'label_id', 'variable']) - data.keys()
  if data__missing_keys:
   if not (isinstance(data, str) and '@' in data):
    raise JsonSchemaValueException("" + (name_prefix or "data") + " must contain " + (str(sorted(data__missing_keys)) + " properties"), value=data, name="" + (name_prefix or "data") + "", definition={'$description': 'translations.json#/div_input_validators_expression', 'allOf': [{'type': 'object', 'properties': {'label_id': {'$ref': 'common.json#/non_empty_string', '$description': 'translations.json#/div_input_validators_label_id'}, 'allow_empty': {'$ref': 'common.json#/boolean_int', 'default_value': 'false', '$description': 'translations.json#/div_input_validators_allow_empty'}, 'variable': {'$ref': 'div-variable-name.json', '$description': 'translations.json#/div_input_validators_variable'}}, '$schema': 'http://json-schema.org/draft-07/schema'}, {'properties': {'type': {'type': 'string', 'enum': ['expression']}, 'condition': {'oneOf': [{'type': 'boolean'}, {'type': 'integer', 'enum': [0, 1]}]}}}], 'required': ['type', 'condition', 'label_id', 'variable'], '$schema': 'http://json-schema.org/draft-07/schema'}, rule='required')
 return data

def validate_div_input_validator_base_json(data, custom_formats={}, name_prefix=None):
 if not isinstance(data, (dict)):
  if not (isinstance(data, str) and '@' in data):
   raise JsonSchemaValueException("" + (name_prefix or "data") + " must be object", value=data, name="" + (name_prefix or "data") + "", definition={'type': 'object', 'properties': {'label_id': {'type': 'string', 'minLength': 1, 'clientMinLength': 1}, 'allow_empty': {'oneOf': [{'type': 'boolean'}, {'type': 'integer', 'enum': [0, 1]}]}, 'variable': {'supports_expressions': False, '$ref': 'common.json#/non_empty_string', '$schema': 'http://json-schema.org/draft-07/schema'}}, '$schema': 'http://json-schema.org/draft-07/schema'}, rule='type')
 data_is_dict = isinstance(data, dict)
 if data_is_dict:
  data_keys = set(data.keys())
  if "label_id" in data_keys:
   data_keys.remove("label_id")
   data__labelid = data["label_id"]
   validate_common_json__non_empty_string(data__labelid, custom_formats, (name_prefix or "data") + ".label_id")
  if "allow_empty" in data_keys:
   data_keys.remove("allow_empty")
   data__allowempty = data["allow_empty"]
   validate_common_json__boolean_int(data__allowempty, custom_formats, (name_prefix or "data") + ".allow_empty")
  if "variable" in data_keys:
   data_keys.remove("variable")
   data__variable = data["variable"]
   validate_div_variable_name_json(data__variable, custom_formats, (name_prefix or "data") + ".variable")
 return data

def validate_div_input_validator_regex_json(data, custom_formats={}, name_prefix=None):
 validate_div_input_validator_base_json(data, custom_formats, (name_prefix or "data") + "")
 data_is_dict = isinstance(data, dict)
 if data_is_dict:
  data_keys = set(data.keys())
  if "type" in data_keys:
   data_keys.remove("type")
   data__type = data["type"]
   if not isinstance(data__type, (str)):
    if not (isinstance(data__type, str) and '@' in data__type):
     raise JsonSchemaValueException("" + (name_prefix or "data") + ".type must be string", value=data__type, name="" + (name_prefix or "data") + ".type", definition={'type': 'string', 'enum': ['regex']}, rule='type')
   if data__type not in ['regex']:
    if not (isinstance(data__type, str) and '@' in data__type):
     raise JsonSchemaValueException("" + (name_prefix or "data") + ".type must be one of ['regex']", value=data__type, name="" + (name_prefix or "data") + ".type", definition={'type': 'string', 'enum': ['regex']}, rule='enum')
  if "pattern" in data_keys:
   data_keys.remove("pattern")
   data__pattern = data["pattern"]
   validate_common_json__non_empty_string(data__pattern, custom_formats, (name_prefix or "data") + ".pattern")
 data_is_dict = isinstance(data, dict)
 if data_is_dict:
  data__missing_keys = set(['type', 'pattern', 'label_id', 'variable']) - data.keys()
  if data__missing_keys:
   if not (isinstance(data, str) and '@' in data):
    raise JsonSchemaValueException("" + (name_prefix or "data") + " must contain " + (str(sorted(data__missing_keys)) + " properties"), value=data, name="" + (name_prefix or "data") + "", definition={'$description': 'translations.json#/div_input_validators_regex', 'allOf': [{'type': 'object', 'properties': {'label_id': {'$ref': 'common.json#/non_empty_string', '$description': 'translations.json#/div_input_validators_label_id'}, 'allow_empty': {'$ref': 'common.json#/boolean_int', 'default_value': 'false', '$description': 'translations.json#/div_input_validators_allow_empty'}, 'variable': {'$ref': 'div-variable-name.json', '$description': 'translations.json#/div_input_validators_variable'}}, '$schema': 'http://json-schema.org/draft-07/schema'}, {'properties': {'type': {'type': 'string', 'enum': ['regex']}, 'pattern': {'type': 'string', 'minLength': 1, 'clientMinLength': 1}}}], 'required': ['type', 'pattern', 'label_id', 'variable'], '$schema': 'http://json-schema.org/draft-07/schema'}, rule='required')
 return data

def validate_div_input_mask_json(data, custom_formats={}, name_prefix=None):
 data_any_of_count16 = 0
 if not data_any_of_count16:
  try:
   validate_div_fixed_length_input_mask_json(data, custom_formats, (name_prefix or "data") + "")
   data_any_of_count16 += 1
  except JsonSchemaValueException: pass
 if not data_any_of_count16:
  try:
   validate_div_currency_input_mask_json(data, custom_formats, (name_prefix or "data") + "")
   data_any_of_count16 += 1
  except JsonSchemaValueException: pass
 if not data_any_of_count16:
  try:
   validate_div_phone_input_mask_json(data, custom_formats, (name_prefix or "data") + "")
   data_any_of_count16 += 1
  except JsonSchemaValueException: pass
 if not data_any_of_count16:
  if not (isinstance(data, str) and '@' in data):
   raise JsonSchemaValueException("" + (name_prefix or "data") + " cannot be validated by any definition", value=data, name="" + (name_prefix or "data") + "", definition={'anyOf': [{'$description': 'translations.json#/div_input_mask_fixed_length', 'allOf': [{'$ref': 'div-input-mask-base.json'}, {'properties': {'type': {'type': 'string', 'enum': ['fixed_length']}, 'pattern': {'$ref': 'common.json#/non_empty_string', '$description': 'translations.json#/div_input_mask_fixed_length_pattern'}, 'pattern_elements': {'type': 'array', 'items': {'type': 'object', '$description': 'translations.json#/div_input_mask_fixed_length_pattern_elements', 'properties': {'key': {'type': 'string', 'minLength': 1, 'maxLength': 1, '$description': 'translations.json#/div_input_mask_fixed_length_pattern_elements_key'}, 'regex': {'$ref': 'common.json#/non_empty_string', '$description': 'translations.json#/div_input_mask_fixed_length_pattern_elements_regex'}, 'placeholder': {'type': 'string', 'maxLength': 1, 'default_value': '_', '$description': 'translations.json#/div_input_mask_fixed_length_pattern_elements_placeholder'}}, 'required': ['key']}, 'minItems': 1, '$description': 'translations.json#/div_input_mask_fixed_length_pattern_elements'}, 'always_visible': {'$ref': 'common.json#/boolean_int', 'default_value': 'false', '$description': 'translations.json#/div_input_mask_fixed_length_always_visible'}}}], 'required': ['type', 'pattern', 'pattern_elements'], '$schema': 'http://json-schema.org/draft-07/schema'}, {'$description': 'translations.json#/div_input_mask_currency', 'allOf': [{'$ref': 'div-input-mask-base.json'}, {'properties': {'type': {'type': 'string', 'enum': ['currency']}, 'locale': {'$ref': 'common.json#/non_empty_string', '$description': 'translations.json#/div_input_mask_currency_locale'}}}], 'required': ['type'], '$schema': 'http://json-schema.org/draft-07/schema'}, {'$description': 'translations.json#/div_input_mask_phone', 'allOf': [{'$ref': 'div-input-mask-base.json'}, {'properties': {'type': {'type': 'string', 'enum': ['phone']}}}], 'required': ['type'], '$schema': 'http://json-schema.org/draft-07/schema'}], '$schema': 'http://json-schema.org/draft-07/schema'}, rule='anyOf')
 return data

def validate_div_phone_input_mask_json(data, custom_formats={}, name_prefix=None):
 validate_div_input_mask_base_json(data, custom_formats, (name_prefix or "data") + "")
 data_is_dict = isinstance(data, dict)
 if data_is_dict:
  data_keys = set(data.keys())
  if "type" in data_keys:
   data_keys.remove("type")
   data__type = data["type"]
   if not isinstance(data__type, (str)):
    if not (isinstance(data__type, str) and '@' in data__type):
     raise JsonSchemaValueException("" + (name_prefix or "data") + ".type must be string", value=data__type, name="" + (name_prefix or "data") + ".type", definition={'type': 'string', 'enum': ['phone']}, rule='type')
   if data__type not in ['phone']:
    if not (isinstance(data__type, str) and '@' in data__type):
     raise JsonSchemaValueException("" + (name_prefix or "data") + ".type must be one of ['phone']", value=data__type, name="" + (name_prefix or "data") + ".type", definition={'type': 'string', 'enum': ['phone']}, rule='enum')
 data_is_dict = isinstance(data, dict)
 if data_is_dict:
  data__missing_keys = set(['type']) - data.keys()
  if data__missing_keys:
   if not (isinstance(data, str) and '@' in data):
    raise JsonSchemaValueException("" + (name_prefix or "data") + " must contain " + (str(sorted(data__missing_keys)) + " properties"), value=data, name="" + (name_prefix or "data") + "", definition={'$description': 'translations.json#/div_input_mask_phone', 'allOf': [{'protocol_name': 'div-input-mask-base', 'type': 'object', 'codegen': {'documentation': {'include_in_toc': True}}, 'properties': {'raw_text_variable': {'$ref': 'div-variable-name.json', '$description': 'translations.json#/div_input_mask_raw_text_variable'}}, 'required': ['raw_text_variable'], '$schema': 'http://json-schema.org/draft-07/schema'}, {'properties': {'type': {'type': 'string', 'enum': ['phone']}}}], 'required': ['type'], '$schema': 'http://json-schema.org/draft-07/schema'}, rule='required')
 return data

def validate_div_input_mask_base_json(data, custom_formats={}, name_prefix=None):
 if not isinstance(data, (dict)):
  if not (isinstance(data, str) and '@' in data):
   raise JsonSchemaValueException("" + (name_prefix or "data") + " must be object", value=data, name="" + (name_prefix or "data") + "", definition={'protocol_name': 'div-input-mask-base', 'type': 'object', 'codegen': {'documentation': {'include_in_toc': True}}, 'properties': {'raw_text_variable': {'supports_expressions': False, '$ref': 'common.json#/non_empty_string', '$schema': 'http://json-schema.org/draft-07/schema'}}, 'required': ['raw_text_variable'], '$schema': 'http://json-schema.org/draft-07/schema'}, rule='type')
 data_is_dict = isinstance(data, dict)
 if data_is_dict:
  data__missing_keys = set(['raw_text_variable']) - data.keys()
  if data__missing_keys:
   if not (isinstance(data, str) and '@' in data):
    raise JsonSchemaValueException("" + (name_prefix or "data") + " must contain " + (str(sorted(data__missing_keys)) + " properties"), value=data, name="" + (name_prefix or "data") + "", definition={'protocol_name': 'div-input-mask-base', 'type': 'object', 'codegen': {'documentation': {'include_in_toc': True}}, 'properties': {'raw_text_variable': {'supports_expressions': False, '$ref': 'common.json#/non_empty_string', '$schema': 'http://json-schema.org/draft-07/schema'}}, 'required': ['raw_text_variable'], '$schema': 'http://json-schema.org/draft-07/schema'}, rule='required')
  data_keys = set(data.keys())
  if "raw_text_variable" in data_keys:
   data_keys.remove("raw_text_variable")
   data__rawtextvariable = data["raw_text_variable"]
   validate_div_variable_name_json(data__rawtextvariable, custom_formats, (name_prefix or "data") + ".raw_text_variable")
 return data

def validate_div_currency_input_mask_json(data, custom_formats={}, name_prefix=None):
 validate_div_input_mask_base_json(data, custom_formats, (name_prefix or "data") + "")
 data_is_dict = isinstance(data, dict)
 if data_is_dict:
  data_keys = set(data.keys())
  if "type" in data_keys:
   data_keys.remove("type")
   data__type = data["type"]
   if not isinstance(data__type, (str)):
    if not (isinstance(data__type, str) and '@' in data__type):
     raise JsonSchemaValueException("" + (name_prefix or "data") + ".type must be string", value=data__type, name="" + (name_prefix or "data") + ".type", definition={'type': 'string', 'enum': ['currency']}, rule='type')
   if data__type not in ['currency']:
    if not (isinstance(data__type, str) and '@' in data__type):
     raise JsonSchemaValueException("" + (name_prefix or "data") + ".type must be one of ['currency']", value=data__type, name="" + (name_prefix or "data") + ".type", definition={'type': 'string', 'enum': ['currency']}, rule='enum')
  if "locale" in data_keys:
   data_keys.remove("locale")
   data__locale = data["locale"]
   validate_common_json__non_empty_string(data__locale, custom_formats, (name_prefix or "data") + ".locale")
 data_is_dict = isinstance(data, dict)
 if data_is_dict:
  data__missing_keys = set(['type']) - data.keys()
  if data__missing_keys:
   if not (isinstance(data, str) and '@' in data):
    raise JsonSchemaValueException("" + (name_prefix or "data") + " must contain " + (str(sorted(data__missing_keys)) + " properties"), value=data, name="" + (name_prefix or "data") + "", definition={'$description': 'translations.json#/div_input_mask_currency', 'allOf': [{'protocol_name': 'div-input-mask-base', 'type': 'object', 'codegen': {'documentation': {'include_in_toc': True}}, 'properties': {'raw_text_variable': {'$ref': 'div-variable-name.json', '$description': 'translations.json#/div_input_mask_raw_text_variable'}}, 'required': ['raw_text_variable'], '$schema': 'http://json-schema.org/draft-07/schema'}, {'properties': {'type': {'type': 'string', 'enum': ['currency']}, 'locale': {'type': 'string', 'minLength': 1, 'clientMinLength': 1}}}], 'required': ['type'], '$schema': 'http://json-schema.org/draft-07/schema'}, rule='required')
 return data

def validate_div_fixed_length_input_mask_json(data, custom_formats={}, name_prefix=None):
 validate_div_input_mask_base_json(data, custom_formats, (name_prefix or "data") + "")
 data_is_dict = isinstance(data, dict)
 if data_is_dict:
  data_keys = set(data.keys())
  if "type" in data_keys:
   data_keys.remove("type")
   data__type = data["type"]
   if not isinstance(data__type, (str)):
    if not (isinstance(data__type, str) and '@' in data__type):
     raise JsonSchemaValueException("" + (name_prefix or "data") + ".type must be string", value=data__type, name="" + (name_prefix or "data") + ".type", definition={'type': 'string', 'enum': ['fixed_length']}, rule='type')
   if data__type not in ['fixed_length']:
    if not (isinstance(data__type, str) and '@' in data__type):
     raise JsonSchemaValueException("" + (name_prefix or "data") + ".type must be one of ['fixed_length']", value=data__type, name="" + (name_prefix or "data") + ".type", definition={'type': 'string', 'enum': ['fixed_length']}, rule='enum')
  if "pattern" in data_keys:
   data_keys.remove("pattern")
   data__pattern = data["pattern"]
   validate_common_json__non_empty_string(data__pattern, custom_formats, (name_prefix or "data") + ".pattern")
  if "pattern_elements" in data_keys:
   data_keys.remove("pattern_elements")
   data__patternelements = data["pattern_elements"]
   if not isinstance(data__patternelements, (list, tuple)):
    if not (isinstance(data__patternelements, str) and '@' in data__patternelements):
     raise JsonSchemaValueException("" + (name_prefix or "data") + ".pattern_elements must be array", value=data__patternelements, name="" + (name_prefix or "data") + ".pattern_elements", definition={'type': 'array', 'items': {'type': 'object', '$description': 'translations.json#/div_input_mask_fixed_length_pattern_elements', 'properties': {'key': {'type': 'string', 'minLength': 1, 'maxLength': 1, '$description': 'translations.json#/div_input_mask_fixed_length_pattern_elements_key'}, 'regex': {'type': 'string', 'minLength': 1, 'clientMinLength': 1}, 'placeholder': {'type': 'string', 'maxLength': 1, 'default_value': '_', '$description': 'translations.json#/div_input_mask_fixed_length_pattern_elements_placeholder'}}, 'required': ['key']}, 'minItems': 1, '$description': 'translations.json#/div_input_mask_fixed_length_pattern_elements'}, rule='type')
   data__patternelements_is_list = isinstance(data__patternelements, (list, tuple))
   if data__patternelements_is_list:
    data__patternelements_len = len(data__patternelements)
    if data__patternelements_len < 1:
     if not (isinstance(data__patternelements, str) and '@' in data__patternelements):
      raise JsonSchemaValueException("" + (name_prefix or "data") + ".pattern_elements must contain at least 1 items", value=data__patternelements, name="" + (name_prefix or "data") + ".pattern_elements", definition={'type': 'array', 'items': {'type': 'object', '$description': 'translations.json#/div_input_mask_fixed_length_pattern_elements', 'properties': {'key': {'type': 'string', 'minLength': 1, 'maxLength': 1, '$description': 'translations.json#/div_input_mask_fixed_length_pattern_elements_key'}, 'regex': {'type': 'string', 'minLength': 1, 'clientMinLength': 1}, 'placeholder': {'type': 'string', 'maxLength': 1, 'default_value': '_', '$description': 'translations.json#/div_input_mask_fixed_length_pattern_elements_placeholder'}}, 'required': ['key']}, 'minItems': 1, '$description': 'translations.json#/div_input_mask_fixed_length_pattern_elements'}, rule='minItems')
    for data__patternelements_x, data__patternelements_item in enumerate(data__patternelements):
     if not isinstance(data__patternelements_item, (dict)):
      if not (isinstance(data__patternelements_item, str) and '@' in data__patternelements_item):
       raise JsonSchemaValueException("" + (name_prefix or "data") + ".pattern_elements[{data__patternelements_x}]".format(**locals()) + " must be object", value=data__patternelements_item, name="" + (name_prefix or "data") + ".pattern_elements[{data__patternelements_x}]".format(**locals()) + "", definition={'type': 'object', '$description': 'translations.json#/div_input_mask_fixed_length_pattern_elements', 'properties': {'key': {'type': 'string', 'minLength': 1, 'maxLength': 1, '$description': 'translations.json#/div_input_mask_fixed_length_pattern_elements_key'}, 'regex': {'type': 'string', 'minLength': 1, 'clientMinLength': 1}, 'placeholder': {'type': 'string', 'maxLength': 1, 'default_value': '_', '$description': 'translations.json#/div_input_mask_fixed_length_pattern_elements_placeholder'}}, 'required': ['key']}, rule='type')
     data__patternelements_item_is_dict = isinstance(data__patternelements_item, dict)
     if data__patternelements_item_is_dict:
      data__patternelements_item__missing_keys = set(['key']) - data__patternelements_item.keys()
      if data__patternelements_item__missing_keys:
       if not (isinstance(data__patternelements_item, str) and '@' in data__patternelements_item):
        raise JsonSchemaValueException("" + (name_prefix or "data") + ".pattern_elements[{data__patternelements_x}]".format(**locals()) + " must contain " + (str(sorted(data__patternelements_item__missing_keys)) + " properties"), value=data__patternelements_item, name="" + (name_prefix or "data") + ".pattern_elements[{data__patternelements_x}]".format(**locals()) + "", definition={'type': 'object', '$description': 'translations.json#/div_input_mask_fixed_length_pattern_elements', 'properties': {'key': {'type': 'string', 'minLength': 1, 'maxLength': 1, '$description': 'translations.json#/div_input_mask_fixed_length_pattern_elements_key'}, 'regex': {'type': 'string', 'minLength': 1, 'clientMinLength': 1}, 'placeholder': {'type': 'string', 'maxLength': 1, 'default_value': '_', '$description': 'translations.json#/div_input_mask_fixed_length_pattern_elements_placeholder'}}, 'required': ['key']}, rule='required')
      data__patternelements_item_keys = set(data__patternelements_item.keys())
      if "key" in data__patternelements_item_keys:
       data__patternelements_item_keys.remove("key")
       data__patternelements_item__key = data__patternelements_item["key"]
       if not isinstance(data__patternelements_item__key, (str)):
        if not (isinstance(data__patternelements_item__key, str) and '@' in data__patternelements_item__key):
         raise JsonSchemaValueException("" + (name_prefix or "data") + ".pattern_elements[{data__patternelements_x}].key".format(**locals()) + " must be string", value=data__patternelements_item__key, name="" + (name_prefix or "data") + ".pattern_elements[{data__patternelements_x}].key".format(**locals()) + "", definition={'type': 'string', 'minLength': 1, 'maxLength': 1, '$description': 'translations.json#/div_input_mask_fixed_length_pattern_elements_key'}, rule='type')
       if isinstance(data__patternelements_item__key, str):
        data__patternelements_item__key_len = len(data__patternelements_item__key)
        if data__patternelements_item__key_len < 1:
         if not (isinstance(data__patternelements_item__key, str) and '@' in data__patternelements_item__key):
          raise JsonSchemaValueException("" + (name_prefix or "data") + ".pattern_elements[{data__patternelements_x}].key".format(**locals()) + " must be longer than or equal to 1 characters", value=data__patternelements_item__key, name="" + (name_prefix or "data") + ".pattern_elements[{data__patternelements_x}].key".format(**locals()) + "", definition={'type': 'string', 'minLength': 1, 'maxLength': 1, '$description': 'translations.json#/div_input_mask_fixed_length_pattern_elements_key'}, rule='minLength')
        if data__patternelements_item__key_len > 1:
         if not (isinstance(data__patternelements_item__key, str) and '@' in data__patternelements_item__key):
          raise JsonSchemaValueException("" + (name_prefix or "data") + ".pattern_elements[{data__patternelements_x}].key".format(**locals()) + " must be shorter than or equal to 1 characters", value=data__patternelements_item__key, name="" + (name_prefix or "data") + ".pattern_elements[{data__patternelements_x}].key".format(**locals()) + "", definition={'type': 'string', 'minLength': 1, 'maxLength': 1, '$description': 'translations.json#/div_input_mask_fixed_length_pattern_elements_key'}, rule='maxLength')
      if "regex" in data__patternelements_item_keys:
       data__patternelements_item_keys.remove("regex")
       data__patternelements_item__regex = data__patternelements_item["regex"]
       validate_common_json__non_empty_string(data__patternelements_item__regex, custom_formats, (name_prefix or "data") + ".pattern_elements[{data__patternelements_x}].regex".format(**locals()))
      if "placeholder" in data__patternelements_item_keys:
       data__patternelements_item_keys.remove("placeholder")
       data__patternelements_item__placeholder = data__patternelements_item["placeholder"]
       if not isinstance(data__patternelements_item__placeholder, (str)):
        if not (isinstance(data__patternelements_item__placeholder, str) and '@' in data__patternelements_item__placeholder):
         raise JsonSchemaValueException("" + (name_prefix or "data") + ".pattern_elements[{data__patternelements_x}].placeholder".format(**locals()) + " must be string", value=data__patternelements_item__placeholder, name="" + (name_prefix or "data") + ".pattern_elements[{data__patternelements_x}].placeholder".format(**locals()) + "", definition={'type': 'string', 'maxLength': 1, 'default_value': '_', '$description': 'translations.json#/div_input_mask_fixed_length_pattern_elements_placeholder'}, rule='type')
       if isinstance(data__patternelements_item__placeholder, str):
        data__patternelements_item__placeholder_len = len(data__patternelements_item__placeholder)
        if data__patternelements_item__placeholder_len > 1:
         if not (isinstance(data__patternelements_item__placeholder, str) and '@' in data__patternelements_item__placeholder):
          raise JsonSchemaValueException("" + (name_prefix or "data") + ".pattern_elements[{data__patternelements_x}].placeholder".format(**locals()) + " must be shorter than or equal to 1 characters", value=data__patternelements_item__placeholder, name="" + (name_prefix or "data") + ".pattern_elements[{data__patternelements_x}].placeholder".format(**locals()) + "", definition={'type': 'string', 'maxLength': 1, 'default_value': '_', '$description': 'translations.json#/div_input_mask_fixed_length_pattern_elements_placeholder'}, rule='maxLength')
  if "always_visible" in data_keys:
   data_keys.remove("always_visible")
   data__alwaysvisible = data["always_visible"]
   validate_common_json__boolean_int(data__alwaysvisible, custom_formats, (name_prefix or "data") + ".always_visible")
 data_is_dict = isinstance(data, dict)
 if data_is_dict:
  data__missing_keys = set(['type', 'pattern', 'pattern_elements']) - data.keys()
  if data__missing_keys:
   if not (isinstance(data, str) and '@' in data):
    raise JsonSchemaValueException("" + (name_prefix or "data") + " must contain " + (str(sorted(data__missing_keys)) + " properties"), value=data, name="" + (name_prefix or "data") + "", definition={'$description': 'translations.json#/div_input_mask_fixed_length', 'allOf': [{'protocol_name': 'div-input-mask-base', 'type': 'object', 'codegen': {'documentation': {'include_in_toc': True}}, 'properties': {'raw_text_variable': {'$ref': 'div-variable-name.json', '$description': 'translations.json#/div_input_mask_raw_text_variable'}}, 'required': ['raw_text_variable'], '$schema': 'http://json-schema.org/draft-07/schema'}, {'properties': {'type': {'type': 'string', 'enum': ['fixed_length']}, 'pattern': {'type': 'string', 'minLength': 1, 'clientMinLength': 1}, 'pattern_elements': {'type': 'array', 'items': {'type': 'object', '$description': 'translations.json#/div_input_mask_fixed_length_pattern_elements', 'properties': {'key': {'type': 'string', 'minLength': 1, 'maxLength': 1, '$description': 'translations.json#/div_input_mask_fixed_length_pattern_elements_key'}, 'regex': {'type': 'string', 'minLength': 1, 'clientMinLength': 1}, 'placeholder': {'type': 'string', 'maxLength': 1, 'default_value': '_', '$description': 'translations.json#/div_input_mask_fixed_length_pattern_elements_placeholder'}}, 'required': ['key']}, 'minItems': 1, '$description': 'translations.json#/div_input_mask_fixed_length_pattern_elements'}, 'always_visible': {'oneOf': [{'type': 'boolean'}, {'type': 'integer', 'enum': [0, 1]}]}}}], 'required': ['type', 'pattern', 'pattern_elements'], '$schema': 'http://json-schema.org/draft-07/schema'}, rule='required')
 return data

def validate_div_input_json__definitions_native_interface(data, custom_formats={}, name_prefix=None):
 if not isinstance(data, (dict)):
  if not (isinstance(data, str) and '@' in data):
   raise JsonSchemaValueException("" + (name_prefix or "data") + " must be object", value=data, name="" + (name_prefix or "data") + "", definition={'type': 'object', 'properties': {'color': {'type': 'string', 'format': 'color'}}, 'required': ['color']}, rule='type')
 data_is_dict = isinstance(data, dict)
 if data_is_dict:
  data__missing_keys = set(['color']) - data.keys()
  if data__missing_keys:
   if not (isinstance(data, str) and '@' in data):
    raise JsonSchemaValueException("" + (name_prefix or "data") + " must contain " + (str(sorted(data__missing_keys)) + " properties"), value=data, name="" + (name_prefix or "data") + "", definition={'type': 'object', 'properties': {'color': {'type': 'string', 'format': 'color'}}, 'required': ['color']}, rule='required')
  data_keys = set(data.keys())
  if "color" in data_keys:
   data_keys.remove("color")
   data__color = data["color"]
   validate_common_json__color(data__color, custom_formats, (name_prefix or "data") + ".color")
 return data

def validate_div_slider_json(data, custom_formats={}, name_prefix=None):
 validate_div_base_json(data, custom_formats, (name_prefix or "data") + "")
 data_is_dict = isinstance(data, dict)
 if data_is_dict:
  data_keys = set(data.keys())
  if "type" in data_keys:
   data_keys.remove("type")
   data__type = data["type"]
   if not isinstance(data__type, (str)):
    if not (isinstance(data__type, str) and '@' in data__type):
     raise JsonSchemaValueException("" + (name_prefix or "data") + ".type must be string", value=data__type, name="" + (name_prefix or "data") + ".type", definition={'type': 'string', 'enum': ['slider']}, rule='type')
   if data__type not in ['slider']:
    if not (isinstance(data__type, str) and '@' in data__type):
     raise JsonSchemaValueException("" + (name_prefix or "data") + ".type must be one of ['slider']", value=data__type, name="" + (name_prefix or "data") + ".type", definition={'type': 'string', 'enum': ['slider']}, rule='enum')
  if "min_value" in data_keys:
   data_keys.remove("min_value")
   data__minvalue = data["min_value"]
   if not isinstance(data__minvalue, (int)) and not (isinstance(data__minvalue, float) and data__minvalue.is_integer()) or isinstance(data__minvalue, bool):
    if not (isinstance(data__minvalue, str) and '@' in data__minvalue):
     raise JsonSchemaValueException("" + (name_prefix or "data") + ".min_value must be integer", value=data__minvalue, name="" + (name_prefix or "data") + ".min_value", definition={'type': 'integer', 'default_value': '0', '$description': 'translations.json#/div_slider_min_value'}, rule='type')
  if "max_value" in data_keys:
   data_keys.remove("max_value")
   data__maxvalue = data["max_value"]
   if not isinstance(data__maxvalue, (int)) and not (isinstance(data__maxvalue, float) and data__maxvalue.is_integer()) or isinstance(data__maxvalue, bool):
    if not (isinstance(data__maxvalue, str) and '@' in data__maxvalue):
     raise JsonSchemaValueException("" + (name_prefix or "data") + ".max_value must be integer", value=data__maxvalue, name="" + (name_prefix or "data") + ".max_value", definition={'type': 'integer', 'default_value': '100', '$description': 'translations.json#/div_slider_max_value'}, rule='type')
  if "thumb_value_variable" in data_keys:
   data_keys.remove("thumb_value_variable")
   data__thumbvaluevariable = data["thumb_value_variable"]
   validate_div_variable_name_json(data__thumbvaluevariable, custom_formats, (name_prefix or "data") + ".thumb_value_variable")
  if "thumb_secondary_value_variable" in data_keys:
   data_keys.remove("thumb_secondary_value_variable")
   data__thumbsecondaryvaluevariable = data["thumb_secondary_value_variable"]
   validate_div_variable_name_json(data__thumbsecondaryvaluevariable, custom_formats, (name_prefix or "data") + ".thumb_secondary_value_variable")
  if "thumb_style" in data_keys:
   data_keys.remove("thumb_style")
   data__thumbstyle = data["thumb_style"]
   validate_div_drawable_json(data__thumbstyle, custom_formats, (name_prefix or "data") + ".thumb_style")
  if "thumb_secondary_style" in data_keys:
   data_keys.remove("thumb_secondary_style")
   data__thumbsecondarystyle = data["thumb_secondary_style"]
   validate_div_drawable_json(data__thumbsecondarystyle, custom_formats, (name_prefix or "data") + ".thumb_secondary_style")
  if "thumb_text_style" in data_keys:
   data_keys.remove("thumb_text_style")
   data__thumbtextstyle = data["thumb_text_style"]
   validate_div_slider_json__definitions_text_style(data__thumbtextstyle, custom_formats, (name_prefix or "data") + ".thumb_text_style")
  if "thumb_secondary_text_style" in data_keys:
   data_keys.remove("thumb_secondary_text_style")
   data__thumbsecondarytextstyle = data["thumb_secondary_text_style"]
   validate_div_slider_json__definitions_text_style(data__thumbsecondarytextstyle, custom_formats, (name_prefix or "data") + ".thumb_secondary_text_style")
  if "track_active_style" in data_keys:
   data_keys.remove("track_active_style")
   data__trackactivestyle = data["track_active_style"]
   validate_div_drawable_json(data__trackactivestyle, custom_formats, (name_prefix or "data") + ".track_active_style")
  if "tick_mark_active_style" in data_keys:
   data_keys.remove("tick_mark_active_style")
   data__tickmarkactivestyle = data["tick_mark_active_style"]
   validate_div_drawable_json(data__tickmarkactivestyle, custom_formats, (name_prefix or "data") + ".tick_mark_active_style")
  if "track_inactive_style" in data_keys:
   data_keys.remove("track_inactive_style")
   data__trackinactivestyle = data["track_inactive_style"]
   validate_div_drawable_json(data__trackinactivestyle, custom_formats, (name_prefix or "data") + ".track_inactive_style")
  if "tick_mark_inactive_style" in data_keys:
   data_keys.remove("tick_mark_inactive_style")
   data__tickmarkinactivestyle = data["tick_mark_inactive_style"]
   validate_div_drawable_json(data__tickmarkinactivestyle, custom_formats, (name_prefix or "data") + ".tick_mark_inactive_style")
  if "ranges" in data_keys:
   data_keys.remove("ranges")
   data__ranges = data["ranges"]
   if not isinstance(data__ranges, (list, tuple)):
    if not (isinstance(data__ranges, str) and '@' in data__ranges):
     raise JsonSchemaValueException("" + (name_prefix or "data") + ".ranges must be array", value=data__ranges, name="" + (name_prefix or "data") + ".ranges", definition={'type': 'array', 'items': {'type': 'object', 'properties': {'start': {'type': 'integer', '$description': 'translations.json#/div_slider_range_start'}, 'end': {'type': 'integer', '$description': 'translations.json#/div_slider_range_end'}, 'track_active_style': {'$ref': 'div-drawable.json', '$description': 'translations.json#/div_slider_track_active_style'}, 'track_inactive_style': {'$ref': 'div-drawable.json', '$description': 'translations.json#/div_slider_track_inactive_style'}, 'margins': {'$ref': 'div-edge-insets.json', '$description': 'translations.json#/div_slider_range_margins'}}}, 'minItems': 1, '$description': 'translations.json#/div_slider_ranges', 'platforms': ['android', 'ios']}, rule='type')
   data__ranges_is_list = isinstance(data__ranges, (list, tuple))
   if data__ranges_is_list:
    data__ranges_len = len(data__ranges)
    if data__ranges_len < 1:
     if not (isinstance(data__ranges, str) and '@' in data__ranges):
      raise JsonSchemaValueException("" + (name_prefix or "data") + ".ranges must contain at least 1 items", value=data__ranges, name="" + (name_prefix or "data") + ".ranges", definition={'type': 'array', 'items': {'type': 'object', 'properties': {'start': {'type': 'integer', '$description': 'translations.json#/div_slider_range_start'}, 'end': {'type': 'integer', '$description': 'translations.json#/div_slider_range_end'}, 'track_active_style': {'$ref': 'div-drawable.json', '$description': 'translations.json#/div_slider_track_active_style'}, 'track_inactive_style': {'$ref': 'div-drawable.json', '$description': 'translations.json#/div_slider_track_inactive_style'}, 'margins': {'$ref': 'div-edge-insets.json', '$description': 'translations.json#/div_slider_range_margins'}}}, 'minItems': 1, '$description': 'translations.json#/div_slider_ranges', 'platforms': ['android', 'ios']}, rule='minItems')
    for data__ranges_x, data__ranges_item in enumerate(data__ranges):
     validate_div_slider_json__definitions_range(data__ranges_item, custom_formats, (name_prefix or "data") + ".ranges[{data__ranges_x}]".format(**locals()))
  if "secondary_value_accessibility" in data_keys:
   data_keys.remove("secondary_value_accessibility")
   data__secondaryvalueaccessibility = data["secondary_value_accessibility"]
   validate_div_accessibility_json(data__secondaryvalueaccessibility, custom_formats, (name_prefix or "data") + ".secondary_value_accessibility")
 data_is_dict = isinstance(data, dict)
 if data_is_dict:
  data__missing_keys = set(['type', 'thumb_style', 'track_active_style', 'track_inactive_style']) - data.keys()
  if data__missing_keys:
   if not (isinstance(data, str) and '@' in data):
    raise JsonSchemaValueException("" + (name_prefix or "data") + " must contain " + (str(sorted(data__missing_keys)) + " properties"), value=data, name="" + (name_prefix or "data") + "", definition={'java_extends': 'DivBlockWithId', '$description': 'translations.json#/div_slider', 'definitions': {'text_style': {'type': 'object', 'properties': {'font_size': {'type': 'integer', 'constraint': 'number >= 0'}, 'font_size_unit': {'type': 'string', 'enum': ['dp', 'sp', 'px'], '$description': 'translations.json#/div_size_unit', 'platforms': ['android', 'ios'], '$schema': 'http://json-schema.org/draft-07/schema'}, 'font_weight': {'type': 'string', 'enum': ['light', 'medium', 'regular', 'bold'], '$schema': 'http://json-schema.org/draft-07/schema'}, 'text_color': {'type': 'string', 'format': 'color'}, 'offset': {'type': 'object', '$description': 'translations.json#/div_point', 'properties': {'x': {'$ref': 'div-dimension.json', '$description': 'translations.json#/div_point_x'}, 'y': {'$ref': 'div-dimension.json', '$description': 'translations.json#/div_point_y'}}, 'required': ['x', 'y'], '$schema': 'http://json-schema.org/draft-07/schema'}}, 'required': ['font_size']}, 'range': {'type': 'object', 'properties': {'start': {'type': 'integer', '$description': 'translations.json#/div_slider_range_start'}, 'end': {'type': 'integer', '$description': 'translations.json#/div_slider_range_end'}, 'track_active_style': {'anyOf': [{'$ref': 'div-shape-drawable.json', '$description': 'translations.json#/div_shape_drawable'}], '$schema': 'http://json-schema.org/draft-07/schema'}, 'track_inactive_style': {'anyOf': [{'$ref': 'div-shape-drawable.json', '$description': 'translations.json#/div_shape_drawable'}], '$schema': 'http://json-schema.org/draft-07/schema'}, 'margins': {'type': 'object', '$description': 'translations.json#/div_edge_insets', 'properties': {'left': {'$ref': 'common.json#/non_negative_integer', 'default_value': '0', '$description': 'translations.json#/div_edge_insets_left'}, 'right': {'$ref': 'common.json#/non_negative_integer', 'default_value': '0', '$description': 'translations.json#/div_edge_insets_right'}, 'top': {'$ref': 'common.json#/non_negative_integer', 'default_value': '0', '$description': 'translations.json#/div_edge_insets_top'}, 'bottom': {'$ref': 'common.json#/non_negative_integer', 'default_value': '0', '$description': 'translations.json#/div_edge_insets_bottom'}, 'start': {'$ref': 'common.json#/non_negative_integer', '$description': 'translations.json#/div_edge_insets_start', 'platforms': []}, 'end': {'$ref': 'common.json#/non_negative_integer', '$description': 'translations.json#/div_edge_insets_end', 'platforms': []}, 'unit': {'$ref': 'div-size-unit.json', 'default_value': 'dp'}}, '$schema': 'http://json-schema.org/draft-07/schema'}}}}, 'allOf': [{'protocol_name': 'div-base', 'codegen': {'swift': {'super_protocol': 'DivBlockModeling'}, 'documentation': {'include_in_toc': True}}, 'type': 'object', 'properties': {'id': {'$ref': 'common.json#/non_empty_string', 'supports_expressions': False, '$description': 'translations.json#/div_base_id'}, 'border': {'$ref': 'div-border.json', '$description': 'translations.json#/div_base_border'}, 'width': {'$ref': 'div-size.json', 'default_value': '{"type": "match_parent"}', '$description': 'translations.json#/div_base_width'}, 'height': {'$ref': 'div-size.json', 'default_value': '{"type": "wrap_content"}', '$description': 'translations.json#/div_base_height'}, 'background': {'type': 'array', 'items': {'$ref': 'div-background.json'}, 'minItems': 1, '$description': 'translations.json#/div_base_background'}, 'paddings': {'$ref': 'div-edge-insets.json', '$description': 'translations.json#/div_base_paddings'}, 'margins': {'$ref': 'div-edge-insets.json', '$description': 'translations.json#/div_base_margins'}, 'alpha': {'type': 'number', 'default_value': '1.0', 'constraint': 'number >= 0.0 && number <= 1.0', '$description': 'translations.json#/div_base_alpha'}, 'alignment_vertical': {'$ref': 'div-alignment-vertical.json', '$description': 'translations.json#/div_base_alignment_vertical'}, 'alignment_horizontal': {'$ref': 'div-alignment-horizontal.json', '$description': 'translations.json#/div_base_alignment_horizontal'}, 'row_span': {'$ref': 'common.json#/non_negative_integer', '$description': 'translations.json#/div_base_row_span'}, 'column_span': {'$ref': 'common.json#/non_negative_integer', '$description': 'translations.json#/div_base_column_span'}, 'visibility_action': {'$ref': 'div-visibility-action.json', '$description': 'translations.json#/div_base_visibility_action'}, 'visibility_actions': {'type': 'array', 'items': {'$ref': 'div-visibility-action.json'}, 'minItems': 1, '$description': 'translations.json#/div_base_visibility_actions'}, 'disappear_actions': {'type': 'array', 'items': {'$ref': 'div-disappear-action.json'}, 'minItems': 1, '$description': 'translations.json#/div_base_disappear_actions'}, 'tooltips': {'type': 'array', 'items': {'$ref': 'div-tooltip.json'}, 'minItems': 1, '$description': 'translations.json#/div_base_tooltips'}, 'accessibility': {'$ref': 'div-accessibility.json', '$description': 'translations.json#/div_base_accessibility'}, 'extensions': {'type': 'array', 'items': {'$ref': 'div-extension.json'}, 'minItems': 1, '$description': 'translations.json#/div_base_extensions'}, 'transition_triggers': {'type': 'array', 'items': {'$ref': 'div-transition-trigger.json'}, 'minItems': 1, 'supports_expressions': False, '$description': 'translations.json#/div_base_transition_triggers'}, 'transition_in': {'$ref': 'div-appearance-transition.json', '$description': 'translations.json#/div_base_transition_in'}, 'transition_change': {'$ref': 'div-change-transition.json', '$description': 'translations.json#/div_base_transition_change'}, 'transition_out': {'$ref': 'div-appearance-transition.json', '$description': 'translations.json#/div_base_transition_out'}, 'selected_actions': {'type': 'array', 'items': {'$ref': 'div-action.json'}, 'minItems': 1, '$description': 'translations.json#/div_base_selected_actions'}, 'focus': {'$ref': 'div-focus.json', '$description': 'translations.json#/div_base_focus', 'platforms': ['android', 'ios']}, 'visibility': {'$ref': 'div-visibility.json', '$description': 'translations.json#/div_base_visibility', 'default_value': 'visible'}, 'transform': {'$ref': 'div-transform.json', '$description': 'translations.json#/div_base_transform'}}, '$schema': 'http://json-schema.org/draft-07/schema'}, {'properties': {'type': {'type': 'string', 'enum': ['slider']}, 'min_value': {'type': 'integer', 'default_value': '0', '$description': 'translations.json#/div_slider_min_value'}, 'max_value': {'type': 'integer', 'default_value': '100', '$description': 'translations.json#/div_slider_max_value'}, 'thumb_value_variable': {'supports_expressions': False, '$ref': 'common.json#/non_empty_string', '$schema': 'http://json-schema.org/draft-07/schema'}, 'thumb_secondary_value_variable': {'supports_expressions': False, '$ref': 'common.json#/non_empty_string', '$schema': 'http://json-schema.org/draft-07/schema'}, 'thumb_style': {'anyOf': [{'$ref': 'div-shape-drawable.json', '$description': 'translations.json#/div_shape_drawable'}], '$schema': 'http://json-schema.org/draft-07/schema'}, 'thumb_secondary_style': {'anyOf': [{'$ref': 'div-shape-drawable.json', '$description': 'translations.json#/div_shape_drawable'}], '$schema': 'http://json-schema.org/draft-07/schema'}, 'thumb_text_style': {'type': 'object', 'properties': {'font_size': {'$ref': 'common.json#/non_negative_integer', '$description': 'translations.json#/div_font_size'}, 'font_size_unit': {'$ref': 'div-size-unit.json', 'default_value': 'sp', 'platforms': ['android']}, 'font_weight': {'$ref': 'div-font-weight.json', 'default_value': 'regular', '$description': 'translations.json#/div_font_weight'}, 'text_color': {'$ref': 'common.json#/color', 'default_value': '#FF000000', '$description': 'translations.json#/div_text_color'}, 'offset': {'$ref': 'div-point.json', '$description': 'translations.json#/div_slider_text_style_offset'}}, 'required': ['font_size']}, 'thumb_secondary_text_style': {'type': 'object', 'properties': {'font_size': {'$ref': 'common.json#/non_negative_integer', '$description': 'translations.json#/div_font_size'}, 'font_size_unit': {'$ref': 'div-size-unit.json', 'default_value': 'sp', 'platforms': ['android']}, 'font_weight': {'$ref': 'div-font-weight.json', 'default_value': 'regular', '$description': 'translations.json#/div_font_weight'}, 'text_color': {'$ref': 'common.json#/color', 'default_value': '#FF000000', '$description': 'translations.json#/div_text_color'}, 'offset': {'$ref': 'div-point.json', '$description': 'translations.json#/div_slider_text_style_offset'}}, 'required': ['font_size']}, 'track_active_style': {'anyOf': [{'$ref': 'div-shape-drawable.json', '$description': 'translations.json#/div_shape_drawable'}], '$schema': 'http://json-schema.org/draft-07/schema'}, 'tick_mark_active_style': {'anyOf': [{'$ref': 'div-shape-drawable.json', '$description': 'translations.json#/div_shape_drawable'}], '$schema': 'http://json-schema.org/draft-07/schema'}, 'track_inactive_style': {'anyOf': [{'$ref': 'div-shape-drawable.json', '$description': 'translations.json#/div_shape_drawable'}], '$schema': 'http://json-schema.org/draft-07/schema'}, 'tick_mark_inactive_style': {'anyOf': [{'$ref': 'div-shape-drawable.json', '$description': 'translations.json#/div_shape_drawable'}], '$schema': 'http://json-schema.org/draft-07/schema'}, 'ranges': {'type': 'array', 'items': {'type': 'object', 'properties': {'start': {'type': 'integer', '$description': 'translations.json#/div_slider_range_start'}, 'end': {'type': 'integer', '$description': 'translations.json#/div_slider_range_end'}, 'track_active_style': {'$ref': 'div-drawable.json', '$description': 'translations.json#/div_slider_track_active_style'}, 'track_inactive_style': {'$ref': 'div-drawable.json', '$description': 'translations.json#/div_slider_track_inactive_style'}, 'margins': {'$ref': 'div-edge-insets.json', '$description': 'translations.json#/div_slider_range_margins'}}}, 'minItems': 1, '$description': 'translations.json#/div_slider_ranges', 'platforms': ['android', 'ios']}, 'secondary_value_accessibility': {'type': 'object', '$description': 'translations.json#/div_accessibility', 'properties': {'description': {'$ref': 'common.json#/non_empty_string', '$description': 'translations.json#/div_accessibility_description'}, 'type': {'type': 'string', 'enum': ['none', 'button', 'image', 'text', 'edit_text', 'header', 'tab_bar', 'list', 'select'], 'supports_expressions': False, '$description': 'translations.json#/div_accessibility_type', 'platforms': ['android', 'ios']}, 'state_description': {'$ref': 'common.json#/non_empty_string', '$description': 'translations.json#/div_accessibility_state_description', 'platforms': ['android', 'ios']}, 'hint': {'$ref': 'common.json#/non_empty_string', '$description': 'translations.json#/div_accessibility_hint', 'platforms': ['android', 'ios']}, 'mode': {'type': 'string', 'enum': ['default', 'merge', 'exclude'], 'default_value': 'default', '$description': 'translations.json#/div_accessibility_mode', 'platforms': ['android', 'ios']}, 'mute_after_action': {'$ref': 'common.json#/boolean_int', 'default_value': 'false', '$description': 'translations.json#/div_accessibility_mute_after_action', 'platforms': ['ios']}}, '$schema': 'http://json-schema.org/draft-07/schema'}}}], 'required': ['type', 'thumb_style', 'track_active_style', 'track_inactive_style'], '$schema': 'http://json-schema.org/draft-07/schema'}, rule='required')
 return data

def validate_div_slider_json__definitions_range(data, custom_formats={}, name_prefix=None):
 if not isinstance(data, (dict)):
  if not (isinstance(data, str) and '@' in data):
   raise JsonSchemaValueException("" + (name_prefix or "data") + " must be object", value=data, name="" + (name_prefix or "data") + "", definition={'type': 'object', 'properties': {'start': {'type': 'integer', '$description': 'translations.json#/div_slider_range_start'}, 'end': {'type': 'integer', '$description': 'translations.json#/div_slider_range_end'}, 'track_active_style': {'anyOf': [{'$ref': 'div-shape-drawable.json', '$description': 'translations.json#/div_shape_drawable'}], '$schema': 'http://json-schema.org/draft-07/schema'}, 'track_inactive_style': {'anyOf': [{'$ref': 'div-shape-drawable.json', '$description': 'translations.json#/div_shape_drawable'}], '$schema': 'http://json-schema.org/draft-07/schema'}, 'margins': {'type': 'object', '$description': 'translations.json#/div_edge_insets', 'properties': {'left': {'$ref': 'common.json#/non_negative_integer', 'default_value': '0', '$description': 'translations.json#/div_edge_insets_left'}, 'right': {'$ref': 'common.json#/non_negative_integer', 'default_value': '0', '$description': 'translations.json#/div_edge_insets_right'}, 'top': {'$ref': 'common.json#/non_negative_integer', 'default_value': '0', '$description': 'translations.json#/div_edge_insets_top'}, 'bottom': {'$ref': 'common.json#/non_negative_integer', 'default_value': '0', '$description': 'translations.json#/div_edge_insets_bottom'}, 'start': {'$ref': 'common.json#/non_negative_integer', '$description': 'translations.json#/div_edge_insets_start', 'platforms': []}, 'end': {'$ref': 'common.json#/non_negative_integer', '$description': 'translations.json#/div_edge_insets_end', 'platforms': []}, 'unit': {'$ref': 'div-size-unit.json', 'default_value': 'dp'}}, '$schema': 'http://json-schema.org/draft-07/schema'}}}, rule='type')
 data_is_dict = isinstance(data, dict)
 if data_is_dict:
  data_keys = set(data.keys())
  if "start" in data_keys:
   data_keys.remove("start")
   data__start = data["start"]
   if not isinstance(data__start, (int)) and not (isinstance(data__start, float) and data__start.is_integer()) or isinstance(data__start, bool):
    if not (isinstance(data__start, str) and '@' in data__start):
     raise JsonSchemaValueException("" + (name_prefix or "data") + ".start must be integer", value=data__start, name="" + (name_prefix or "data") + ".start", definition={'type': 'integer', '$description': 'translations.json#/div_slider_range_start'}, rule='type')
  if "end" in data_keys:
   data_keys.remove("end")
   data__end = data["end"]
   if not isinstance(data__end, (int)) and not (isinstance(data__end, float) and data__end.is_integer()) or isinstance(data__end, bool):
    if not (isinstance(data__end, str) and '@' in data__end):
     raise JsonSchemaValueException("" + (name_prefix or "data") + ".end must be integer", value=data__end, name="" + (name_prefix or "data") + ".end", definition={'type': 'integer', '$description': 'translations.json#/div_slider_range_end'}, rule='type')
  if "track_active_style" in data_keys:
   data_keys.remove("track_active_style")
   data__trackactivestyle = data["track_active_style"]
   validate_div_drawable_json(data__trackactivestyle, custom_formats, (name_prefix or "data") + ".track_active_style")
  if "track_inactive_style" in data_keys:
   data_keys.remove("track_inactive_style")
   data__trackinactivestyle = data["track_inactive_style"]
   validate_div_drawable_json(data__trackinactivestyle, custom_formats, (name_prefix or "data") + ".track_inactive_style")
  if "margins" in data_keys:
   data_keys.remove("margins")
   data__margins = data["margins"]
   validate_div_edge_insets_json(data__margins, custom_formats, (name_prefix or "data") + ".margins")
 return data

def validate_div_slider_json__definitions_text_style(data, custom_formats={}, name_prefix=None):
 if not isinstance(data, (dict)):
  if not (isinstance(data, str) and '@' in data):
   raise JsonSchemaValueException("" + (name_prefix or "data") + " must be object", value=data, name="" + (name_prefix or "data") + "", definition={'type': 'object', 'properties': {'font_size': {'type': 'integer', 'constraint': 'number >= 0'}, 'font_size_unit': {'type': 'string', 'enum': ['dp', 'sp', 'px'], '$description': 'translations.json#/div_size_unit', 'platforms': ['android', 'ios'], '$schema': 'http://json-schema.org/draft-07/schema'}, 'font_weight': {'type': 'string', 'enum': ['light', 'medium', 'regular', 'bold'], '$schema': 'http://json-schema.org/draft-07/schema'}, 'text_color': {'type': 'string', 'format': 'color'}, 'offset': {'type': 'object', '$description': 'translations.json#/div_point', 'properties': {'x': {'$ref': 'div-dimension.json', '$description': 'translations.json#/div_point_x'}, 'y': {'$ref': 'div-dimension.json', '$description': 'translations.json#/div_point_y'}}, 'required': ['x', 'y'], '$schema': 'http://json-schema.org/draft-07/schema'}}, 'required': ['font_size']}, rule='type')
 data_is_dict = isinstance(data, dict)
 if data_is_dict:
  data__missing_keys = set(['font_size']) - data.keys()
  if data__missing_keys:
   if not (isinstance(data, str) and '@' in data):
    raise JsonSchemaValueException("" + (name_prefix or "data") + " must contain " + (str(sorted(data__missing_keys)) + " properties"), value=data, name="" + (name_prefix or "data") + "", definition={'type': 'object', 'properties': {'font_size': {'type': 'integer', 'constraint': 'number >= 0'}, 'font_size_unit': {'type': 'string', 'enum': ['dp', 'sp', 'px'], '$description': 'translations.json#/div_size_unit', 'platforms': ['android', 'ios'], '$schema': 'http://json-schema.org/draft-07/schema'}, 'font_weight': {'type': 'string', 'enum': ['light', 'medium', 'regular', 'bold'], '$schema': 'http://json-schema.org/draft-07/schema'}, 'text_color': {'type': 'string', 'format': 'color'}, 'offset': {'type': 'object', '$description': 'translations.json#/div_point', 'properties': {'x': {'$ref': 'div-dimension.json', '$description': 'translations.json#/div_point_x'}, 'y': {'$ref': 'div-dimension.json', '$description': 'translations.json#/div_point_y'}}, 'required': ['x', 'y'], '$schema': 'http://json-schema.org/draft-07/schema'}}, 'required': ['font_size']}, rule='required')
  data_keys = set(data.keys())
  if "font_size" in data_keys:
   data_keys.remove("font_size")
   data__fontsize = data["font_size"]
   validate_common_json__non_negative_integer(data__fontsize, custom_formats, (name_prefix or "data") + ".font_size")
  if "font_size_unit" in data_keys:
   data_keys.remove("font_size_unit")
   data__fontsizeunit = data["font_size_unit"]
   validate_div_size_unit_json(data__fontsizeunit, custom_formats, (name_prefix or "data") + ".font_size_unit")
  if "font_weight" in data_keys:
   data_keys.remove("font_weight")
   data__fontweight = data["font_weight"]
   validate_div_font_weight_json(data__fontweight, custom_formats, (name_prefix or "data") + ".font_weight")
  if "text_color" in data_keys:
   data_keys.remove("text_color")
   data__textcolor = data["text_color"]
   validate_common_json__color(data__textcolor, custom_formats, (name_prefix or "data") + ".text_color")
  if "offset" in data_keys:
   data_keys.remove("offset")
   data__offset = data["offset"]
   validate_div_point_json(data__offset, custom_formats, (name_prefix or "data") + ".offset")
 return data

def validate_div_drawable_json(data, custom_formats={}, name_prefix=None):
 data_any_of_count17 = 0
 if not data_any_of_count17:
  try:
   validate_div_shape_drawable_json(data, custom_formats, (name_prefix or "data") + "")
   data_any_of_count17 += 1
  except JsonSchemaValueException: pass
 if not data_any_of_count17:
  if not (isinstance(data, str) and '@' in data):
   raise JsonSchemaValueException("" + (name_prefix or "data") + " cannot be validated by any definition", value=data, name="" + (name_prefix or "data") + "", definition={'anyOf': [{'type': 'object', '$description': 'translations.json#/div_shape_drawable', 'properties': {'shape': {'$ref': 'div-shape.json', '$description': 'translations.json#/div_shape_drawable_shape'}, 'color': {'$ref': 'common.json#/color', '$description': 'translations.json#/div_shape_drawable_color', 'deprecated': True}, 'stroke': {'$ref': 'div-stroke.json', '$description': 'translations.json#/div_shape_drawable_stroke', 'deprecated': True}, 'type': {'type': 'string', 'enum': ['shape_drawable']}}, 'required': ['type', 'shape', 'color'], '$schema': 'http://json-schema.org/draft-07/schema'}], '$schema': 'http://json-schema.org/draft-07/schema'}, rule='anyOf')
 return data

def validate_div_shape_drawable_json(data, custom_formats={}, name_prefix=None):
 if not isinstance(data, (dict)):
  if not (isinstance(data, str) and '@' in data):
   raise JsonSchemaValueException("" + (name_prefix or "data") + " must be object", value=data, name="" + (name_prefix or "data") + "", definition={'type': 'object', '$description': 'translations.json#/div_shape_drawable', 'properties': {'shape': {'anyOf': [{'$ref': 'div-rounded-rectangle-shape.json', '$description': 'translations.json#/div_rounded_rectangle_shape'}, {'$ref': 'div-circle-shape.json', '$description': 'translations.json#/div_circle_shape', 'platforms': ['android', 'web']}], '$schema': 'http://json-schema.org/draft-07/schema'}, 'color': {'type': 'string', 'format': 'color'}, 'stroke': {'type': 'object', '$description': 'translations.json#/div_stroke', 'properties': {'width': {'$ref': 'common.json#/non_negative_integer', 'default_value': '1', '$description': 'translations.json#/div_stroke_width'}, 'color': {'$ref': 'common.json#/color', '$description': 'translations.json#/div_stroke_color'}, 'unit': {'$ref': 'div-size-unit.json', 'default_value': 'dp'}}, 'required': ['color'], '$schema': 'http://json-schema.org/draft-07/schema'}, 'type': {'type': 'string', 'enum': ['shape_drawable']}}, 'required': ['type', 'shape', 'color'], '$schema': 'http://json-schema.org/draft-07/schema'}, rule='type')
 data_is_dict = isinstance(data, dict)
 if data_is_dict:
  data__missing_keys = set(['type', 'shape', 'color']) - data.keys()
  if data__missing_keys:
   if not (isinstance(data, str) and '@' in data):
    raise JsonSchemaValueException("" + (name_prefix or "data") + " must contain " + (str(sorted(data__missing_keys)) + " properties"), value=data, name="" + (name_prefix or "data") + "", definition={'type': 'object', '$description': 'translations.json#/div_shape_drawable', 'properties': {'shape': {'anyOf': [{'$ref': 'div-rounded-rectangle-shape.json', '$description': 'translations.json#/div_rounded_rectangle_shape'}, {'$ref': 'div-circle-shape.json', '$description': 'translations.json#/div_circle_shape', 'platforms': ['android', 'web']}], '$schema': 'http://json-schema.org/draft-07/schema'}, 'color': {'type': 'string', 'format': 'color'}, 'stroke': {'type': 'object', '$description': 'translations.json#/div_stroke', 'properties': {'width': {'$ref': 'common.json#/non_negative_integer', 'default_value': '1', '$description': 'translations.json#/div_stroke_width'}, 'color': {'$ref': 'common.json#/color', '$description': 'translations.json#/div_stroke_color'}, 'unit': {'$ref': 'div-size-unit.json', 'default_value': 'dp'}}, 'required': ['color'], '$schema': 'http://json-schema.org/draft-07/schema'}, 'type': {'type': 'string', 'enum': ['shape_drawable']}}, 'required': ['type', 'shape', 'color'], '$schema': 'http://json-schema.org/draft-07/schema'}, rule='required')
  data_keys = set(data.keys())
  if "shape" in data_keys:
   data_keys.remove("shape")
   data__shape = data["shape"]
   validate_div_shape_json(data__shape, custom_formats, (name_prefix or "data") + ".shape")
  if "color" in data_keys:
   data_keys.remove("color")
   data__color = data["color"]
   validate_common_json__color(data__color, custom_formats, (name_prefix or "data") + ".color")
  if "stroke" in data_keys:
   data_keys.remove("stroke")
   data__stroke = data["stroke"]
   validate_div_stroke_json(data__stroke, custom_formats, (name_prefix or "data") + ".stroke")
  if "type" in data_keys:
   data_keys.remove("type")
   data__type = data["type"]
   if not isinstance(data__type, (str)):
    if not (isinstance(data__type, str) and '@' in data__type):
     raise JsonSchemaValueException("" + (name_prefix or "data") + ".type must be string", value=data__type, name="" + (name_prefix or "data") + ".type", definition={'type': 'string', 'enum': ['shape_drawable']}, rule='type')
   if data__type not in ['shape_drawable']:
    if not (isinstance(data__type, str) and '@' in data__type):
     raise JsonSchemaValueException("" + (name_prefix or "data") + ".type must be one of ['shape_drawable']", value=data__type, name="" + (name_prefix or "data") + ".type", definition={'type': 'string', 'enum': ['shape_drawable']}, rule='enum')
 return data

def validate_div_shape_json(data, custom_formats={}, name_prefix=None):
 data_any_of_count18 = 0
 if not data_any_of_count18:
  try:
   validate_div_rounded_rectangle_shape_json(data, custom_formats, (name_prefix or "data") + "")
   data_any_of_count18 += 1
  except JsonSchemaValueException: pass
 if not data_any_of_count18:
  try:
   validate_div_circle_shape_json(data, custom_formats, (name_prefix or "data") + "")
   data_any_of_count18 += 1
  except JsonSchemaValueException: pass
 if not data_any_of_count18:
  if not (isinstance(data, str) and '@' in data):
   raise JsonSchemaValueException("" + (name_prefix or "data") + " cannot be validated by any definition", value=data, name="" + (name_prefix or "data") + "", definition={'anyOf': [{'$description': 'translations.json#/div_rounded_rectangle_shape', 'allOf': [{'$ref': 'div-shape-base.json'}, {'type': 'object', 'properties': {'item_width': {'$ref': 'div-fixed-size.json', 'default_value': '{"type":"fixed","value":10}', '$description': 'translations.json#/div_rounded_rectangle_shape_item_width'}, 'item_height': {'$ref': 'div-fixed-size.json', 'default_value': '{"type":"fixed","value":10}', '$description': 'translations.json#/div_rounded_rectangle_shape_item_height'}, 'corner_radius': {'$ref': 'div-fixed-size.json', 'default_value': '{"type":"fixed","value":5}', '$description': 'translations.json#/div_rounded_rectangle_shape_corner_radius'}, 'type': {'type': 'string', 'enum': ['rounded_rectangle']}}}], 'required': ['type'], '$schema': 'http://json-schema.org/draft-07/schema'}, {'$description': 'translations.json#/div_circle_shape', 'allOf': [{'$ref': 'div-shape-base.json'}, {'type': 'object', 'properties': {'radius': {'$ref': 'div-fixed-size.json', 'default_value': '{"type":"fixed","value":10}', '$description': 'translations.json#/div_circle_shape_radius'}, 'type': {'type': 'string', 'enum': ['circle']}}}], 'required': ['type'], 'platforms': ['android', 'web'], '$schema': 'http://json-schema.org/draft-07/schema'}], '$schema': 'http://json-schema.org/draft-07/schema'}, rule='anyOf')
 return data

def validate_div_circle_shape_json(data, custom_formats={}, name_prefix=None):
 validate_div_shape_base_json(data, custom_formats, (name_prefix or "data") + "")
 if not isinstance(data, (dict)):
  if not (isinstance(data, str) and '@' in data):
   raise JsonSchemaValueException("" + (name_prefix or "data") + " must be object", value=data, name="" + (name_prefix or "data") + "", definition={'type': 'object', 'properties': {'radius': {'type': 'object', '$description': 'translations.json#/div_fixed_size', 'codegen': {'divan': {'forced_properties_order': ['value']}}, 'properties': {'value': {'$ref': 'common.json#/non_negative_integer', '$description': 'translations.json#/div_fixed_size_value'}, 'unit': {'$ref': 'div-size-unit.json', '$description': 'translations.json#/div_fixed_size_unit', 'default_value': 'dp'}, 'type': {'type': 'string', 'enum': ['fixed']}}, 'required': ['value', 'type'], '$schema': 'http://json-schema.org/draft-07/schema'}, 'type': {'type': 'string', 'enum': ['circle']}}}, rule='type')
 data_is_dict = isinstance(data, dict)
 if data_is_dict:
  data_keys = set(data.keys())
  if "radius" in data_keys:
   data_keys.remove("radius")
   data__radius = data["radius"]
   validate_div_fixed_size_json(data__radius, custom_formats, (name_prefix or "data") + ".radius")
  if "type" in data_keys:
   data_keys.remove("type")
   data__type = data["type"]
   if not isinstance(data__type, (str)):
    if not (isinstance(data__type, str) and '@' in data__type):
     raise JsonSchemaValueException("" + (name_prefix or "data") + ".type must be string", value=data__type, name="" + (name_prefix or "data") + ".type", definition={'type': 'string', 'enum': ['circle']}, rule='type')
   if data__type not in ['circle']:
    if not (isinstance(data__type, str) and '@' in data__type):
     raise JsonSchemaValueException("" + (name_prefix or "data") + ".type must be one of ['circle']", value=data__type, name="" + (name_prefix or "data") + ".type", definition={'type': 'string', 'enum': ['circle']}, rule='enum')
 data_is_dict = isinstance(data, dict)
 if data_is_dict:
  data__missing_keys = set(['type']) - data.keys()
  if data__missing_keys:
   if not (isinstance(data, str) and '@' in data):
    raise JsonSchemaValueException("" + (name_prefix or "data") + " must contain " + (str(sorted(data__missing_keys)) + " properties"), value=data, name="" + (name_prefix or "data") + "", definition={'$description': 'translations.json#/div_circle_shape', 'allOf': [{'properties': {'background_color': {'$ref': 'common.json#/color', '$description': 'translations.json#/div_shape_base_background_color'}, 'stroke': {'$ref': 'div-stroke.json', '$description': 'translations.json#/div_shape_base_stroke'}}, '$schema': 'http://json-schema.org/draft-07/schema'}, {'type': 'object', 'properties': {'radius': {'type': 'object', '$description': 'translations.json#/div_fixed_size', 'codegen': {'divan': {'forced_properties_order': ['value']}}, 'properties': {'value': {'$ref': 'common.json#/non_negative_integer', '$description': 'translations.json#/div_fixed_size_value'}, 'unit': {'$ref': 'div-size-unit.json', '$description': 'translations.json#/div_fixed_size_unit', 'default_value': 'dp'}, 'type': {'type': 'string', 'enum': ['fixed']}}, 'required': ['value', 'type'], '$schema': 'http://json-schema.org/draft-07/schema'}, 'type': {'type': 'string', 'enum': ['circle']}}}], 'required': ['type'], 'platforms': ['android', 'web'], '$schema': 'http://json-schema.org/draft-07/schema'}, rule='required')
 return data

def validate_div_shape_base_json(data, custom_formats={}, name_prefix=None):
 data_is_dict = isinstance(data, dict)
 if data_is_dict:
  data_keys = set(data.keys())
  if "background_color" in data_keys:
   data_keys.remove("background_color")
   data__backgroundcolor = data["background_color"]
   validate_common_json__color(data__backgroundcolor, custom_formats, (name_prefix or "data") + ".background_color")
  if "stroke" in data_keys:
   data_keys.remove("stroke")
   data__stroke = data["stroke"]
   validate_div_stroke_json(data__stroke, custom_formats, (name_prefix or "data") + ".stroke")
 return data

def validate_div_rounded_rectangle_shape_json(data, custom_formats={}, name_prefix=None):
 validate_div_shape_base_json(data, custom_formats, (name_prefix or "data") + "")
 if not isinstance(data, (dict)):
  if not (isinstance(data, str) and '@' in data):
   raise JsonSchemaValueException("" + (name_prefix or "data") + " must be object", value=data, name="" + (name_prefix or "data") + "", definition={'type': 'object', 'properties': {'item_width': {'type': 'object', '$description': 'translations.json#/div_fixed_size', 'codegen': {'divan': {'forced_properties_order': ['value']}}, 'properties': {'value': {'$ref': 'common.json#/non_negative_integer', '$description': 'translations.json#/div_fixed_size_value'}, 'unit': {'$ref': 'div-size-unit.json', '$description': 'translations.json#/div_fixed_size_unit', 'default_value': 'dp'}, 'type': {'type': 'string', 'enum': ['fixed']}}, 'required': ['value', 'type'], '$schema': 'http://json-schema.org/draft-07/schema'}, 'item_height': {'type': 'object', '$description': 'translations.json#/div_fixed_size', 'codegen': {'divan': {'forced_properties_order': ['value']}}, 'properties': {'value': {'$ref': 'common.json#/non_negative_integer', '$description': 'translations.json#/div_fixed_size_value'}, 'unit': {'$ref': 'div-size-unit.json', '$description': 'translations.json#/div_fixed_size_unit', 'default_value': 'dp'}, 'type': {'type': 'string', 'enum': ['fixed']}}, 'required': ['value', 'type'], '$schema': 'http://json-schema.org/draft-07/schema'}, 'corner_radius': {'type': 'object', '$description': 'translations.json#/div_fixed_size', 'codegen': {'divan': {'forced_properties_order': ['value']}}, 'properties': {'value': {'$ref': 'common.json#/non_negative_integer', '$description': 'translations.json#/div_fixed_size_value'}, 'unit': {'$ref': 'div-size-unit.json', '$description': 'translations.json#/div_fixed_size_unit', 'default_value': 'dp'}, 'type': {'type': 'string', 'enum': ['fixed']}}, 'required': ['value', 'type'], '$schema': 'http://json-schema.org/draft-07/schema'}, 'type': {'type': 'string', 'enum': ['rounded_rectangle']}}}, rule='type')
 data_is_dict = isinstance(data, dict)
 if data_is_dict:
  data_keys = set(data.keys())
  if "item_width" in data_keys:
   data_keys.remove("item_width")
   data__itemwidth = data["item_width"]
   validate_div_fixed_size_json(data__itemwidth, custom_formats, (name_prefix or "data") + ".item_width")
  if "item_height" in data_keys:
   data_keys.remove("item_height")
   data__itemheight = data["item_height"]
   validate_div_fixed_size_json(data__itemheight, custom_formats, (name_prefix or "data") + ".item_height")
  if "corner_radius" in data_keys:
   data_keys.remove("corner_radius")
   data__cornerradius = data["corner_radius"]
   validate_div_fixed_size_json(data__cornerradius, custom_formats, (name_prefix or "data") + ".corner_radius")
  if "type" in data_keys:
   data_keys.remove("type")
   data__type = data["type"]
   if not isinstance(data__type, (str)):
    if not (isinstance(data__type, str) and '@' in data__type):
     raise JsonSchemaValueException("" + (name_prefix or "data") + ".type must be string", value=data__type, name="" + (name_prefix or "data") + ".type", definition={'type': 'string', 'enum': ['rounded_rectangle']}, rule='type')
   if data__type not in ['rounded_rectangle']:
    if not (isinstance(data__type, str) and '@' in data__type):
     raise JsonSchemaValueException("" + (name_prefix or "data") + ".type must be one of ['rounded_rectangle']", value=data__type, name="" + (name_prefix or "data") + ".type", definition={'type': 'string', 'enum': ['rounded_rectangle']}, rule='enum')
 data_is_dict = isinstance(data, dict)
 if data_is_dict:
  data__missing_keys = set(['type']) - data.keys()
  if data__missing_keys:
   if not (isinstance(data, str) and '@' in data):
    raise JsonSchemaValueException("" + (name_prefix or "data") + " must contain " + (str(sorted(data__missing_keys)) + " properties"), value=data, name="" + (name_prefix or "data") + "", definition={'$description': 'translations.json#/div_rounded_rectangle_shape', 'allOf': [{'properties': {'background_color': {'$ref': 'common.json#/color', '$description': 'translations.json#/div_shape_base_background_color'}, 'stroke': {'$ref': 'div-stroke.json', '$description': 'translations.json#/div_shape_base_stroke'}}, '$schema': 'http://json-schema.org/draft-07/schema'}, {'type': 'object', 'properties': {'item_width': {'type': 'object', '$description': 'translations.json#/div_fixed_size', 'codegen': {'divan': {'forced_properties_order': ['value']}}, 'properties': {'value': {'$ref': 'common.json#/non_negative_integer', '$description': 'translations.json#/div_fixed_size_value'}, 'unit': {'$ref': 'div-size-unit.json', '$description': 'translations.json#/div_fixed_size_unit', 'default_value': 'dp'}, 'type': {'type': 'string', 'enum': ['fixed']}}, 'required': ['value', 'type'], '$schema': 'http://json-schema.org/draft-07/schema'}, 'item_height': {'type': 'object', '$description': 'translations.json#/div_fixed_size', 'codegen': {'divan': {'forced_properties_order': ['value']}}, 'properties': {'value': {'$ref': 'common.json#/non_negative_integer', '$description': 'translations.json#/div_fixed_size_value'}, 'unit': {'$ref': 'div-size-unit.json', '$description': 'translations.json#/div_fixed_size_unit', 'default_value': 'dp'}, 'type': {'type': 'string', 'enum': ['fixed']}}, 'required': ['value', 'type'], '$schema': 'http://json-schema.org/draft-07/schema'}, 'corner_radius': {'type': 'object', '$description': 'translations.json#/div_fixed_size', 'codegen': {'divan': {'forced_properties_order': ['value']}}, 'properties': {'value': {'$ref': 'common.json#/non_negative_integer', '$description': 'translations.json#/div_fixed_size_value'}, 'unit': {'$ref': 'div-size-unit.json', '$description': 'translations.json#/div_fixed_size_unit', 'default_value': 'dp'}, 'type': {'type': 'string', 'enum': ['fixed']}}, 'required': ['value', 'type'], '$schema': 'http://json-schema.org/draft-07/schema'}, 'type': {'type': 'string', 'enum': ['rounded_rectangle']}}}], 'required': ['type'], '$schema': 'http://json-schema.org/draft-07/schema'}, rule='required')
 return data

def validate_div_indicator_json(data, custom_formats={}, name_prefix=None):
 validate_div_base_json(data, custom_formats, (name_prefix or "data") + "")
 data_is_dict = isinstance(data, dict)
 if data_is_dict:
  data_keys = set(data.keys())
  if "type" in data_keys:
   data_keys.remove("type")
   data__type = data["type"]
   if not isinstance(data__type, (str)):
    if not (isinstance(data__type, str) and '@' in data__type):
     raise JsonSchemaValueException("" + (name_prefix or "data") + ".type must be string", value=data__type, name="" + (name_prefix or "data") + ".type", definition={'type': 'string', 'enum': ['indicator']}, rule='type')
   if data__type not in ['indicator']:
    if not (isinstance(data__type, str) and '@' in data__type):
     raise JsonSchemaValueException("" + (name_prefix or "data") + ".type must be one of ['indicator']", value=data__type, name="" + (name_prefix or "data") + ".type", definition={'type': 'string', 'enum': ['indicator']}, rule='enum')
  if "pager_id" in data_keys:
   data_keys.remove("pager_id")
   data__pagerid = data["pager_id"]
   if not isinstance(data__pagerid, (str)):
    if not (isinstance(data__pagerid, str) and '@' in data__pagerid):
     raise JsonSchemaValueException("" + (name_prefix or "data") + ".pager_id must be string", value=data__pagerid, name="" + (name_prefix or "data") + ".pager_id", definition={'type': 'string', 'supports_expressions': False, '$description': 'translations.json#/div_indicator_pager_id'}, rule='type')
  if "items_placement" in data_keys:
   data_keys.remove("items_placement")
   data__itemsplacement = data["items_placement"]
   validate_div_indicator_item_placement_json(data__itemsplacement, custom_formats, (name_prefix or "data") + ".items_placement")
  if "space_between_centers" in data_keys:
   data_keys.remove("space_between_centers")
   data__spacebetweencenters = data["space_between_centers"]
   validate_div_fixed_size_json(data__spacebetweencenters, custom_formats, (name_prefix or "data") + ".space_between_centers")
  if "inactive_item_color" in data_keys:
   data_keys.remove("inactive_item_color")
   data__inactiveitemcolor = data["inactive_item_color"]
   validate_common_json__color(data__inactiveitemcolor, custom_formats, (name_prefix or "data") + ".inactive_item_color")
  if "active_item_color" in data_keys:
   data_keys.remove("active_item_color")
   data__activeitemcolor = data["active_item_color"]
   validate_common_json__color(data__activeitemcolor, custom_formats, (name_prefix or "data") + ".active_item_color")
  if "shape" in data_keys:
   data_keys.remove("shape")
   data__shape = data["shape"]
   validate_div_shape_json(data__shape, custom_formats, (name_prefix or "data") + ".shape")
  if "active_item_size" in data_keys:
   data_keys.remove("active_item_size")
   data__activeitemsize = data["active_item_size"]
   validate_common_json__positive_number(data__activeitemsize, custom_formats, (name_prefix or "data") + ".active_item_size")
  if "minimum_item_size" in data_keys:
   data_keys.remove("minimum_item_size")
   data__minimumitemsize = data["minimum_item_size"]
   validate_common_json__positive_number(data__minimumitemsize, custom_formats, (name_prefix or "data") + ".minimum_item_size")
  if "active_shape" in data_keys:
   data_keys.remove("active_shape")
   data__activeshape = data["active_shape"]
   validate_div_rounded_rectangle_shape_json(data__activeshape, custom_formats, (name_prefix or "data") + ".active_shape")
  if "inactive_shape" in data_keys:
   data_keys.remove("inactive_shape")
   data__inactiveshape = data["inactive_shape"]
   validate_div_rounded_rectangle_shape_json(data__inactiveshape, custom_formats, (name_prefix or "data") + ".inactive_shape")
  if "inactive_minimum_shape" in data_keys:
   data_keys.remove("inactive_minimum_shape")
   data__inactiveminimumshape = data["inactive_minimum_shape"]
   validate_div_rounded_rectangle_shape_json(data__inactiveminimumshape, custom_formats, (name_prefix or "data") + ".inactive_minimum_shape")
  if "animation" in data_keys:
   data_keys.remove("animation")
   data__animation = data["animation"]
   if not isinstance(data__animation, (str)):
    if not (isinstance(data__animation, str) and '@' in data__animation):
     raise JsonSchemaValueException("" + (name_prefix or "data") + ".animation must be string", value=data__animation, name="" + (name_prefix or "data") + ".animation", definition={'type': 'string', 'enum': ['scale', 'worm', 'slider'], 'default_value': 'scale', '$description': 'translations.json#/div_indicator_animation', 'platforms': ['android', 'ios']}, rule='type')
   if data__animation not in ['scale', 'worm', 'slider']:
    if not (isinstance(data__animation, str) and '@' in data__animation):
     raise JsonSchemaValueException("" + (name_prefix or "data") + ".animation must be one of ['scale', 'worm', 'slider']", value=data__animation, name="" + (name_prefix or "data") + ".animation", definition={'type': 'string', 'enum': ['scale', 'worm', 'slider'], 'default_value': 'scale', '$description': 'translations.json#/div_indicator_animation', 'platforms': ['android', 'ios']}, rule='enum')
 data_is_dict = isinstance(data, dict)
 if data_is_dict:
  data__missing_keys = set(['type']) - data.keys()
  if data__missing_keys:
   if not (isinstance(data, str) and '@' in data):
    raise JsonSchemaValueException("" + (name_prefix or "data") + " must contain " + (str(sorted(data__missing_keys)) + " properties"), value=data, name="" + (name_prefix or "data") + "", definition={'java_extends': 'DivBlockWithId', '$description': 'translations.json#/div_indicator', 'allOf': [{'protocol_name': 'div-base', 'codegen': {'swift': {'super_protocol': 'DivBlockModeling'}, 'documentation': {'include_in_toc': True}}, 'type': 'object', 'properties': {'id': {'$ref': 'common.json#/non_empty_string', 'supports_expressions': False, '$description': 'translations.json#/div_base_id'}, 'border': {'$ref': 'div-border.json', '$description': 'translations.json#/div_base_border'}, 'width': {'$ref': 'div-size.json', 'default_value': '{"type": "match_parent"}', '$description': 'translations.json#/div_base_width'}, 'height': {'$ref': 'div-size.json', 'default_value': '{"type": "wrap_content"}', '$description': 'translations.json#/div_base_height'}, 'background': {'type': 'array', 'items': {'$ref': 'div-background.json'}, 'minItems': 1, '$description': 'translations.json#/div_base_background'}, 'paddings': {'$ref': 'div-edge-insets.json', '$description': 'translations.json#/div_base_paddings'}, 'margins': {'$ref': 'div-edge-insets.json', '$description': 'translations.json#/div_base_margins'}, 'alpha': {'type': 'number', 'default_value': '1.0', 'constraint': 'number >= 0.0 && number <= 1.0', '$description': 'translations.json#/div_base_alpha'}, 'alignment_vertical': {'$ref': 'div-alignment-vertical.json', '$description': 'translations.json#/div_base_alignment_vertical'}, 'alignment_horizontal': {'$ref': 'div-alignment-horizontal.json', '$description': 'translations.json#/div_base_alignment_horizontal'}, 'row_span': {'$ref': 'common.json#/non_negative_integer', '$description': 'translations.json#/div_base_row_span'}, 'column_span': {'$ref': 'common.json#/non_negative_integer', '$description': 'translations.json#/div_base_column_span'}, 'visibility_action': {'$ref': 'div-visibility-action.json', '$description': 'translations.json#/div_base_visibility_action'}, 'visibility_actions': {'type': 'array', 'items': {'$ref': 'div-visibility-action.json'}, 'minItems': 1, '$description': 'translations.json#/div_base_visibility_actions'}, 'disappear_actions': {'type': 'array', 'items': {'$ref': 'div-disappear-action.json'}, 'minItems': 1, '$description': 'translations.json#/div_base_disappear_actions'}, 'tooltips': {'type': 'array', 'items': {'$ref': 'div-tooltip.json'}, 'minItems': 1, '$description': 'translations.json#/div_base_tooltips'}, 'accessibility': {'$ref': 'div-accessibility.json', '$description': 'translations.json#/div_base_accessibility'}, 'extensions': {'type': 'array', 'items': {'$ref': 'div-extension.json'}, 'minItems': 1, '$description': 'translations.json#/div_base_extensions'}, 'transition_triggers': {'type': 'array', 'items': {'$ref': 'div-transition-trigger.json'}, 'minItems': 1, 'supports_expressions': False, '$description': 'translations.json#/div_base_transition_triggers'}, 'transition_in': {'$ref': 'div-appearance-transition.json', '$description': 'translations.json#/div_base_transition_in'}, 'transition_change': {'$ref': 'div-change-transition.json', '$description': 'translations.json#/div_base_transition_change'}, 'transition_out': {'$ref': 'div-appearance-transition.json', '$description': 'translations.json#/div_base_transition_out'}, 'selected_actions': {'type': 'array', 'items': {'$ref': 'div-action.json'}, 'minItems': 1, '$description': 'translations.json#/div_base_selected_actions'}, 'focus': {'$ref': 'div-focus.json', '$description': 'translations.json#/div_base_focus', 'platforms': ['android', 'ios']}, 'visibility': {'$ref': 'div-visibility.json', '$description': 'translations.json#/div_base_visibility', 'default_value': 'visible'}, 'transform': {'$ref': 'div-transform.json', '$description': 'translations.json#/div_base_transform'}}, '$schema': 'http://json-schema.org/draft-07/schema'}, {'properties': {'type': {'type': 'string', 'enum': ['indicator']}, 'pager_id': {'type': 'string', 'supports_expressions': False, '$description': 'translations.json#/div_indicator_pager_id'}, 'items_placement': {'anyOf': [{'$ref': 'div-default-indicator-item-placement.json', '$description': 'translations.json#/div_indicator_item_placement_default'}, {'$ref': 'div-stretch-indicator-item-placement.json', '$description': 'translations.json#/div_indicator_item_placement_stretch'}], '$schema': 'http://json-schema.org/draft-07/schema'}, 'space_between_centers': {'type': 'object', '$description': 'translations.json#/div_fixed_size', 'codegen': {'divan': {'forced_properties_order': ['value']}}, 'properties': {'value': {'$ref': 'common.json#/non_negative_integer', '$description': 'translations.json#/div_fixed_size_value'}, 'unit': {'$ref': 'div-size-unit.json', '$description': 'translations.json#/div_fixed_size_unit', 'default_value': 'dp'}, 'type': {'type': 'string', 'enum': ['fixed']}}, 'required': ['value', 'type'], '$schema': 'http://json-schema.org/draft-07/schema'}, 'inactive_item_color': {'type': 'string', 'format': 'color'}, 'active_item_color': {'type': 'string', 'format': 'color'}, 'shape': {'anyOf': [{'$ref': 'div-rounded-rectangle-shape.json', '$description': 'translations.json#/div_rounded_rectangle_shape'}, {'$ref': 'div-circle-shape.json', '$description': 'translations.json#/div_circle_shape', 'platforms': ['android', 'web']}], '$schema': 'http://json-schema.org/draft-07/schema'}, 'active_item_size': {'type': 'number', 'constraint': 'number > 0'}, 'minimum_item_size': {'type': 'number', 'constraint': 'number > 0'}, 'active_shape': {'$description': 'translations.json#/div_rounded_rectangle_shape', 'allOf': [{'$ref': 'div-shape-base.json'}, {'type': 'object', 'properties': {'item_width': {'$ref': 'div-fixed-size.json', 'default_value': '{"type":"fixed","value":10}', '$description': 'translations.json#/div_rounded_rectangle_shape_item_width'}, 'item_height': {'$ref': 'div-fixed-size.json', 'default_value': '{"type":"fixed","value":10}', '$description': 'translations.json#/div_rounded_rectangle_shape_item_height'}, 'corner_radius': {'$ref': 'div-fixed-size.json', 'default_value': '{"type":"fixed","value":5}', '$description': 'translations.json#/div_rounded_rectangle_shape_corner_radius'}, 'type': {'type': 'string', 'enum': ['rounded_rectangle']}}}], 'required': ['type'], '$schema': 'http://json-schema.org/draft-07/schema'}, 'inactive_shape': {'$description': 'translations.json#/div_rounded_rectangle_shape', 'allOf': [{'$ref': 'div-shape-base.json'}, {'type': 'object', 'properties': {'item_width': {'$ref': 'div-fixed-size.json', 'default_value': '{"type":"fixed","value":10}', '$description': 'translations.json#/div_rounded_rectangle_shape_item_width'}, 'item_height': {'$ref': 'div-fixed-size.json', 'default_value': '{"type":"fixed","value":10}', '$description': 'translations.json#/div_rounded_rectangle_shape_item_height'}, 'corner_radius': {'$ref': 'div-fixed-size.json', 'default_value': '{"type":"fixed","value":5}', '$description': 'translations.json#/div_rounded_rectangle_shape_corner_radius'}, 'type': {'type': 'string', 'enum': ['rounded_rectangle']}}}], 'required': ['type'], '$schema': 'http://json-schema.org/draft-07/schema'}, 'inactive_minimum_shape': {'$description': 'translations.json#/div_rounded_rectangle_shape', 'allOf': [{'$ref': 'div-shape-base.json'}, {'type': 'object', 'properties': {'item_width': {'$ref': 'div-fixed-size.json', 'default_value': '{"type":"fixed","value":10}', '$description': 'translations.json#/div_rounded_rectangle_shape_item_width'}, 'item_height': {'$ref': 'div-fixed-size.json', 'default_value': '{"type":"fixed","value":10}', '$description': 'translations.json#/div_rounded_rectangle_shape_item_height'}, 'corner_radius': {'$ref': 'div-fixed-size.json', 'default_value': '{"type":"fixed","value":5}', '$description': 'translations.json#/div_rounded_rectangle_shape_corner_radius'}, 'type': {'type': 'string', 'enum': ['rounded_rectangle']}}}], 'required': ['type'], '$schema': 'http://json-schema.org/draft-07/schema'}, 'animation': {'type': 'string', 'enum': ['scale', 'worm', 'slider'], 'default_value': 'scale', '$description': 'translations.json#/div_indicator_animation', 'platforms': ['android', 'ios']}}}], 'required': ['type'], '$schema': 'http://json-schema.org/draft-07/schema'}, rule='required')
 return data

def validate_div_indicator_item_placement_json(data, custom_formats={}, name_prefix=None):
 data_any_of_count19 = 0
 if not data_any_of_count19:
  try:
   validate_div_default_indicator_item_placement_json(data, custom_formats, (name_prefix or "data") + "")
   data_any_of_count19 += 1
  except JsonSchemaValueException: pass
 if not data_any_of_count19:
  try:
   validate_div_stretch_indicator_item_placement_json(data, custom_formats, (name_prefix or "data") + "")
   data_any_of_count19 += 1
  except JsonSchemaValueException: pass
 if not data_any_of_count19:
  if not (isinstance(data, str) and '@' in data):
   raise JsonSchemaValueException("" + (name_prefix or "data") + " cannot be validated by any definition", value=data, name="" + (name_prefix or "data") + "", definition={'anyOf': [{'type': 'object', '$description': 'translations.json#/div_match_parent_size', 'properties': {'space_between_centers': {'$ref': 'div-fixed-size.json', 'default_value': '{"type": "fixed","value":15}', '$description': 'translations.json#/div_indicator_space_between_centers'}, 'type': {'type': 'string', 'enum': ['default']}}, 'required': ['type'], '$schema': 'http://json-schema.org/draft-07/schema'}, {'type': 'object', '$description': 'translations.json#/div_match_parent_size', 'properties': {'item_spacing': {'$ref': 'div-fixed-size.json', 'default_value': '{"type": "fixed","value":5}', '$description': 'translations.json#/div_indicator_space_between_centers'}, 'max_visible_items': {'$ref': 'common.json#/positive_integer', 'default_value': '10', '$description': 'translations.json#/div_indicator_max_visible_items'}, 'type': {'type': 'string', 'enum': ['stretch']}}, 'required': ['type'], '$schema': 'http://json-schema.org/draft-07/schema'}], '$schema': 'http://json-schema.org/draft-07/schema'}, rule='anyOf')
 return data

def validate_div_stretch_indicator_item_placement_json(data, custom_formats={}, name_prefix=None):
 if not isinstance(data, (dict)):
  if not (isinstance(data, str) and '@' in data):
   raise JsonSchemaValueException("" + (name_prefix or "data") + " must be object", value=data, name="" + (name_prefix or "data") + "", definition={'type': 'object', '$description': 'translations.json#/div_match_parent_size', 'properties': {'item_spacing': {'type': 'object', '$description': 'translations.json#/div_fixed_size', 'codegen': {'divan': {'forced_properties_order': ['value']}}, 'properties': {'value': {'$ref': 'common.json#/non_negative_integer', '$description': 'translations.json#/div_fixed_size_value'}, 'unit': {'$ref': 'div-size-unit.json', '$description': 'translations.json#/div_fixed_size_unit', 'default_value': 'dp'}, 'type': {'type': 'string', 'enum': ['fixed']}}, 'required': ['value', 'type'], '$schema': 'http://json-schema.org/draft-07/schema'}, 'max_visible_items': {'type': 'integer', 'constraint': 'number > 0'}, 'type': {'type': 'string', 'enum': ['stretch']}}, 'required': ['type'], '$schema': 'http://json-schema.org/draft-07/schema'}, rule='type')
 data_is_dict = isinstance(data, dict)
 if data_is_dict:
  data__missing_keys = set(['type']) - data.keys()
  if data__missing_keys:
   if not (isinstance(data, str) and '@' in data):
    raise JsonSchemaValueException("" + (name_prefix or "data") + " must contain " + (str(sorted(data__missing_keys)) + " properties"), value=data, name="" + (name_prefix or "data") + "", definition={'type': 'object', '$description': 'translations.json#/div_match_parent_size', 'properties': {'item_spacing': {'type': 'object', '$description': 'translations.json#/div_fixed_size', 'codegen': {'divan': {'forced_properties_order': ['value']}}, 'properties': {'value': {'$ref': 'common.json#/non_negative_integer', '$description': 'translations.json#/div_fixed_size_value'}, 'unit': {'$ref': 'div-size-unit.json', '$description': 'translations.json#/div_fixed_size_unit', 'default_value': 'dp'}, 'type': {'type': 'string', 'enum': ['fixed']}}, 'required': ['value', 'type'], '$schema': 'http://json-schema.org/draft-07/schema'}, 'max_visible_items': {'type': 'integer', 'constraint': 'number > 0'}, 'type': {'type': 'string', 'enum': ['stretch']}}, 'required': ['type'], '$schema': 'http://json-schema.org/draft-07/schema'}, rule='required')
  data_keys = set(data.keys())
  if "item_spacing" in data_keys:
   data_keys.remove("item_spacing")
   data__itemspacing = data["item_spacing"]
   validate_div_fixed_size_json(data__itemspacing, custom_formats, (name_prefix or "data") + ".item_spacing")
  if "max_visible_items" in data_keys:
   data_keys.remove("max_visible_items")
   data__maxvisibleitems = data["max_visible_items"]
   validate_common_json__positive_integer(data__maxvisibleitems, custom_formats, (name_prefix or "data") + ".max_visible_items")
  if "type" in data_keys:
   data_keys.remove("type")
   data__type = data["type"]
   if not isinstance(data__type, (str)):
    if not (isinstance(data__type, str) and '@' in data__type):
     raise JsonSchemaValueException("" + (name_prefix or "data") + ".type must be string", value=data__type, name="" + (name_prefix or "data") + ".type", definition={'type': 'string', 'enum': ['stretch']}, rule='type')
   if data__type not in ['stretch']:
    if not (isinstance(data__type, str) and '@' in data__type):
     raise JsonSchemaValueException("" + (name_prefix or "data") + ".type must be one of ['stretch']", value=data__type, name="" + (name_prefix or "data") + ".type", definition={'type': 'string', 'enum': ['stretch']}, rule='enum')
 return data

def validate_div_default_indicator_item_placement_json(data, custom_formats={}, name_prefix=None):
 if not isinstance(data, (dict)):
  if not (isinstance(data, str) and '@' in data):
   raise JsonSchemaValueException("" + (name_prefix or "data") + " must be object", value=data, name="" + (name_prefix or "data") + "", definition={'type': 'object', '$description': 'translations.json#/div_match_parent_size', 'properties': {'space_between_centers': {'type': 'object', '$description': 'translations.json#/div_fixed_size', 'codegen': {'divan': {'forced_properties_order': ['value']}}, 'properties': {'value': {'$ref': 'common.json#/non_negative_integer', '$description': 'translations.json#/div_fixed_size_value'}, 'unit': {'$ref': 'div-size-unit.json', '$description': 'translations.json#/div_fixed_size_unit', 'default_value': 'dp'}, 'type': {'type': 'string', 'enum': ['fixed']}}, 'required': ['value', 'type'], '$schema': 'http://json-schema.org/draft-07/schema'}, 'type': {'type': 'string', 'enum': ['default']}}, 'required': ['type'], '$schema': 'http://json-schema.org/draft-07/schema'}, rule='type')
 data_is_dict = isinstance(data, dict)
 if data_is_dict:
  data__missing_keys = set(['type']) - data.keys()
  if data__missing_keys:
   if not (isinstance(data, str) and '@' in data):
    raise JsonSchemaValueException("" + (name_prefix or "data") + " must contain " + (str(sorted(data__missing_keys)) + " properties"), value=data, name="" + (name_prefix or "data") + "", definition={'type': 'object', '$description': 'translations.json#/div_match_parent_size', 'properties': {'space_between_centers': {'type': 'object', '$description': 'translations.json#/div_fixed_size', 'codegen': {'divan': {'forced_properties_order': ['value']}}, 'properties': {'value': {'$ref': 'common.json#/non_negative_integer', '$description': 'translations.json#/div_fixed_size_value'}, 'unit': {'$ref': 'div-size-unit.json', '$description': 'translations.json#/div_fixed_size_unit', 'default_value': 'dp'}, 'type': {'type': 'string', 'enum': ['fixed']}}, 'required': ['value', 'type'], '$schema': 'http://json-schema.org/draft-07/schema'}, 'type': {'type': 'string', 'enum': ['default']}}, 'required': ['type'], '$schema': 'http://json-schema.org/draft-07/schema'}, rule='required')
  data_keys = set(data.keys())
  if "space_between_centers" in data_keys:
   data_keys.remove("space_between_centers")
   data__spacebetweencenters = data["space_between_centers"]
   validate_div_fixed_size_json(data__spacebetweencenters, custom_formats, (name_prefix or "data") + ".space_between_centers")
  if "type" in data_keys:
   data_keys.remove("type")
   data__type = data["type"]
   if not isinstance(data__type, (str)):
    if not (isinstance(data__type, str) and '@' in data__type):
     raise JsonSchemaValueException("" + (name_prefix or "data") + ".type must be string", value=data__type, name="" + (name_prefix or "data") + ".type", definition={'type': 'string', 'enum': ['default']}, rule='type')
   if data__type not in ['default']:
    if not (isinstance(data__type, str) and '@' in data__type):
     raise JsonSchemaValueException("" + (name_prefix or "data") + ".type must be one of ['default']", value=data__type, name="" + (name_prefix or "data") + ".type", definition={'type': 'string', 'enum': ['default']}, rule='enum')
 return data

def validate_div_custom_json(data, custom_formats={}, name_prefix=None):
 validate_div_base_json(data, custom_formats, (name_prefix or "data") + "")
 data_is_dict = isinstance(data, dict)
 if data_is_dict:
  data_keys = set(data.keys())
  if "type" in data_keys:
   data_keys.remove("type")
   data__type = data["type"]
   if not isinstance(data__type, (str)):
    if not (isinstance(data__type, str) and '@' in data__type):
     raise JsonSchemaValueException("" + (name_prefix or "data") + ".type must be string", value=data__type, name="" + (name_prefix or "data") + ".type", definition={'type': 'string', 'enum': ['custom']}, rule='type')
   if data__type not in ['custom']:
    if not (isinstance(data__type, str) and '@' in data__type):
     raise JsonSchemaValueException("" + (name_prefix or "data") + ".type must be one of ['custom']", value=data__type, name="" + (name_prefix or "data") + ".type", definition={'type': 'string', 'enum': ['custom']}, rule='enum')
  if "items" in data_keys:
   data_keys.remove("items")
   data__items = data["items"]
   if not isinstance(data__items, (list, tuple)):
    if not (isinstance(data__items, str) and '@' in data__items):
     raise JsonSchemaValueException("" + (name_prefix or "data") + ".items must be array", value=data__items, name="" + (name_prefix or "data") + ".items", definition={'type': 'array', 'items': {'generate_case_for_templates_kotlinDsl': True, 'generate_case_for_templates_typescript': True, 'anyOf': [{'$ref': 'div-image.json', '$description': 'translations.json#/div_image_short'}, {'$ref': 'div-gif-image.json', '$description': 'translations.json#/div_gif_image_short'}, {'$ref': 'div-text.json', '$description': 'translations.json#/div_text_short'}, {'$ref': 'div-separator.json', '$description': 'translations.json#/div_separator_short'}, {'$ref': 'div-container.json', '$description': 'translations.json#/div_container_short'}, {'$ref': 'div-grid.json', '$description': 'translations.json#/div_grid_short'}, {'$ref': 'div-gallery.json', '$description': 'translations.json#/div_gallery_short'}, {'$ref': 'div-pager.json', '$description': 'translations.json#/div_pager_short'}, {'$ref': 'div-tabs.json', '$description': 'translations.json#/div_tabs_short'}, {'$ref': 'div-state.json', '$description': 'translations.json#/div_state_short'}, {'$ref': 'div-custom.json', '$description': 'translations.json#/div_custom_short'}, {'$ref': 'div-indicator.json', '$description': 'translations.json#/div_indicator_short'}, {'$ref': 'div-slider.json', '$description': 'translations.json#/div_slider_short'}, {'$ref': 'div-input.json', '$description': 'translations.json#/div_input_short'}, {'$ref': 'div-select.json', '$description': 'translations.json#/div_select'}, {'$ref': 'div-video.json', '$description': 'translations.json#/div_video'}], '$schema': 'http://json-schema.org/draft-07/schema'}, 'minItems': 1, '$description': 'translations.json#/div_custom_items'}, rule='type')
   data__items_is_list = isinstance(data__items, (list, tuple))
   if data__items_is_list:
    data__items_len = len(data__items)
    if data__items_len < 1:
     if not (isinstance(data__items, str) and '@' in data__items):
      raise JsonSchemaValueException("" + (name_prefix or "data") + ".items must contain at least 1 items", value=data__items, name="" + (name_prefix or "data") + ".items", definition={'type': 'array', 'items': {'generate_case_for_templates_kotlinDsl': True, 'generate_case_for_templates_typescript': True, 'anyOf': [{'$ref': 'div-image.json', '$description': 'translations.json#/div_image_short'}, {'$ref': 'div-gif-image.json', '$description': 'translations.json#/div_gif_image_short'}, {'$ref': 'div-text.json', '$description': 'translations.json#/div_text_short'}, {'$ref': 'div-separator.json', '$description': 'translations.json#/div_separator_short'}, {'$ref': 'div-container.json', '$description': 'translations.json#/div_container_short'}, {'$ref': 'div-grid.json', '$description': 'translations.json#/div_grid_short'}, {'$ref': 'div-gallery.json', '$description': 'translations.json#/div_gallery_short'}, {'$ref': 'div-pager.json', '$description': 'translations.json#/div_pager_short'}, {'$ref': 'div-tabs.json', '$description': 'translations.json#/div_tabs_short'}, {'$ref': 'div-state.json', '$description': 'translations.json#/div_state_short'}, {'$ref': 'div-custom.json', '$description': 'translations.json#/div_custom_short'}, {'$ref': 'div-indicator.json', '$description': 'translations.json#/div_indicator_short'}, {'$ref': 'div-slider.json', '$description': 'translations.json#/div_slider_short'}, {'$ref': 'div-input.json', '$description': 'translations.json#/div_input_short'}, {'$ref': 'div-select.json', '$description': 'translations.json#/div_select'}, {'$ref': 'div-video.json', '$description': 'translations.json#/div_video'}], '$schema': 'http://json-schema.org/draft-07/schema'}, 'minItems': 1, '$description': 'translations.json#/div_custom_items'}, rule='minItems')
    for data__items_x, data__items_item in enumerate(data__items):
     validate_div_json(data__items_item, custom_formats, (name_prefix or "data") + ".items[{data__items_x}]".format(**locals()))
  if "custom_type" in data_keys:
   data_keys.remove("custom_type")
   data__customtype = data["custom_type"]
   if not isinstance(data__customtype, (str)):
    if not (isinstance(data__customtype, str) and '@' in data__customtype):
     raise JsonSchemaValueException("" + (name_prefix or "data") + ".custom_type must be string", value=data__customtype, name="" + (name_prefix or "data") + ".custom_type", definition={'type': 'string', 'supports_expressions': False, '$description': 'translations.json#/div_custom_custom_type'}, rule='type')
  if "custom_props" in data_keys:
   data_keys.remove("custom_props")
   data__customprops = data["custom_props"]
   if not isinstance(data__customprops, (dict)):
    if not (isinstance(data__customprops, str) and '@' in data__customprops):
     raise JsonSchemaValueException("" + (name_prefix or "data") + ".custom_props must be object", value=data__customprops, name="" + (name_prefix or "data") + ".custom_props", definition={'type': 'object', 'additionalProperties': True, '$description': 'translations.json#/div_custom_custom_props'}, rule='type')
   data__customprops_is_dict = isinstance(data__customprops, dict)
   if data__customprops_is_dict:
    data__customprops_keys = set(data__customprops.keys())
 data_is_dict = isinstance(data, dict)
 if data_is_dict:
  data__missing_keys = set(['type', 'custom_type']) - data.keys()
  if data__missing_keys:
   if not (isinstance(data, str) and '@' in data):
    raise JsonSchemaValueException("" + (name_prefix or "data") + " must contain " + (str(sorted(data__missing_keys)) + " properties"), value=data, name="" + (name_prefix or "data") + "", definition={'java_extends': 'DivBlockWithId', '$description': 'translations.json#/div_custom', 'allOf': [{'protocol_name': 'div-base', 'codegen': {'swift': {'super_protocol': 'DivBlockModeling'}, 'documentation': {'include_in_toc': True}}, 'type': 'object', 'properties': {'id': {'$ref': 'common.json#/non_empty_string', 'supports_expressions': False, '$description': 'translations.json#/div_base_id'}, 'border': {'$ref': 'div-border.json', '$description': 'translations.json#/div_base_border'}, 'width': {'$ref': 'div-size.json', 'default_value': '{"type": "match_parent"}', '$description': 'translations.json#/div_base_width'}, 'height': {'$ref': 'div-size.json', 'default_value': '{"type": "wrap_content"}', '$description': 'translations.json#/div_base_height'}, 'background': {'type': 'array', 'items': {'$ref': 'div-background.json'}, 'minItems': 1, '$description': 'translations.json#/div_base_background'}, 'paddings': {'$ref': 'div-edge-insets.json', '$description': 'translations.json#/div_base_paddings'}, 'margins': {'$ref': 'div-edge-insets.json', '$description': 'translations.json#/div_base_margins'}, 'alpha': {'type': 'number', 'default_value': '1.0', 'constraint': 'number >= 0.0 && number <= 1.0', '$description': 'translations.json#/div_base_alpha'}, 'alignment_vertical': {'$ref': 'div-alignment-vertical.json', '$description': 'translations.json#/div_base_alignment_vertical'}, 'alignment_horizontal': {'$ref': 'div-alignment-horizontal.json', '$description': 'translations.json#/div_base_alignment_horizontal'}, 'row_span': {'$ref': 'common.json#/non_negative_integer', '$description': 'translations.json#/div_base_row_span'}, 'column_span': {'$ref': 'common.json#/non_negative_integer', '$description': 'translations.json#/div_base_column_span'}, 'visibility_action': {'$ref': 'div-visibility-action.json', '$description': 'translations.json#/div_base_visibility_action'}, 'visibility_actions': {'type': 'array', 'items': {'$ref': 'div-visibility-action.json'}, 'minItems': 1, '$description': 'translations.json#/div_base_visibility_actions'}, 'disappear_actions': {'type': 'array', 'items': {'$ref': 'div-disappear-action.json'}, 'minItems': 1, '$description': 'translations.json#/div_base_disappear_actions'}, 'tooltips': {'type': 'array', 'items': {'$ref': 'div-tooltip.json'}, 'minItems': 1, '$description': 'translations.json#/div_base_tooltips'}, 'accessibility': {'$ref': 'div-accessibility.json', '$description': 'translations.json#/div_base_accessibility'}, 'extensions': {'type': 'array', 'items': {'$ref': 'div-extension.json'}, 'minItems': 1, '$description': 'translations.json#/div_base_extensions'}, 'transition_triggers': {'type': 'array', 'items': {'$ref': 'div-transition-trigger.json'}, 'minItems': 1, 'supports_expressions': False, '$description': 'translations.json#/div_base_transition_triggers'}, 'transition_in': {'$ref': 'div-appearance-transition.json', '$description': 'translations.json#/div_base_transition_in'}, 'transition_change': {'$ref': 'div-change-transition.json', '$description': 'translations.json#/div_base_transition_change'}, 'transition_out': {'$ref': 'div-appearance-transition.json', '$description': 'translations.json#/div_base_transition_out'}, 'selected_actions': {'type': 'array', 'items': {'$ref': 'div-action.json'}, 'minItems': 1, '$description': 'translations.json#/div_base_selected_actions'}, 'focus': {'$ref': 'div-focus.json', '$description': 'translations.json#/div_base_focus', 'platforms': ['android', 'ios']}, 'visibility': {'$ref': 'div-visibility.json', '$description': 'translations.json#/div_base_visibility', 'default_value': 'visible'}, 'transform': {'$ref': 'div-transform.json', '$description': 'translations.json#/div_base_transform'}}, '$schema': 'http://json-schema.org/draft-07/schema'}, {'properties': {'type': {'type': 'string', 'enum': ['custom']}, 'items': {'type': 'array', 'items': {'generate_case_for_templates_kotlinDsl': True, 'generate_case_for_templates_typescript': True, 'anyOf': [{'$ref': 'div-image.json', '$description': 'translations.json#/div_image_short'}, {'$ref': 'div-gif-image.json', '$description': 'translations.json#/div_gif_image_short'}, {'$ref': 'div-text.json', '$description': 'translations.json#/div_text_short'}, {'$ref': 'div-separator.json', '$description': 'translations.json#/div_separator_short'}, {'$ref': 'div-container.json', '$description': 'translations.json#/div_container_short'}, {'$ref': 'div-grid.json', '$description': 'translations.json#/div_grid_short'}, {'$ref': 'div-gallery.json', '$description': 'translations.json#/div_gallery_short'}, {'$ref': 'div-pager.json', '$description': 'translations.json#/div_pager_short'}, {'$ref': 'div-tabs.json', '$description': 'translations.json#/div_tabs_short'}, {'$ref': 'div-state.json', '$description': 'translations.json#/div_state_short'}, {'$ref': 'div-custom.json', '$description': 'translations.json#/div_custom_short'}, {'$ref': 'div-indicator.json', '$description': 'translations.json#/div_indicator_short'}, {'$ref': 'div-slider.json', '$description': 'translations.json#/div_slider_short'}, {'$ref': 'div-input.json', '$description': 'translations.json#/div_input_short'}, {'$ref': 'div-select.json', '$description': 'translations.json#/div_select'}, {'$ref': 'div-video.json', '$description': 'translations.json#/div_video'}], '$schema': 'http://json-schema.org/draft-07/schema'}, 'minItems': 1, '$description': 'translations.json#/div_custom_items'}, 'custom_type': {'type': 'string', 'supports_expressions': False, '$description': 'translations.json#/div_custom_custom_type'}, 'custom_props': {'type': 'object', 'additionalProperties': True, '$description': 'translations.json#/div_custom_custom_props'}}}], 'required': ['type', 'custom_type'], '$schema': 'http://json-schema.org/draft-07/schema'}, rule='required')
 return data

def validate_div_state_json(data, custom_formats={}, name_prefix=None):
 validate_div_base_json(data, custom_formats, (name_prefix or "data") + "")
 data_is_dict = isinstance(data, dict)
 if data_is_dict:
  data__missing_keys = set(['type', 'states']) - data.keys()
  if data__missing_keys:
   if not (isinstance(data, str) and '@' in data):
    raise JsonSchemaValueException("" + (name_prefix or "data") + " must contain " + (str(sorted(data__missing_keys)) + " properties"), value=data, name="" + (name_prefix or "data") + "", definition={'properties': {'type': {'type': 'string', 'enum': ['state']}, 'states': {'type': 'array', 'items': {'type': 'object', 'alias_divan': 'item', 'codegen': {'swift': {'generate_optional_arguments': False}}, 'properties': {'state_id': {'type': 'string', 'supports_expressions': False, '$description': 'translations.json#/div_state_div_state_state_id'}, 'div': {'$ref': 'div.json', '$description': 'translations.json#/div_state_div_state_div'}, 'animation_in': {'$ref': 'div-animation.json', '$description': 'translations.json#/div_state_div_state_animation_in', 'platforms': ['android', 'ios'], 'deprecated': True}, 'animation_out': {'$ref': 'div-animation.json', '$description': 'translations.json#/div_state_div_state_animation_out', 'platforms': ['android', 'ios'], 'deprecated': True}, 'swipe_out_actions': {'type': 'array', 'items': {'$ref': 'div-action.json'}, 'minItems': 1, '$description': 'translations.json#/div_state_div_state_swipe_out_actions', 'platforms': ['android'], 'deprecated': True}}, 'required': ['state_id']}, 'minItems': 1, '$description': 'translations.json#/div_state_states'}, 'state_id_variable': {'supports_expressions': False, '$ref': 'common.json#/non_empty_string', '$schema': 'http://json-schema.org/draft-07/schema'}, 'div_id': {'type': 'string', 'supports_expressions': False, '$description': 'translations.json#/div_state_div_id', 'deprecated': True}, 'default_state_id': {'type': 'string', '$description': 'translations.json#/div_state_default_state_id'}, 'transition_animation_selector': {'type': 'string', 'enum': ['none', 'data_change', 'state_change', 'any_change'], '$description': 'translations.json#/div_transition_selector', 'deprecated': True, '$schema': 'http://json-schema.org/draft-07/schema'}}, 'required': ['type', 'states']}, rule='required')
  data_keys = set(data.keys())
  if "type" in data_keys:
   data_keys.remove("type")
   data__type = data["type"]
   if not isinstance(data__type, (str)):
    if not (isinstance(data__type, str) and '@' in data__type):
     raise JsonSchemaValueException("" + (name_prefix or "data") + ".type must be string", value=data__type, name="" + (name_prefix or "data") + ".type", definition={'type': 'string', 'enum': ['state']}, rule='type')
   if data__type not in ['state']:
    if not (isinstance(data__type, str) and '@' in data__type):
     raise JsonSchemaValueException("" + (name_prefix or "data") + ".type must be one of ['state']", value=data__type, name="" + (name_prefix or "data") + ".type", definition={'type': 'string', 'enum': ['state']}, rule='enum')
  if "states" in data_keys:
   data_keys.remove("states")
   data__states = data["states"]
   if not isinstance(data__states, (list, tuple)):
    if not (isinstance(data__states, str) and '@' in data__states):
     raise JsonSchemaValueException("" + (name_prefix or "data") + ".states must be array", value=data__states, name="" + (name_prefix or "data") + ".states", definition={'type': 'array', 'items': {'type': 'object', 'alias_divan': 'item', 'codegen': {'swift': {'generate_optional_arguments': False}}, 'properties': {'state_id': {'type': 'string', 'supports_expressions': False, '$description': 'translations.json#/div_state_div_state_state_id'}, 'div': {'$ref': 'div.json', '$description': 'translations.json#/div_state_div_state_div'}, 'animation_in': {'$ref': 'div-animation.json', '$description': 'translations.json#/div_state_div_state_animation_in', 'platforms': ['android', 'ios'], 'deprecated': True}, 'animation_out': {'$ref': 'div-animation.json', '$description': 'translations.json#/div_state_div_state_animation_out', 'platforms': ['android', 'ios'], 'deprecated': True}, 'swipe_out_actions': {'type': 'array', 'items': {'$ref': 'div-action.json'}, 'minItems': 1, '$description': 'translations.json#/div_state_div_state_swipe_out_actions', 'platforms': ['android'], 'deprecated': True}}, 'required': ['state_id']}, 'minItems': 1, '$description': 'translations.json#/div_state_states'}, rule='type')
   data__states_is_list = isinstance(data__states, (list, tuple))
   if data__states_is_list:
    data__states_len = len(data__states)
    if data__states_len < 1:
     if not (isinstance(data__states, str) and '@' in data__states):
      raise JsonSchemaValueException("" + (name_prefix or "data") + ".states must contain at least 1 items", value=data__states, name="" + (name_prefix or "data") + ".states", definition={'type': 'array', 'items': {'type': 'object', 'alias_divan': 'item', 'codegen': {'swift': {'generate_optional_arguments': False}}, 'properties': {'state_id': {'type': 'string', 'supports_expressions': False, '$description': 'translations.json#/div_state_div_state_state_id'}, 'div': {'$ref': 'div.json', '$description': 'translations.json#/div_state_div_state_div'}, 'animation_in': {'$ref': 'div-animation.json', '$description': 'translations.json#/div_state_div_state_animation_in', 'platforms': ['android', 'ios'], 'deprecated': True}, 'animation_out': {'$ref': 'div-animation.json', '$description': 'translations.json#/div_state_div_state_animation_out', 'platforms': ['android', 'ios'], 'deprecated': True}, 'swipe_out_actions': {'type': 'array', 'items': {'$ref': 'div-action.json'}, 'minItems': 1, '$description': 'translations.json#/div_state_div_state_swipe_out_actions', 'platforms': ['android'], 'deprecated': True}}, 'required': ['state_id']}, 'minItems': 1, '$description': 'translations.json#/div_state_states'}, rule='minItems')
    for data__states_x, data__states_item in enumerate(data__states):
     validate_div_state_json__definitions_div_state(data__states_item, custom_formats, (name_prefix or "data") + ".states[{data__states_x}]".format(**locals()))
  if "state_id_variable" in data_keys:
   data_keys.remove("state_id_variable")
   data__stateidvariable = data["state_id_variable"]
   validate_div_variable_name_json(data__stateidvariable, custom_formats, (name_prefix or "data") + ".state_id_variable")
  if "div_id" in data_keys:
   data_keys.remove("div_id")
   data__divid = data["div_id"]
   if not isinstance(data__divid, (str)):
    if not (isinstance(data__divid, str) and '@' in data__divid):
     raise JsonSchemaValueException("" + (name_prefix or "data") + ".div_id must be string", value=data__divid, name="" + (name_prefix or "data") + ".div_id", definition={'type': 'string', 'supports_expressions': False, '$description': 'translations.json#/div_state_div_id', 'deprecated': True}, rule='type')
  if "default_state_id" in data_keys:
   data_keys.remove("default_state_id")
   data__defaultstateid = data["default_state_id"]
   if not isinstance(data__defaultstateid, (str)):
    if not (isinstance(data__defaultstateid, str) and '@' in data__defaultstateid):
     raise JsonSchemaValueException("" + (name_prefix or "data") + ".default_state_id must be string", value=data__defaultstateid, name="" + (name_prefix or "data") + ".default_state_id", definition={'type': 'string', '$description': 'translations.json#/div_state_default_state_id'}, rule='type')
  if "transition_animation_selector" in data_keys:
   data_keys.remove("transition_animation_selector")
   data__transitionanimationselector = data["transition_animation_selector"]
   validate_div_transition_selector_json(data__transitionanimationselector, custom_formats, (name_prefix or "data") + ".transition_animation_selector")
 return data

def validate_div_transition_selector_json(data, custom_formats={}, name_prefix=None):
 if not isinstance(data, (str)):
  if not (isinstance(data, str) and '@' in data):
   raise JsonSchemaValueException("" + (name_prefix or "data") + " must be string", value=data, name="" + (name_prefix or "data") + "", definition={'type': 'string', 'enum': ['none', 'data_change', 'state_change', 'any_change'], '$description': 'translations.json#/div_transition_selector', 'deprecated': True, '$schema': 'http://json-schema.org/draft-07/schema'}, rule='type')
 if data not in ['none', 'data_change', 'state_change', 'any_change']:
  if not (isinstance(data, str) and '@' in data):
   raise JsonSchemaValueException("" + (name_prefix or "data") + " must be one of ['none', 'data_change', 'state_change', 'any_change']", value=data, name="" + (name_prefix or "data") + "", definition={'type': 'string', 'enum': ['none', 'data_change', 'state_change', 'any_change'], '$description': 'translations.json#/div_transition_selector', 'deprecated': True, '$schema': 'http://json-schema.org/draft-07/schema'}, rule='enum')
 return data

def validate_div_state_json__definitions_div_state(data, custom_formats={}, name_prefix=None):
 if not isinstance(data, (dict)):
  if not (isinstance(data, str) and '@' in data):
   raise JsonSchemaValueException("" + (name_prefix or "data") + " must be object", value=data, name="" + (name_prefix or "data") + "", definition={'type': 'object', 'alias_divan': 'item', 'codegen': {'swift': {'generate_optional_arguments': False}}, 'properties': {'state_id': {'type': 'string', 'supports_expressions': False, '$description': 'translations.json#/div_state_div_state_state_id'}, 'div': {'generate_case_for_templates_kotlinDsl': True, 'generate_case_for_templates_typescript': True, 'anyOf': [{'$ref': 'div-image.json', '$description': 'translations.json#/div_image_short'}, {'$ref': 'div-gif-image.json', '$description': 'translations.json#/div_gif_image_short'}, {'$ref': 'div-text.json', '$description': 'translations.json#/div_text_short'}, {'$ref': 'div-separator.json', '$description': 'translations.json#/div_separator_short'}, {'$ref': 'div-container.json', '$description': 'translations.json#/div_container_short'}, {'$ref': 'div-grid.json', '$description': 'translations.json#/div_grid_short'}, {'$ref': 'div-gallery.json', '$description': 'translations.json#/div_gallery_short'}, {'$ref': 'div-pager.json', '$description': 'translations.json#/div_pager_short'}, {'$ref': 'div-tabs.json', '$description': 'translations.json#/div_tabs_short'}, {'$ref': 'div-state.json', '$description': 'translations.json#/div_state_short'}, {'$ref': 'div-custom.json', '$description': 'translations.json#/div_custom_short'}, {'$ref': 'div-indicator.json', '$description': 'translations.json#/div_indicator_short'}, {'$ref': 'div-slider.json', '$description': 'translations.json#/div_slider_short'}, {'$ref': 'div-input.json', '$description': 'translations.json#/div_input_short'}, {'$ref': 'div-select.json', '$description': 'translations.json#/div_select'}, {'$ref': 'div-video.json', '$description': 'translations.json#/div_video'}], '$schema': 'http://json-schema.org/draft-07/schema'}, 'animation_in': {'type': 'object', '$description': 'translations.json#/div_animation', 'properties': {'name': {'type': 'string', 'enum': ['fade', 'translate', 'scale', 'native', 'set', 'no_animation'], '$description': 'translations.json#/div_animation_name'}, 'duration': {'$ref': 'common.json#/non_negative_integer', 'default_value': '300', '$description': 'translations.json#/div_animation_duration'}, 'start_delay': {'$ref': 'common.json#/non_negative_integer', 'default_value': '0', '$description': 'translations.json#/div_animation_start_delay'}, 'start_value': {'type': 'number', '$description': 'translations.json#/div_animation_start_value'}, 'end_value': {'type': 'number', '$description': 'translations.json#/div_animation_end_value'}, 'repeat': {'alias_swift': 'repeat_count', '$ref': 'div-count.json', 'default_value': '{ "type": "infinity" }', '$description': 'translations.json#/div_animation_repeat'}, 'interpolator': {'$ref': 'div-animation-interpolator.json', 'default_value': 'spring', '$description': 'translations.json#/div_animation_interpolator'}, 'items': {'type': 'array', 'items': {'$ref': 'div-animation.json'}, 'minItems': 1, '$description': 'translations.json#/div_animation_items'}}, 'required': ['name'], '$schema': 'http://json-schema.org/draft-07/schema'}, 'animation_out': {'type': 'object', '$description': 'translations.json#/div_animation', 'properties': {'name': {'type': 'string', 'enum': ['fade', 'translate', 'scale', 'native', 'set', 'no_animation'], '$description': 'translations.json#/div_animation_name'}, 'duration': {'$ref': 'common.json#/non_negative_integer', 'default_value': '300', '$description': 'translations.json#/div_animation_duration'}, 'start_delay': {'$ref': 'common.json#/non_negative_integer', 'default_value': '0', '$description': 'translations.json#/div_animation_start_delay'}, 'start_value': {'type': 'number', '$description': 'translations.json#/div_animation_start_value'}, 'end_value': {'type': 'number', '$description': 'translations.json#/div_animation_end_value'}, 'repeat': {'alias_swift': 'repeat_count', '$ref': 'div-count.json', 'default_value': '{ "type": "infinity" }', '$description': 'translations.json#/div_animation_repeat'}, 'interpolator': {'$ref': 'div-animation-interpolator.json', 'default_value': 'spring', '$description': 'translations.json#/div_animation_interpolator'}, 'items': {'type': 'array', 'items': {'$ref': 'div-animation.json'}, 'minItems': 1, '$description': 'translations.json#/div_animation_items'}}, 'required': ['name'], '$schema': 'http://json-schema.org/draft-07/schema'}, 'swipe_out_actions': {'type': 'array', 'items': {'definitions': {'menu_item': {'type': 'object', 'properties': {'text': {'$ref': 'common.json#/non_empty_string', '$description': 'translations.json#/div_action_menu_item_text'}, 'action': {'$ref': 'div-action.json', '$description': 'translations.json#/div_action_menu_item_action'}, 'actions': {'type': 'array', 'items': {'$ref': 'div-action.json'}, 'minItems': 1, '$description': 'translations.json#/div_action_menu_item_actions'}}, 'required': ['text']}}, 'allOf': [{'$ref': 'div-action-base.json'}, {'type': 'object', '$description': 'translations.json#/div_action', 'properties': {'menu_items': {'type': 'array', 'items': {'$ref': '#/definitions/menu_item'}, '$description': 'translations.json#/div_action_menu_items', 'platforms': ['android', 'ios']}, 'log_url': {'$ref': 'common.json#/url', '$description': 'translations.json#/div_action_log_url'}, 'target': {'type': 'string', 'enum': ['_self', '_blank'], 'force_enum_field': True, '$description': 'translations.json#/div_action_target', 'platforms': ['web'], 'code_generation_disabled_swift': True}}, 'required': ['log_id']}], '$schema': 'http://json-schema.org/draft-07/schema'}, 'minItems': 1, '$description': 'translations.json#/div_state_div_state_swipe_out_actions', 'platforms': ['android'], 'deprecated': True}}, 'required': ['state_id']}, rule='type')
 data_is_dict = isinstance(data, dict)
 if data_is_dict:
  data__missing_keys = set(['state_id']) - data.keys()
  if data__missing_keys:
   if not (isinstance(data, str) and '@' in data):
    raise JsonSchemaValueException("" + (name_prefix or "data") + " must contain " + (str(sorted(data__missing_keys)) + " properties"), value=data, name="" + (name_prefix or "data") + "", definition={'type': 'object', 'alias_divan': 'item', 'codegen': {'swift': {'generate_optional_arguments': False}}, 'properties': {'state_id': {'type': 'string', 'supports_expressions': False, '$description': 'translations.json#/div_state_div_state_state_id'}, 'div': {'generate_case_for_templates_kotlinDsl': True, 'generate_case_for_templates_typescript': True, 'anyOf': [{'$ref': 'div-image.json', '$description': 'translations.json#/div_image_short'}, {'$ref': 'div-gif-image.json', '$description': 'translations.json#/div_gif_image_short'}, {'$ref': 'div-text.json', '$description': 'translations.json#/div_text_short'}, {'$ref': 'div-separator.json', '$description': 'translations.json#/div_separator_short'}, {'$ref': 'div-container.json', '$description': 'translations.json#/div_container_short'}, {'$ref': 'div-grid.json', '$description': 'translations.json#/div_grid_short'}, {'$ref': 'div-gallery.json', '$description': 'translations.json#/div_gallery_short'}, {'$ref': 'div-pager.json', '$description': 'translations.json#/div_pager_short'}, {'$ref': 'div-tabs.json', '$description': 'translations.json#/div_tabs_short'}, {'$ref': 'div-state.json', '$description': 'translations.json#/div_state_short'}, {'$ref': 'div-custom.json', '$description': 'translations.json#/div_custom_short'}, {'$ref': 'div-indicator.json', '$description': 'translations.json#/div_indicator_short'}, {'$ref': 'div-slider.json', '$description': 'translations.json#/div_slider_short'}, {'$ref': 'div-input.json', '$description': 'translations.json#/div_input_short'}, {'$ref': 'div-select.json', '$description': 'translations.json#/div_select'}, {'$ref': 'div-video.json', '$description': 'translations.json#/div_video'}], '$schema': 'http://json-schema.org/draft-07/schema'}, 'animation_in': {'type': 'object', '$description': 'translations.json#/div_animation', 'properties': {'name': {'type': 'string', 'enum': ['fade', 'translate', 'scale', 'native', 'set', 'no_animation'], '$description': 'translations.json#/div_animation_name'}, 'duration': {'$ref': 'common.json#/non_negative_integer', 'default_value': '300', '$description': 'translations.json#/div_animation_duration'}, 'start_delay': {'$ref': 'common.json#/non_negative_integer', 'default_value': '0', '$description': 'translations.json#/div_animation_start_delay'}, 'start_value': {'type': 'number', '$description': 'translations.json#/div_animation_start_value'}, 'end_value': {'type': 'number', '$description': 'translations.json#/div_animation_end_value'}, 'repeat': {'alias_swift': 'repeat_count', '$ref': 'div-count.json', 'default_value': '{ "type": "infinity" }', '$description': 'translations.json#/div_animation_repeat'}, 'interpolator': {'$ref': 'div-animation-interpolator.json', 'default_value': 'spring', '$description': 'translations.json#/div_animation_interpolator'}, 'items': {'type': 'array', 'items': {'$ref': 'div-animation.json'}, 'minItems': 1, '$description': 'translations.json#/div_animation_items'}}, 'required': ['name'], '$schema': 'http://json-schema.org/draft-07/schema'}, 'animation_out': {'type': 'object', '$description': 'translations.json#/div_animation', 'properties': {'name': {'type': 'string', 'enum': ['fade', 'translate', 'scale', 'native', 'set', 'no_animation'], '$description': 'translations.json#/div_animation_name'}, 'duration': {'$ref': 'common.json#/non_negative_integer', 'default_value': '300', '$description': 'translations.json#/div_animation_duration'}, 'start_delay': {'$ref': 'common.json#/non_negative_integer', 'default_value': '0', '$description': 'translations.json#/div_animation_start_delay'}, 'start_value': {'type': 'number', '$description': 'translations.json#/div_animation_start_value'}, 'end_value': {'type': 'number', '$description': 'translations.json#/div_animation_end_value'}, 'repeat': {'alias_swift': 'repeat_count', '$ref': 'div-count.json', 'default_value': '{ "type": "infinity" }', '$description': 'translations.json#/div_animation_repeat'}, 'interpolator': {'$ref': 'div-animation-interpolator.json', 'default_value': 'spring', '$description': 'translations.json#/div_animation_interpolator'}, 'items': {'type': 'array', 'items': {'$ref': 'div-animation.json'}, 'minItems': 1, '$description': 'translations.json#/div_animation_items'}}, 'required': ['name'], '$schema': 'http://json-schema.org/draft-07/schema'}, 'swipe_out_actions': {'type': 'array', 'items': {'definitions': {'menu_item': {'type': 'object', 'properties': {'text': {'$ref': 'common.json#/non_empty_string', '$description': 'translations.json#/div_action_menu_item_text'}, 'action': {'$ref': 'div-action.json', '$description': 'translations.json#/div_action_menu_item_action'}, 'actions': {'type': 'array', 'items': {'$ref': 'div-action.json'}, 'minItems': 1, '$description': 'translations.json#/div_action_menu_item_actions'}}, 'required': ['text']}}, 'allOf': [{'$ref': 'div-action-base.json'}, {'type': 'object', '$description': 'translations.json#/div_action', 'properties': {'menu_items': {'type': 'array', 'items': {'$ref': '#/definitions/menu_item'}, '$description': 'translations.json#/div_action_menu_items', 'platforms': ['android', 'ios']}, 'log_url': {'$ref': 'common.json#/url', '$description': 'translations.json#/div_action_log_url'}, 'target': {'type': 'string', 'enum': ['_self', '_blank'], 'force_enum_field': True, '$description': 'translations.json#/div_action_target', 'platforms': ['web'], 'code_generation_disabled_swift': True}}, 'required': ['log_id']}], '$schema': 'http://json-schema.org/draft-07/schema'}, 'minItems': 1, '$description': 'translations.json#/div_state_div_state_swipe_out_actions', 'platforms': ['android'], 'deprecated': True}}, 'required': ['state_id']}, rule='required')
  data_keys = set(data.keys())
  if "state_id" in data_keys:
   data_keys.remove("state_id")
   data__stateid = data["state_id"]
   if not isinstance(data__stateid, (str)):
    if not (isinstance(data__stateid, str) and '@' in data__stateid):
     raise JsonSchemaValueException("" + (name_prefix or "data") + ".state_id must be string", value=data__stateid, name="" + (name_prefix or "data") + ".state_id", definition={'type': 'string', 'supports_expressions': False, '$description': 'translations.json#/div_state_div_state_state_id'}, rule='type')
  if "div" in data_keys:
   data_keys.remove("div")
   data__div = data["div"]
   validate_div_json(data__div, custom_formats, (name_prefix or "data") + ".div")
  if "animation_in" in data_keys:
   data_keys.remove("animation_in")
   data__animationin = data["animation_in"]
   validate_div_animation_json(data__animationin, custom_formats, (name_prefix or "data") + ".animation_in")
  if "animation_out" in data_keys:
   data_keys.remove("animation_out")
   data__animationout = data["animation_out"]
   validate_div_animation_json(data__animationout, custom_formats, (name_prefix or "data") + ".animation_out")
  if "swipe_out_actions" in data_keys:
   data_keys.remove("swipe_out_actions")
   data__swipeoutactions = data["swipe_out_actions"]
   if not isinstance(data__swipeoutactions, (list, tuple)):
    if not (isinstance(data__swipeoutactions, str) and '@' in data__swipeoutactions):
     raise JsonSchemaValueException("" + (name_prefix or "data") + ".swipe_out_actions must be array", value=data__swipeoutactions, name="" + (name_prefix or "data") + ".swipe_out_actions", definition={'type': 'array', 'items': {'definitions': {'menu_item': {'type': 'object', 'properties': {'text': {'$ref': 'common.json#/non_empty_string', '$description': 'translations.json#/div_action_menu_item_text'}, 'action': {'$ref': 'div-action.json', '$description': 'translations.json#/div_action_menu_item_action'}, 'actions': {'type': 'array', 'items': {'$ref': 'div-action.json'}, 'minItems': 1, '$description': 'translations.json#/div_action_menu_item_actions'}}, 'required': ['text']}}, 'allOf': [{'$ref': 'div-action-base.json'}, {'type': 'object', '$description': 'translations.json#/div_action', 'properties': {'menu_items': {'type': 'array', 'items': {'$ref': '#/definitions/menu_item'}, '$description': 'translations.json#/div_action_menu_items', 'platforms': ['android', 'ios']}, 'log_url': {'$ref': 'common.json#/url', '$description': 'translations.json#/div_action_log_url'}, 'target': {'type': 'string', 'enum': ['_self', '_blank'], 'force_enum_field': True, '$description': 'translations.json#/div_action_target', 'platforms': ['web'], 'code_generation_disabled_swift': True}}, 'required': ['log_id']}], '$schema': 'http://json-schema.org/draft-07/schema'}, 'minItems': 1, '$description': 'translations.json#/div_state_div_state_swipe_out_actions', 'platforms': ['android'], 'deprecated': True}, rule='type')
   data__swipeoutactions_is_list = isinstance(data__swipeoutactions, (list, tuple))
   if data__swipeoutactions_is_list:
    data__swipeoutactions_len = len(data__swipeoutactions)
    if data__swipeoutactions_len < 1:
     if not (isinstance(data__swipeoutactions, str) and '@' in data__swipeoutactions):
      raise JsonSchemaValueException("" + (name_prefix or "data") + ".swipe_out_actions must contain at least 1 items", value=data__swipeoutactions, name="" + (name_prefix or "data") + ".swipe_out_actions", definition={'type': 'array', 'items': {'definitions': {'menu_item': {'type': 'object', 'properties': {'text': {'$ref': 'common.json#/non_empty_string', '$description': 'translations.json#/div_action_menu_item_text'}, 'action': {'$ref': 'div-action.json', '$description': 'translations.json#/div_action_menu_item_action'}, 'actions': {'type': 'array', 'items': {'$ref': 'div-action.json'}, 'minItems': 1, '$description': 'translations.json#/div_action_menu_item_actions'}}, 'required': ['text']}}, 'allOf': [{'$ref': 'div-action-base.json'}, {'type': 'object', '$description': 'translations.json#/div_action', 'properties': {'menu_items': {'type': 'array', 'items': {'$ref': '#/definitions/menu_item'}, '$description': 'translations.json#/div_action_menu_items', 'platforms': ['android', 'ios']}, 'log_url': {'$ref': 'common.json#/url', '$description': 'translations.json#/div_action_log_url'}, 'target': {'type': 'string', 'enum': ['_self', '_blank'], 'force_enum_field': True, '$description': 'translations.json#/div_action_target', 'platforms': ['web'], 'code_generation_disabled_swift': True}}, 'required': ['log_id']}], '$schema': 'http://json-schema.org/draft-07/schema'}, 'minItems': 1, '$description': 'translations.json#/div_state_div_state_swipe_out_actions', 'platforms': ['android'], 'deprecated': True}, rule='minItems')
    for data__swipeoutactions_x, data__swipeoutactions_item in enumerate(data__swipeoutactions):
     validate_div_action_json(data__swipeoutactions_item, custom_formats, (name_prefix or "data") + ".swipe_out_actions[{data__swipeoutactions_x}]".format(**locals()))
 return data

def validate_div_tabs_json(data, custom_formats={}, name_prefix=None):
 validate_div_base_json(data, custom_formats, (name_prefix or "data") + "")
 data_is_dict = isinstance(data, dict)
 if data_is_dict:
  data_keys = set(data.keys())
  if "type" in data_keys:
   data_keys.remove("type")
   data__type = data["type"]
   if not isinstance(data__type, (str)):
    if not (isinstance(data__type, str) and '@' in data__type):
     raise JsonSchemaValueException("" + (name_prefix or "data") + ".type must be string", value=data__type, name="" + (name_prefix or "data") + ".type", definition={'type': 'string', 'enum': ['tabs']}, rule='type')
   if data__type not in ['tabs']:
    if not (isinstance(data__type, str) and '@' in data__type):
     raise JsonSchemaValueException("" + (name_prefix or "data") + ".type must be one of ['tabs']", value=data__type, name="" + (name_prefix or "data") + ".type", definition={'type': 'string', 'enum': ['tabs']}, rule='enum')
  if "title_paddings" in data_keys:
   data_keys.remove("title_paddings")
   data__titlepaddings = data["title_paddings"]
   validate_div_edge_insets_json(data__titlepaddings, custom_formats, (name_prefix or "data") + ".title_paddings")
  if "separator_paddings" in data_keys:
   data_keys.remove("separator_paddings")
   data__separatorpaddings = data["separator_paddings"]
   validate_div_edge_insets_json(data__separatorpaddings, custom_formats, (name_prefix or "data") + ".separator_paddings")
  if "tab_title_style" in data_keys:
   data_keys.remove("tab_title_style")
   data__tabtitlestyle = data["tab_title_style"]
   if not isinstance(data__tabtitlestyle, (dict)):
    if not (isinstance(data__tabtitlestyle, str) and '@' in data__tabtitlestyle):
     raise JsonSchemaValueException("" + (name_prefix or "data") + ".tab_title_style must be object", value=data__tabtitlestyle, name="" + (name_prefix or "data") + ".tab_title_style", definition={'type': 'object', 'properties': {'font_size': {'type': 'integer', 'constraint': 'number >= 0'}, 'font_size_unit': {'type': 'string', 'enum': ['dp', 'sp', 'px'], '$description': 'translations.json#/div_size_unit', 'platforms': ['android', 'ios'], '$schema': 'http://json-schema.org/draft-07/schema'}, 'paddings': {'type': 'object', '$description': 'translations.json#/div_edge_insets', 'properties': {'left': {'$ref': 'common.json#/non_negative_integer', 'default_value': '0', '$description': 'translations.json#/div_edge_insets_left'}, 'right': {'$ref': 'common.json#/non_negative_integer', 'default_value': '0', '$description': 'translations.json#/div_edge_insets_right'}, 'top': {'$ref': 'common.json#/non_negative_integer', 'default_value': '0', '$description': 'translations.json#/div_edge_insets_top'}, 'bottom': {'$ref': 'common.json#/non_negative_integer', 'default_value': '0', '$description': 'translations.json#/div_edge_insets_bottom'}, 'start': {'$ref': 'common.json#/non_negative_integer', '$description': 'translations.json#/div_edge_insets_start', 'platforms': []}, 'end': {'$ref': 'common.json#/non_negative_integer', '$description': 'translations.json#/div_edge_insets_end', 'platforms': []}, 'unit': {'$ref': 'div-size-unit.json', 'default_value': 'dp'}}, '$schema': 'http://json-schema.org/draft-07/schema'}, 'item_spacing': {'type': 'integer', 'constraint': 'number >= 0'}, 'line_height': {'type': 'integer', 'constraint': 'number >= 0'}, 'letter_spacing': {'type': 'number', 'default_value': '0', '$description': 'translations.json#/div_tabs_tab_title_style_letter_spacing'}, 'font_weight': {'type': 'string', 'enum': ['light', 'medium', 'regular', 'bold'], '$schema': 'http://json-schema.org/draft-07/schema'}, 'active_font_weight': {'type': 'string', 'enum': ['light', 'medium', 'regular', 'bold'], '$schema': 'http://json-schema.org/draft-07/schema'}, 'inactive_font_weight': {'type': 'string', 'enum': ['light', 'medium', 'regular', 'bold'], '$schema': 'http://json-schema.org/draft-07/schema'}, 'font_family': {'type': 'string', 'minLength': 1, 'clientMinLength': 1}, 'active_text_color': {'type': 'string', 'format': 'color'}, 'inactive_text_color': {'type': 'string', 'format': 'color'}, 'active_background_color': {'type': 'string', 'format': 'color'}, 'inactive_background_color': {'type': 'string', 'format': 'color'}, 'corner_radius': {'type': 'integer', 'constraint': 'number >= 0'}, 'corners_radius': {'type': 'object', '$description': 'translations.json#/div_corners_radius', 'properties': {'top-left': {'$ref': 'common.json#/non_negative_integer', '$description': 'translations.json#/div_corners_radius_top_left'}, 'top-right': {'$ref': 'common.json#/non_negative_integer', '$description': 'translations.json#/div_corners_radius_top_right'}, 'bottom-left': {'$ref': 'common.json#/non_negative_integer', '$description': 'translations.json#/div_corners_radius_bottom_left'}, 'bottom-right': {'$ref': 'common.json#/non_negative_integer', '$description': 'translations.json#/div_corners_radius_bottom_right'}}, '$schema': 'http://json-schema.org/draft-07/schema'}, 'animation_type': {'type': 'string', 'enum': ['slide', 'fade', 'none'], 'default_value': 'slide', '$description': 'translations.json#/div_tabs_tab_title_style_animation_type', 'platforms': ['android', 'ios']}, 'animation_duration': {'type': 'integer', 'constraint': 'number >= 0'}}, '$description': 'translations.json#/div_tabs_tab_title_style'}, rule='type')
   data__tabtitlestyle_is_dict = isinstance(data__tabtitlestyle, dict)
   if data__tabtitlestyle_is_dict:
    data__tabtitlestyle_keys = set(data__tabtitlestyle.keys())
    if "font_size" in data__tabtitlestyle_keys:
     data__tabtitlestyle_keys.remove("font_size")
     data__tabtitlestyle__fontsize = data__tabtitlestyle["font_size"]
     validate_common_json__non_negative_integer(data__tabtitlestyle__fontsize, custom_formats, (name_prefix or "data") + ".tab_title_style.font_size")
    if "font_size_unit" in data__tabtitlestyle_keys:
     data__tabtitlestyle_keys.remove("font_size_unit")
     data__tabtitlestyle__fontsizeunit = data__tabtitlestyle["font_size_unit"]
     validate_div_size_unit_json(data__tabtitlestyle__fontsizeunit, custom_formats, (name_prefix or "data") + ".tab_title_style.font_size_unit")
    if "paddings" in data__tabtitlestyle_keys:
     data__tabtitlestyle_keys.remove("paddings")
     data__tabtitlestyle__paddings = data__tabtitlestyle["paddings"]
     validate_div_edge_insets_json(data__tabtitlestyle__paddings, custom_formats, (name_prefix or "data") + ".tab_title_style.paddings")
    if "item_spacing" in data__tabtitlestyle_keys:
     data__tabtitlestyle_keys.remove("item_spacing")
     data__tabtitlestyle__itemspacing = data__tabtitlestyle["item_spacing"]
     validate_common_json__non_negative_integer(data__tabtitlestyle__itemspacing, custom_formats, (name_prefix or "data") + ".tab_title_style.item_spacing")
    if "line_height" in data__tabtitlestyle_keys:
     data__tabtitlestyle_keys.remove("line_height")
     data__tabtitlestyle__lineheight = data__tabtitlestyle["line_height"]
     validate_common_json__non_negative_integer(data__tabtitlestyle__lineheight, custom_formats, (name_prefix or "data") + ".tab_title_style.line_height")
    if "letter_spacing" in data__tabtitlestyle_keys:
     data__tabtitlestyle_keys.remove("letter_spacing")
     data__tabtitlestyle__letterspacing = data__tabtitlestyle["letter_spacing"]
     if not isinstance(data__tabtitlestyle__letterspacing, (int, float, Decimal)) or isinstance(data__tabtitlestyle__letterspacing, bool):
      if not (isinstance(data__tabtitlestyle__letterspacing, str) and '@' in data__tabtitlestyle__letterspacing):
       raise JsonSchemaValueException("" + (name_prefix or "data") + ".tab_title_style.letter_spacing must be number", value=data__tabtitlestyle__letterspacing, name="" + (name_prefix or "data") + ".tab_title_style.letter_spacing", definition={'type': 'number', 'default_value': '0', '$description': 'translations.json#/div_tabs_tab_title_style_letter_spacing'}, rule='type')
    if "font_weight" in data__tabtitlestyle_keys:
     data__tabtitlestyle_keys.remove("font_weight")
     data__tabtitlestyle__fontweight = data__tabtitlestyle["font_weight"]
     validate_div_font_weight_json(data__tabtitlestyle__fontweight, custom_formats, (name_prefix or "data") + ".tab_title_style.font_weight")
    if "active_font_weight" in data__tabtitlestyle_keys:
     data__tabtitlestyle_keys.remove("active_font_weight")
     data__tabtitlestyle__activefontweight = data__tabtitlestyle["active_font_weight"]
     validate_div_font_weight_json(data__tabtitlestyle__activefontweight, custom_formats, (name_prefix or "data") + ".tab_title_style.active_font_weight")
    if "inactive_font_weight" in data__tabtitlestyle_keys:
     data__tabtitlestyle_keys.remove("inactive_font_weight")
     data__tabtitlestyle__inactivefontweight = data__tabtitlestyle["inactive_font_weight"]
     validate_div_font_weight_json(data__tabtitlestyle__inactivefontweight, custom_formats, (name_prefix or "data") + ".tab_title_style.inactive_font_weight")
    if "font_family" in data__tabtitlestyle_keys:
     data__tabtitlestyle_keys.remove("font_family")
     data__tabtitlestyle__fontfamily = data__tabtitlestyle["font_family"]
     validate_common_json__non_empty_string(data__tabtitlestyle__fontfamily, custom_formats, (name_prefix or "data") + ".tab_title_style.font_family")
    if "active_text_color" in data__tabtitlestyle_keys:
     data__tabtitlestyle_keys.remove("active_text_color")
     data__tabtitlestyle__activetextcolor = data__tabtitlestyle["active_text_color"]
     validate_common_json__color(data__tabtitlestyle__activetextcolor, custom_formats, (name_prefix or "data") + ".tab_title_style.active_text_color")
    if "inactive_text_color" in data__tabtitlestyle_keys:
     data__tabtitlestyle_keys.remove("inactive_text_color")
     data__tabtitlestyle__inactivetextcolor = data__tabtitlestyle["inactive_text_color"]
     validate_common_json__color(data__tabtitlestyle__inactivetextcolor, custom_formats, (name_prefix or "data") + ".tab_title_style.inactive_text_color")
    if "active_background_color" in data__tabtitlestyle_keys:
     data__tabtitlestyle_keys.remove("active_background_color")
     data__tabtitlestyle__activebackgroundcolor = data__tabtitlestyle["active_background_color"]
     validate_common_json__color(data__tabtitlestyle__activebackgroundcolor, custom_formats, (name_prefix or "data") + ".tab_title_style.active_background_color")
    if "inactive_background_color" in data__tabtitlestyle_keys:
     data__tabtitlestyle_keys.remove("inactive_background_color")
     data__tabtitlestyle__inactivebackgroundcolor = data__tabtitlestyle["inactive_background_color"]
     validate_common_json__color(data__tabtitlestyle__inactivebackgroundcolor, custom_formats, (name_prefix or "data") + ".tab_title_style.inactive_background_color")
    if "corner_radius" in data__tabtitlestyle_keys:
     data__tabtitlestyle_keys.remove("corner_radius")
     data__tabtitlestyle__cornerradius = data__tabtitlestyle["corner_radius"]
     validate_common_json__non_negative_integer(data__tabtitlestyle__cornerradius, custom_formats, (name_prefix or "data") + ".tab_title_style.corner_radius")
    if "corners_radius" in data__tabtitlestyle_keys:
     data__tabtitlestyle_keys.remove("corners_radius")
     data__tabtitlestyle__cornersradius = data__tabtitlestyle["corners_radius"]
     validate_div_corners_radius_json(data__tabtitlestyle__cornersradius, custom_formats, (name_prefix or "data") + ".tab_title_style.corners_radius")
    if "animation_type" in data__tabtitlestyle_keys:
     data__tabtitlestyle_keys.remove("animation_type")
     data__tabtitlestyle__animationtype = data__tabtitlestyle["animation_type"]
     if not isinstance(data__tabtitlestyle__animationtype, (str)):
      if not (isinstance(data__tabtitlestyle__animationtype, str) and '@' in data__tabtitlestyle__animationtype):
       raise JsonSchemaValueException("" + (name_prefix or "data") + ".tab_title_style.animation_type must be string", value=data__tabtitlestyle__animationtype, name="" + (name_prefix or "data") + ".tab_title_style.animation_type", definition={'type': 'string', 'enum': ['slide', 'fade', 'none'], 'default_value': 'slide', '$description': 'translations.json#/div_tabs_tab_title_style_animation_type', 'platforms': ['android', 'ios']}, rule='type')
     if data__tabtitlestyle__animationtype not in ['slide', 'fade', 'none']:
      if not (isinstance(data__tabtitlestyle__animationtype, str) and '@' in data__tabtitlestyle__animationtype):
       raise JsonSchemaValueException("" + (name_prefix or "data") + ".tab_title_style.animation_type must be one of ['slide', 'fade', 'none']", value=data__tabtitlestyle__animationtype, name="" + (name_prefix or "data") + ".tab_title_style.animation_type", definition={'type': 'string', 'enum': ['slide', 'fade', 'none'], 'default_value': 'slide', '$description': 'translations.json#/div_tabs_tab_title_style_animation_type', 'platforms': ['android', 'ios']}, rule='enum')
    if "animation_duration" in data__tabtitlestyle_keys:
     data__tabtitlestyle_keys.remove("animation_duration")
     data__tabtitlestyle__animationduration = data__tabtitlestyle["animation_duration"]
     validate_common_json__non_negative_integer(data__tabtitlestyle__animationduration, custom_formats, (name_prefix or "data") + ".tab_title_style.animation_duration")
  if "selected_tab" in data_keys:
   data_keys.remove("selected_tab")
   data__selectedtab = data["selected_tab"]
   validate_common_json__non_negative_integer(data__selectedtab, custom_formats, (name_prefix or "data") + ".selected_tab")
  if "has_separator" in data_keys:
   data_keys.remove("has_separator")
   data__hasseparator = data["has_separator"]
   validate_common_json__boolean_int(data__hasseparator, custom_formats, (name_prefix or "data") + ".has_separator")
  if "switch_tabs_by_content_swipe_enabled" in data_keys:
   data_keys.remove("switch_tabs_by_content_swipe_enabled")
   data__switchtabsbycontentswipeenabled = data["switch_tabs_by_content_swipe_enabled"]
   validate_common_json__boolean_int(data__switchtabsbycontentswipeenabled, custom_formats, (name_prefix or "data") + ".switch_tabs_by_content_swipe_enabled")
  if "separator_color" in data_keys:
   data_keys.remove("separator_color")
   data__separatorcolor = data["separator_color"]
   validate_common_json__color(data__separatorcolor, custom_formats, (name_prefix or "data") + ".separator_color")
  if "items" in data_keys:
   data_keys.remove("items")
   data__items = data["items"]
   if not isinstance(data__items, (list, tuple)):
    if not (isinstance(data__items, str) and '@' in data__items):
     raise JsonSchemaValueException("" + (name_prefix or "data") + ".items must be array", value=data__items, name="" + (name_prefix or "data") + ".items", definition={'type': 'array', 'items': {'type': 'object', 'codegen': {'swift': {'generate_optional_arguments': False}}, 'properties': {'title': {'$ref': 'common.json#/non_empty_string', '$description': 'translations.json#/div_tabs_item_title'}, 'title_click_action': {'$ref': 'div-action.json', '$description': 'translations.json#/div_tabs_item_title_click_action'}, 'div': {'$ref': 'div.json', '$description': 'translations.json#/div_tabs_item_div'}}, 'required': ['title', 'div'], '$description': 'translations.json#/div_tabs_item'}, 'minItems': 1, '$description': 'translations.json#/div_tabs_items'}, rule='type')
   data__items_is_list = isinstance(data__items, (list, tuple))
   if data__items_is_list:
    data__items_len = len(data__items)
    if data__items_len < 1:
     if not (isinstance(data__items, str) and '@' in data__items):
      raise JsonSchemaValueException("" + (name_prefix or "data") + ".items must contain at least 1 items", value=data__items, name="" + (name_prefix or "data") + ".items", definition={'type': 'array', 'items': {'type': 'object', 'codegen': {'swift': {'generate_optional_arguments': False}}, 'properties': {'title': {'$ref': 'common.json#/non_empty_string', '$description': 'translations.json#/div_tabs_item_title'}, 'title_click_action': {'$ref': 'div-action.json', '$description': 'translations.json#/div_tabs_item_title_click_action'}, 'div': {'$ref': 'div.json', '$description': 'translations.json#/div_tabs_item_div'}}, 'required': ['title', 'div'], '$description': 'translations.json#/div_tabs_item'}, 'minItems': 1, '$description': 'translations.json#/div_tabs_items'}, rule='minItems')
    for data__items_x, data__items_item in enumerate(data__items):
     validate_div_tabs_json__definitions_item(data__items_item, custom_formats, (name_prefix or "data") + ".items[{data__items_x}]".format(**locals()))
  if "dynamic_height" in data_keys:
   data_keys.remove("dynamic_height")
   data__dynamicheight = data["dynamic_height"]
   validate_common_json__boolean_int(data__dynamicheight, custom_formats, (name_prefix or "data") + ".dynamic_height")
  if "restrict_parent_scroll" in data_keys:
   data_keys.remove("restrict_parent_scroll")
   data__restrictparentscroll = data["restrict_parent_scroll"]
   validate_common_json__boolean_int(data__restrictparentscroll, custom_formats, (name_prefix or "data") + ".restrict_parent_scroll")
 data_is_dict = isinstance(data, dict)
 if data_is_dict:
  data__missing_keys = set(['type', 'items']) - data.keys()
  if data__missing_keys:
   if not (isinstance(data, str) and '@' in data):
    raise JsonSchemaValueException("" + (name_prefix or "data") + " must contain " + (str(sorted(data__missing_keys)) + " properties"), value=data, name="" + (name_prefix or "data") + "", definition={'java_extends': 'DivBlockWithId', '$description': 'translations.json#/div_tabs', 'codegen': {'swift': {'generate_optional_arguments': False}}, 'definitions': {'item': {'type': 'object', 'codegen': {'swift': {'generate_optional_arguments': False}}, 'properties': {'title': {'type': 'string', 'minLength': 1, 'clientMinLength': 1}, 'title_click_action': {'definitions': {'menu_item': {'type': 'object', 'properties': {'text': {'$ref': 'common.json#/non_empty_string', '$description': 'translations.json#/div_action_menu_item_text'}, 'action': {'$ref': 'div-action.json', '$description': 'translations.json#/div_action_menu_item_action'}, 'actions': {'type': 'array', 'items': {'$ref': 'div-action.json'}, 'minItems': 1, '$description': 'translations.json#/div_action_menu_item_actions'}}, 'required': ['text']}}, 'allOf': [{'$ref': 'div-action-base.json'}, {'type': 'object', '$description': 'translations.json#/div_action', 'properties': {'menu_items': {'type': 'array', 'items': {'$ref': '#/definitions/menu_item'}, '$description': 'translations.json#/div_action_menu_items', 'platforms': ['android', 'ios']}, 'log_url': {'$ref': 'common.json#/url', '$description': 'translations.json#/div_action_log_url'}, 'target': {'type': 'string', 'enum': ['_self', '_blank'], 'force_enum_field': True, '$description': 'translations.json#/div_action_target', 'platforms': ['web'], 'code_generation_disabled_swift': True}}, 'required': ['log_id']}], '$schema': 'http://json-schema.org/draft-07/schema'}, 'div': {'generate_case_for_templates_kotlinDsl': True, 'generate_case_for_templates_typescript': True, 'anyOf': [{'$ref': 'div-image.json', '$description': 'translations.json#/div_image_short'}, {'$ref': 'div-gif-image.json', '$description': 'translations.json#/div_gif_image_short'}, {'$ref': 'div-text.json', '$description': 'translations.json#/div_text_short'}, {'$ref': 'div-separator.json', '$description': 'translations.json#/div_separator_short'}, {'$ref': 'div-container.json', '$description': 'translations.json#/div_container_short'}, {'$ref': 'div-grid.json', '$description': 'translations.json#/div_grid_short'}, {'$ref': 'div-gallery.json', '$description': 'translations.json#/div_gallery_short'}, {'$ref': 'div-pager.json', '$description': 'translations.json#/div_pager_short'}, {'$ref': 'div-tabs.json', '$description': 'translations.json#/div_tabs_short'}, {'$ref': 'div-state.json', '$description': 'translations.json#/div_state_short'}, {'$ref': 'div-custom.json', '$description': 'translations.json#/div_custom_short'}, {'$ref': 'div-indicator.json', '$description': 'translations.json#/div_indicator_short'}, {'$ref': 'div-slider.json', '$description': 'translations.json#/div_slider_short'}, {'$ref': 'div-input.json', '$description': 'translations.json#/div_input_short'}, {'$ref': 'div-select.json', '$description': 'translations.json#/div_select'}, {'$ref': 'div-video.json', '$description': 'translations.json#/div_video'}], '$schema': 'http://json-schema.org/draft-07/schema'}}, 'required': ['title', 'div'], '$description': 'translations.json#/div_tabs_item'}}, 'allOf': [{'protocol_name': 'div-base', 'codegen': {'swift': {'super_protocol': 'DivBlockModeling'}, 'documentation': {'include_in_toc': True}}, 'type': 'object', 'properties': {'id': {'$ref': 'common.json#/non_empty_string', 'supports_expressions': False, '$description': 'translations.json#/div_base_id'}, 'border': {'$ref': 'div-border.json', '$description': 'translations.json#/div_base_border'}, 'width': {'$ref': 'div-size.json', 'default_value': '{"type": "match_parent"}', '$description': 'translations.json#/div_base_width'}, 'height': {'$ref': 'div-size.json', 'default_value': '{"type": "wrap_content"}', '$description': 'translations.json#/div_base_height'}, 'background': {'type': 'array', 'items': {'$ref': 'div-background.json'}, 'minItems': 1, '$description': 'translations.json#/div_base_background'}, 'paddings': {'$ref': 'div-edge-insets.json', '$description': 'translations.json#/div_base_paddings'}, 'margins': {'$ref': 'div-edge-insets.json', '$description': 'translations.json#/div_base_margins'}, 'alpha': {'type': 'number', 'default_value': '1.0', 'constraint': 'number >= 0.0 && number <= 1.0', '$description': 'translations.json#/div_base_alpha'}, 'alignment_vertical': {'$ref': 'div-alignment-vertical.json', '$description': 'translations.json#/div_base_alignment_vertical'}, 'alignment_horizontal': {'$ref': 'div-alignment-horizontal.json', '$description': 'translations.json#/div_base_alignment_horizontal'}, 'row_span': {'$ref': 'common.json#/non_negative_integer', '$description': 'translations.json#/div_base_row_span'}, 'column_span': {'$ref': 'common.json#/non_negative_integer', '$description': 'translations.json#/div_base_column_span'}, 'visibility_action': {'$ref': 'div-visibility-action.json', '$description': 'translations.json#/div_base_visibility_action'}, 'visibility_actions': {'type': 'array', 'items': {'$ref': 'div-visibility-action.json'}, 'minItems': 1, '$description': 'translations.json#/div_base_visibility_actions'}, 'disappear_actions': {'type': 'array', 'items': {'$ref': 'div-disappear-action.json'}, 'minItems': 1, '$description': 'translations.json#/div_base_disappear_actions'}, 'tooltips': {'type': 'array', 'items': {'$ref': 'div-tooltip.json'}, 'minItems': 1, '$description': 'translations.json#/div_base_tooltips'}, 'accessibility': {'$ref': 'div-accessibility.json', '$description': 'translations.json#/div_base_accessibility'}, 'extensions': {'type': 'array', 'items': {'$ref': 'div-extension.json'}, 'minItems': 1, '$description': 'translations.json#/div_base_extensions'}, 'transition_triggers': {'type': 'array', 'items': {'$ref': 'div-transition-trigger.json'}, 'minItems': 1, 'supports_expressions': False, '$description': 'translations.json#/div_base_transition_triggers'}, 'transition_in': {'$ref': 'div-appearance-transition.json', '$description': 'translations.json#/div_base_transition_in'}, 'transition_change': {'$ref': 'div-change-transition.json', '$description': 'translations.json#/div_base_transition_change'}, 'transition_out': {'$ref': 'div-appearance-transition.json', '$description': 'translations.json#/div_base_transition_out'}, 'selected_actions': {'type': 'array', 'items': {'$ref': 'div-action.json'}, 'minItems': 1, '$description': 'translations.json#/div_base_selected_actions'}, 'focus': {'$ref': 'div-focus.json', '$description': 'translations.json#/div_base_focus', 'platforms': ['android', 'ios']}, 'visibility': {'$ref': 'div-visibility.json', '$description': 'translations.json#/div_base_visibility', 'default_value': 'visible'}, 'transform': {'$ref': 'div-transform.json', '$description': 'translations.json#/div_base_transform'}}, '$schema': 'http://json-schema.org/draft-07/schema'}, {'properties': {'type': {'type': 'string', 'enum': ['tabs']}, 'title_paddings': {'type': 'object', '$description': 'translations.json#/div_edge_insets', 'properties': {'left': {'$ref': 'common.json#/non_negative_integer', 'default_value': '0', '$description': 'translations.json#/div_edge_insets_left'}, 'right': {'$ref': 'common.json#/non_negative_integer', 'default_value': '0', '$description': 'translations.json#/div_edge_insets_right'}, 'top': {'$ref': 'common.json#/non_negative_integer', 'default_value': '0', '$description': 'translations.json#/div_edge_insets_top'}, 'bottom': {'$ref': 'common.json#/non_negative_integer', 'default_value': '0', '$description': 'translations.json#/div_edge_insets_bottom'}, 'start': {'$ref': 'common.json#/non_negative_integer', '$description': 'translations.json#/div_edge_insets_start', 'platforms': []}, 'end': {'$ref': 'common.json#/non_negative_integer', '$description': 'translations.json#/div_edge_insets_end', 'platforms': []}, 'unit': {'$ref': 'div-size-unit.json', 'default_value': 'dp'}}, '$schema': 'http://json-schema.org/draft-07/schema'}, 'separator_paddings': {'type': 'object', '$description': 'translations.json#/div_edge_insets', 'properties': {'left': {'$ref': 'common.json#/non_negative_integer', 'default_value': '0', '$description': 'translations.json#/div_edge_insets_left'}, 'right': {'$ref': 'common.json#/non_negative_integer', 'default_value': '0', '$description': 'translations.json#/div_edge_insets_right'}, 'top': {'$ref': 'common.json#/non_negative_integer', 'default_value': '0', '$description': 'translations.json#/div_edge_insets_top'}, 'bottom': {'$ref': 'common.json#/non_negative_integer', 'default_value': '0', '$description': 'translations.json#/div_edge_insets_bottom'}, 'start': {'$ref': 'common.json#/non_negative_integer', '$description': 'translations.json#/div_edge_insets_start', 'platforms': []}, 'end': {'$ref': 'common.json#/non_negative_integer', '$description': 'translations.json#/div_edge_insets_end', 'platforms': []}, 'unit': {'$ref': 'div-size-unit.json', 'default_value': 'dp'}}, '$schema': 'http://json-schema.org/draft-07/schema'}, 'tab_title_style': {'type': 'object', 'properties': {'font_size': {'type': 'integer', 'constraint': 'number >= 0'}, 'font_size_unit': {'type': 'string', 'enum': ['dp', 'sp', 'px'], '$description': 'translations.json#/div_size_unit', 'platforms': ['android', 'ios'], '$schema': 'http://json-schema.org/draft-07/schema'}, 'paddings': {'type': 'object', '$description': 'translations.json#/div_edge_insets', 'properties': {'left': {'$ref': 'common.json#/non_negative_integer', 'default_value': '0', '$description': 'translations.json#/div_edge_insets_left'}, 'right': {'$ref': 'common.json#/non_negative_integer', 'default_value': '0', '$description': 'translations.json#/div_edge_insets_right'}, 'top': {'$ref': 'common.json#/non_negative_integer', 'default_value': '0', '$description': 'translations.json#/div_edge_insets_top'}, 'bottom': {'$ref': 'common.json#/non_negative_integer', 'default_value': '0', '$description': 'translations.json#/div_edge_insets_bottom'}, 'start': {'$ref': 'common.json#/non_negative_integer', '$description': 'translations.json#/div_edge_insets_start', 'platforms': []}, 'end': {'$ref': 'common.json#/non_negative_integer', '$description': 'translations.json#/div_edge_insets_end', 'platforms': []}, 'unit': {'$ref': 'div-size-unit.json', 'default_value': 'dp'}}, '$schema': 'http://json-schema.org/draft-07/schema'}, 'item_spacing': {'type': 'integer', 'constraint': 'number >= 0'}, 'line_height': {'type': 'integer', 'constraint': 'number >= 0'}, 'letter_spacing': {'type': 'number', 'default_value': '0', '$description': 'translations.json#/div_tabs_tab_title_style_letter_spacing'}, 'font_weight': {'type': 'string', 'enum': ['light', 'medium', 'regular', 'bold'], '$schema': 'http://json-schema.org/draft-07/schema'}, 'active_font_weight': {'type': 'string', 'enum': ['light', 'medium', 'regular', 'bold'], '$schema': 'http://json-schema.org/draft-07/schema'}, 'inactive_font_weight': {'type': 'string', 'enum': ['light', 'medium', 'regular', 'bold'], '$schema': 'http://json-schema.org/draft-07/schema'}, 'font_family': {'type': 'string', 'minLength': 1, 'clientMinLength': 1}, 'active_text_color': {'type': 'string', 'format': 'color'}, 'inactive_text_color': {'type': 'string', 'format': 'color'}, 'active_background_color': {'type': 'string', 'format': 'color'}, 'inactive_background_color': {'type': 'string', 'format': 'color'}, 'corner_radius': {'type': 'integer', 'constraint': 'number >= 0'}, 'corners_radius': {'type': 'object', '$description': 'translations.json#/div_corners_radius', 'properties': {'top-left': {'$ref': 'common.json#/non_negative_integer', '$description': 'translations.json#/div_corners_radius_top_left'}, 'top-right': {'$ref': 'common.json#/non_negative_integer', '$description': 'translations.json#/div_corners_radius_top_right'}, 'bottom-left': {'$ref': 'common.json#/non_negative_integer', '$description': 'translations.json#/div_corners_radius_bottom_left'}, 'bottom-right': {'$ref': 'common.json#/non_negative_integer', '$description': 'translations.json#/div_corners_radius_bottom_right'}}, '$schema': 'http://json-schema.org/draft-07/schema'}, 'animation_type': {'type': 'string', 'enum': ['slide', 'fade', 'none'], 'default_value': 'slide', '$description': 'translations.json#/div_tabs_tab_title_style_animation_type', 'platforms': ['android', 'ios']}, 'animation_duration': {'type': 'integer', 'constraint': 'number >= 0'}}, '$description': 'translations.json#/div_tabs_tab_title_style'}, 'selected_tab': {'type': 'integer', 'constraint': 'number >= 0'}, 'has_separator': {'oneOf': [{'type': 'boolean'}, {'type': 'integer', 'enum': [0, 1]}]}, 'switch_tabs_by_content_swipe_enabled': {'oneOf': [{'type': 'boolean'}, {'type': 'integer', 'enum': [0, 1]}]}, 'separator_color': {'type': 'string', 'format': 'color'}, 'items': {'type': 'array', 'items': {'type': 'object', 'codegen': {'swift': {'generate_optional_arguments': False}}, 'properties': {'title': {'$ref': 'common.json#/non_empty_string', '$description': 'translations.json#/div_tabs_item_title'}, 'title_click_action': {'$ref': 'div-action.json', '$description': 'translations.json#/div_tabs_item_title_click_action'}, 'div': {'$ref': 'div.json', '$description': 'translations.json#/div_tabs_item_div'}}, 'required': ['title', 'div'], '$description': 'translations.json#/div_tabs_item'}, 'minItems': 1, '$description': 'translations.json#/div_tabs_items'}, 'dynamic_height': {'oneOf': [{'type': 'boolean'}, {'type': 'integer', 'enum': [0, 1]}]}, 'restrict_parent_scroll': {'oneOf': [{'type': 'boolean'}, {'type': 'integer', 'enum': [0, 1]}]}}}], 'required': ['type', 'items'], '$schema': 'http://json-schema.org/draft-07/schema'}, rule='required')
 return data

def validate_div_tabs_json__definitions_item(data, custom_formats={}, name_prefix=None):
 if not isinstance(data, (dict)):
  if not (isinstance(data, str) and '@' in data):
   raise JsonSchemaValueException("" + (name_prefix or "data") + " must be object", value=data, name="" + (name_prefix or "data") + "", definition={'type': 'object', 'codegen': {'swift': {'generate_optional_arguments': False}}, 'properties': {'title': {'type': 'string', 'minLength': 1, 'clientMinLength': 1}, 'title_click_action': {'definitions': {'menu_item': {'type': 'object', 'properties': {'text': {'$ref': 'common.json#/non_empty_string', '$description': 'translations.json#/div_action_menu_item_text'}, 'action': {'$ref': 'div-action.json', '$description': 'translations.json#/div_action_menu_item_action'}, 'actions': {'type': 'array', 'items': {'$ref': 'div-action.json'}, 'minItems': 1, '$description': 'translations.json#/div_action_menu_item_actions'}}, 'required': ['text']}}, 'allOf': [{'$ref': 'div-action-base.json'}, {'type': 'object', '$description': 'translations.json#/div_action', 'properties': {'menu_items': {'type': 'array', 'items': {'$ref': '#/definitions/menu_item'}, '$description': 'translations.json#/div_action_menu_items', 'platforms': ['android', 'ios']}, 'log_url': {'$ref': 'common.json#/url', '$description': 'translations.json#/div_action_log_url'}, 'target': {'type': 'string', 'enum': ['_self', '_blank'], 'force_enum_field': True, '$description': 'translations.json#/div_action_target', 'platforms': ['web'], 'code_generation_disabled_swift': True}}, 'required': ['log_id']}], '$schema': 'http://json-schema.org/draft-07/schema'}, 'div': {'generate_case_for_templates_kotlinDsl': True, 'generate_case_for_templates_typescript': True, 'anyOf': [{'$ref': 'div-image.json', '$description': 'translations.json#/div_image_short'}, {'$ref': 'div-gif-image.json', '$description': 'translations.json#/div_gif_image_short'}, {'$ref': 'div-text.json', '$description': 'translations.json#/div_text_short'}, {'$ref': 'div-separator.json', '$description': 'translations.json#/div_separator_short'}, {'$ref': 'div-container.json', '$description': 'translations.json#/div_container_short'}, {'$ref': 'div-grid.json', '$description': 'translations.json#/div_grid_short'}, {'$ref': 'div-gallery.json', '$description': 'translations.json#/div_gallery_short'}, {'$ref': 'div-pager.json', '$description': 'translations.json#/div_pager_short'}, {'$ref': 'div-tabs.json', '$description': 'translations.json#/div_tabs_short'}, {'$ref': 'div-state.json', '$description': 'translations.json#/div_state_short'}, {'$ref': 'div-custom.json', '$description': 'translations.json#/div_custom_short'}, {'$ref': 'div-indicator.json', '$description': 'translations.json#/div_indicator_short'}, {'$ref': 'div-slider.json', '$description': 'translations.json#/div_slider_short'}, {'$ref': 'div-input.json', '$description': 'translations.json#/div_input_short'}, {'$ref': 'div-select.json', '$description': 'translations.json#/div_select'}, {'$ref': 'div-video.json', '$description': 'translations.json#/div_video'}], '$schema': 'http://json-schema.org/draft-07/schema'}}, 'required': ['title', 'div'], '$description': 'translations.json#/div_tabs_item'}, rule='type')
 data_is_dict = isinstance(data, dict)
 if data_is_dict:
  data__missing_keys = set(['title', 'div']) - data.keys()
  if data__missing_keys:
   if not (isinstance(data, str) and '@' in data):
    raise JsonSchemaValueException("" + (name_prefix or "data") + " must contain " + (str(sorted(data__missing_keys)) + " properties"), value=data, name="" + (name_prefix or "data") + "", definition={'type': 'object', 'codegen': {'swift': {'generate_optional_arguments': False}}, 'properties': {'title': {'type': 'string', 'minLength': 1, 'clientMinLength': 1}, 'title_click_action': {'definitions': {'menu_item': {'type': 'object', 'properties': {'text': {'$ref': 'common.json#/non_empty_string', '$description': 'translations.json#/div_action_menu_item_text'}, 'action': {'$ref': 'div-action.json', '$description': 'translations.json#/div_action_menu_item_action'}, 'actions': {'type': 'array', 'items': {'$ref': 'div-action.json'}, 'minItems': 1, '$description': 'translations.json#/div_action_menu_item_actions'}}, 'required': ['text']}}, 'allOf': [{'$ref': 'div-action-base.json'}, {'type': 'object', '$description': 'translations.json#/div_action', 'properties': {'menu_items': {'type': 'array', 'items': {'$ref': '#/definitions/menu_item'}, '$description': 'translations.json#/div_action_menu_items', 'platforms': ['android', 'ios']}, 'log_url': {'$ref': 'common.json#/url', '$description': 'translations.json#/div_action_log_url'}, 'target': {'type': 'string', 'enum': ['_self', '_blank'], 'force_enum_field': True, '$description': 'translations.json#/div_action_target', 'platforms': ['web'], 'code_generation_disabled_swift': True}}, 'required': ['log_id']}], '$schema': 'http://json-schema.org/draft-07/schema'}, 'div': {'generate_case_for_templates_kotlinDsl': True, 'generate_case_for_templates_typescript': True, 'anyOf': [{'$ref': 'div-image.json', '$description': 'translations.json#/div_image_short'}, {'$ref': 'div-gif-image.json', '$description': 'translations.json#/div_gif_image_short'}, {'$ref': 'div-text.json', '$description': 'translations.json#/div_text_short'}, {'$ref': 'div-separator.json', '$description': 'translations.json#/div_separator_short'}, {'$ref': 'div-container.json', '$description': 'translations.json#/div_container_short'}, {'$ref': 'div-grid.json', '$description': 'translations.json#/div_grid_short'}, {'$ref': 'div-gallery.json', '$description': 'translations.json#/div_gallery_short'}, {'$ref': 'div-pager.json', '$description': 'translations.json#/div_pager_short'}, {'$ref': 'div-tabs.json', '$description': 'translations.json#/div_tabs_short'}, {'$ref': 'div-state.json', '$description': 'translations.json#/div_state_short'}, {'$ref': 'div-custom.json', '$description': 'translations.json#/div_custom_short'}, {'$ref': 'div-indicator.json', '$description': 'translations.json#/div_indicator_short'}, {'$ref': 'div-slider.json', '$description': 'translations.json#/div_slider_short'}, {'$ref': 'div-input.json', '$description': 'translations.json#/div_input_short'}, {'$ref': 'div-select.json', '$description': 'translations.json#/div_select'}, {'$ref': 'div-video.json', '$description': 'translations.json#/div_video'}], '$schema': 'http://json-schema.org/draft-07/schema'}}, 'required': ['title', 'div'], '$description': 'translations.json#/div_tabs_item'}, rule='required')
  data_keys = set(data.keys())
  if "title" in data_keys:
   data_keys.remove("title")
   data__title = data["title"]
   validate_common_json__non_empty_string(data__title, custom_formats, (name_prefix or "data") + ".title")
  if "title_click_action" in data_keys:
   data_keys.remove("title_click_action")
   data__titleclickaction = data["title_click_action"]
   validate_div_action_json(data__titleclickaction, custom_formats, (name_prefix or "data") + ".title_click_action")
  if "div" in data_keys:
   data_keys.remove("div")
   data__div = data["div"]
   validate_div_json(data__div, custom_formats, (name_prefix or "data") + ".div")
 return data

def validate_div_pager_json(data, custom_formats={}, name_prefix=None):
 validate_div_base_json(data, custom_formats, (name_prefix or "data") + "")
 data_is_dict = isinstance(data, dict)
 if data_is_dict:
  data_keys = set(data.keys())
  if "type" in data_keys:
   data_keys.remove("type")
   data__type = data["type"]
   if not isinstance(data__type, (str)):
    if not (isinstance(data__type, str) and '@' in data__type):
     raise JsonSchemaValueException("" + (name_prefix or "data") + ".type must be string", value=data__type, name="" + (name_prefix or "data") + ".type", definition={'type': 'string', 'enum': ['pager']}, rule='type')
   if data__type not in ['pager']:
    if not (isinstance(data__type, str) and '@' in data__type):
     raise JsonSchemaValueException("" + (name_prefix or "data") + ".type must be one of ['pager']", value=data__type, name="" + (name_prefix or "data") + ".type", definition={'type': 'string', 'enum': ['pager']}, rule='enum')
  if "layout_mode" in data_keys:
   data_keys.remove("layout_mode")
   data__layoutmode = data["layout_mode"]
   validate_div_pager_layout_mode_json(data__layoutmode, custom_formats, (name_prefix or "data") + ".layout_mode")
  if "item_spacing" in data_keys:
   data_keys.remove("item_spacing")
   data__itemspacing = data["item_spacing"]
   validate_div_fixed_size_json(data__itemspacing, custom_formats, (name_prefix or "data") + ".item_spacing")
  if "items" in data_keys:
   data_keys.remove("items")
   data__items = data["items"]
   if not isinstance(data__items, (list, tuple)):
    if not (isinstance(data__items, str) and '@' in data__items):
     raise JsonSchemaValueException("" + (name_prefix or "data") + ".items must be array", value=data__items, name="" + (name_prefix or "data") + ".items", definition={'type': 'array', 'items': {'generate_case_for_templates_kotlinDsl': True, 'generate_case_for_templates_typescript': True, 'anyOf': [{'$ref': 'div-image.json', '$description': 'translations.json#/div_image_short'}, {'$ref': 'div-gif-image.json', '$description': 'translations.json#/div_gif_image_short'}, {'$ref': 'div-text.json', '$description': 'translations.json#/div_text_short'}, {'$ref': 'div-separator.json', '$description': 'translations.json#/div_separator_short'}, {'$ref': 'div-container.json', '$description': 'translations.json#/div_container_short'}, {'$ref': 'div-grid.json', '$description': 'translations.json#/div_grid_short'}, {'$ref': 'div-gallery.json', '$description': 'translations.json#/div_gallery_short'}, {'$ref': 'div-pager.json', '$description': 'translations.json#/div_pager_short'}, {'$ref': 'div-tabs.json', '$description': 'translations.json#/div_tabs_short'}, {'$ref': 'div-state.json', '$description': 'translations.json#/div_state_short'}, {'$ref': 'div-custom.json', '$description': 'translations.json#/div_custom_short'}, {'$ref': 'div-indicator.json', '$description': 'translations.json#/div_indicator_short'}, {'$ref': 'div-slider.json', '$description': 'translations.json#/div_slider_short'}, {'$ref': 'div-input.json', '$description': 'translations.json#/div_input_short'}, {'$ref': 'div-select.json', '$description': 'translations.json#/div_select'}, {'$ref': 'div-video.json', '$description': 'translations.json#/div_video'}], '$schema': 'http://json-schema.org/draft-07/schema'}, 'minItems': 1, '$description': 'translations.json#/div_pager_items'}, rule='type')
   data__items_is_list = isinstance(data__items, (list, tuple))
   if data__items_is_list:
    data__items_len = len(data__items)
    if data__items_len < 1:
     if not (isinstance(data__items, str) and '@' in data__items):
      raise JsonSchemaValueException("" + (name_prefix or "data") + ".items must contain at least 1 items", value=data__items, name="" + (name_prefix or "data") + ".items", definition={'type': 'array', 'items': {'generate_case_for_templates_kotlinDsl': True, 'generate_case_for_templates_typescript': True, 'anyOf': [{'$ref': 'div-image.json', '$description': 'translations.json#/div_image_short'}, {'$ref': 'div-gif-image.json', '$description': 'translations.json#/div_gif_image_short'}, {'$ref': 'div-text.json', '$description': 'translations.json#/div_text_short'}, {'$ref': 'div-separator.json', '$description': 'translations.json#/div_separator_short'}, {'$ref': 'div-container.json', '$description': 'translations.json#/div_container_short'}, {'$ref': 'div-grid.json', '$description': 'translations.json#/div_grid_short'}, {'$ref': 'div-gallery.json', '$description': 'translations.json#/div_gallery_short'}, {'$ref': 'div-pager.json', '$description': 'translations.json#/div_pager_short'}, {'$ref': 'div-tabs.json', '$description': 'translations.json#/div_tabs_short'}, {'$ref': 'div-state.json', '$description': 'translations.json#/div_state_short'}, {'$ref': 'div-custom.json', '$description': 'translations.json#/div_custom_short'}, {'$ref': 'div-indicator.json', '$description': 'translations.json#/div_indicator_short'}, {'$ref': 'div-slider.json', '$description': 'translations.json#/div_slider_short'}, {'$ref': 'div-input.json', '$description': 'translations.json#/div_input_short'}, {'$ref': 'div-select.json', '$description': 'translations.json#/div_select'}, {'$ref': 'div-video.json', '$description': 'translations.json#/div_video'}], '$schema': 'http://json-schema.org/draft-07/schema'}, 'minItems': 1, '$description': 'translations.json#/div_pager_items'}, rule='minItems')
    for data__items_x, data__items_item in enumerate(data__items):
     validate_div_json(data__items_item, custom_formats, (name_prefix or "data") + ".items[{data__items_x}]".format(**locals()))
  if "orientation" in data_keys:
   data_keys.remove("orientation")
   data__orientation = data["orientation"]
   if not isinstance(data__orientation, (str)):
    if not (isinstance(data__orientation, str) and '@' in data__orientation):
     raise JsonSchemaValueException("" + (name_prefix or "data") + ".orientation must be string", value=data__orientation, name="" + (name_prefix or "data") + ".orientation", definition={'type': 'string', 'default_value': 'horizontal', 'enum': ['horizontal', 'vertical'], '$description': 'translations.json#/div_pager_orientation'}, rule='type')
   if data__orientation not in ['horizontal', 'vertical']:
    if not (isinstance(data__orientation, str) and '@' in data__orientation):
     raise JsonSchemaValueException("" + (name_prefix or "data") + ".orientation must be one of ['horizontal', 'vertical']", value=data__orientation, name="" + (name_prefix or "data") + ".orientation", definition={'type': 'string', 'default_value': 'horizontal', 'enum': ['horizontal', 'vertical'], '$description': 'translations.json#/div_pager_orientation'}, rule='enum')
  if "restrict_parent_scroll" in data_keys:
   data_keys.remove("restrict_parent_scroll")
   data__restrictparentscroll = data["restrict_parent_scroll"]
   validate_common_json__boolean_int(data__restrictparentscroll, custom_formats, (name_prefix or "data") + ".restrict_parent_scroll")
  if "default_item" in data_keys:
   data_keys.remove("default_item")
   data__defaultitem = data["default_item"]
   validate_common_json__non_negative_integer(data__defaultitem, custom_formats, (name_prefix or "data") + ".default_item")
  if "infinite_scroll" in data_keys:
   data_keys.remove("infinite_scroll")
   data__infinitescroll = data["infinite_scroll"]
   validate_common_json__boolean_int(data__infinitescroll, custom_formats, (name_prefix or "data") + ".infinite_scroll")
 data_is_dict = isinstance(data, dict)
 if data_is_dict:
  data__missing_keys = set(['type', 'items', 'layout_mode']) - data.keys()
  if data__missing_keys:
   if not (isinstance(data, str) and '@' in data):
    raise JsonSchemaValueException("" + (name_prefix or "data") + " must contain " + (str(sorted(data__missing_keys)) + " properties"), value=data, name="" + (name_prefix or "data") + "", definition={'java_extends': 'DivBlockWithId', '$description': 'translations.json#/div_pager', 'codegen': {'swift': {'generate_optional_arguments': False}}, 'allOf': [{'protocol_name': 'div-base', 'codegen': {'swift': {'super_protocol': 'DivBlockModeling'}, 'documentation': {'include_in_toc': True}}, 'type': 'object', 'properties': {'id': {'$ref': 'common.json#/non_empty_string', 'supports_expressions': False, '$description': 'translations.json#/div_base_id'}, 'border': {'$ref': 'div-border.json', '$description': 'translations.json#/div_base_border'}, 'width': {'$ref': 'div-size.json', 'default_value': '{"type": "match_parent"}', '$description': 'translations.json#/div_base_width'}, 'height': {'$ref': 'div-size.json', 'default_value': '{"type": "wrap_content"}', '$description': 'translations.json#/div_base_height'}, 'background': {'type': 'array', 'items': {'$ref': 'div-background.json'}, 'minItems': 1, '$description': 'translations.json#/div_base_background'}, 'paddings': {'$ref': 'div-edge-insets.json', '$description': 'translations.json#/div_base_paddings'}, 'margins': {'$ref': 'div-edge-insets.json', '$description': 'translations.json#/div_base_margins'}, 'alpha': {'type': 'number', 'default_value': '1.0', 'constraint': 'number >= 0.0 && number <= 1.0', '$description': 'translations.json#/div_base_alpha'}, 'alignment_vertical': {'$ref': 'div-alignment-vertical.json', '$description': 'translations.json#/div_base_alignment_vertical'}, 'alignment_horizontal': {'$ref': 'div-alignment-horizontal.json', '$description': 'translations.json#/div_base_alignment_horizontal'}, 'row_span': {'$ref': 'common.json#/non_negative_integer', '$description': 'translations.json#/div_base_row_span'}, 'column_span': {'$ref': 'common.json#/non_negative_integer', '$description': 'translations.json#/div_base_column_span'}, 'visibility_action': {'$ref': 'div-visibility-action.json', '$description': 'translations.json#/div_base_visibility_action'}, 'visibility_actions': {'type': 'array', 'items': {'$ref': 'div-visibility-action.json'}, 'minItems': 1, '$description': 'translations.json#/div_base_visibility_actions'}, 'disappear_actions': {'type': 'array', 'items': {'$ref': 'div-disappear-action.json'}, 'minItems': 1, '$description': 'translations.json#/div_base_disappear_actions'}, 'tooltips': {'type': 'array', 'items': {'$ref': 'div-tooltip.json'}, 'minItems': 1, '$description': 'translations.json#/div_base_tooltips'}, 'accessibility': {'$ref': 'div-accessibility.json', '$description': 'translations.json#/div_base_accessibility'}, 'extensions': {'type': 'array', 'items': {'$ref': 'div-extension.json'}, 'minItems': 1, '$description': 'translations.json#/div_base_extensions'}, 'transition_triggers': {'type': 'array', 'items': {'$ref': 'div-transition-trigger.json'}, 'minItems': 1, 'supports_expressions': False, '$description': 'translations.json#/div_base_transition_triggers'}, 'transition_in': {'$ref': 'div-appearance-transition.json', '$description': 'translations.json#/div_base_transition_in'}, 'transition_change': {'$ref': 'div-change-transition.json', '$description': 'translations.json#/div_base_transition_change'}, 'transition_out': {'$ref': 'div-appearance-transition.json', '$description': 'translations.json#/div_base_transition_out'}, 'selected_actions': {'type': 'array', 'items': {'$ref': 'div-action.json'}, 'minItems': 1, '$description': 'translations.json#/div_base_selected_actions'}, 'focus': {'$ref': 'div-focus.json', '$description': 'translations.json#/div_base_focus', 'platforms': ['android', 'ios']}, 'visibility': {'$ref': 'div-visibility.json', '$description': 'translations.json#/div_base_visibility', 'default_value': 'visible'}, 'transform': {'$ref': 'div-transform.json', '$description': 'translations.json#/div_base_transform'}}, '$schema': 'http://json-schema.org/draft-07/schema'}, {'properties': {'type': {'type': 'string', 'enum': ['pager']}, 'layout_mode': {'anyOf': [{'$ref': 'div-page-size.json', '$description': 'translations.json#/div_pager_layout_mode_page_size'}, {'$ref': 'div-neighbour-page-size.json', '$description': 'translations.json#/div_pager_layout_mode_neighbour_page_size'}], '$schema': 'http://json-schema.org/draft-07/schema'}, 'item_spacing': {'type': 'object', '$description': 'translations.json#/div_fixed_size', 'codegen': {'divan': {'forced_properties_order': ['value']}}, 'properties': {'value': {'$ref': 'common.json#/non_negative_integer', '$description': 'translations.json#/div_fixed_size_value'}, 'unit': {'$ref': 'div-size-unit.json', '$description': 'translations.json#/div_fixed_size_unit', 'default_value': 'dp'}, 'type': {'type': 'string', 'enum': ['fixed']}}, 'required': ['value', 'type'], '$schema': 'http://json-schema.org/draft-07/schema'}, 'items': {'type': 'array', 'items': {'generate_case_for_templates_kotlinDsl': True, 'generate_case_for_templates_typescript': True, 'anyOf': [{'$ref': 'div-image.json', '$description': 'translations.json#/div_image_short'}, {'$ref': 'div-gif-image.json', '$description': 'translations.json#/div_gif_image_short'}, {'$ref': 'div-text.json', '$description': 'translations.json#/div_text_short'}, {'$ref': 'div-separator.json', '$description': 'translations.json#/div_separator_short'}, {'$ref': 'div-container.json', '$description': 'translations.json#/div_container_short'}, {'$ref': 'div-grid.json', '$description': 'translations.json#/div_grid_short'}, {'$ref': 'div-gallery.json', '$description': 'translations.json#/div_gallery_short'}, {'$ref': 'div-pager.json', '$description': 'translations.json#/div_pager_short'}, {'$ref': 'div-tabs.json', '$description': 'translations.json#/div_tabs_short'}, {'$ref': 'div-state.json', '$description': 'translations.json#/div_state_short'}, {'$ref': 'div-custom.json', '$description': 'translations.json#/div_custom_short'}, {'$ref': 'div-indicator.json', '$description': 'translations.json#/div_indicator_short'}, {'$ref': 'div-slider.json', '$description': 'translations.json#/div_slider_short'}, {'$ref': 'div-input.json', '$description': 'translations.json#/div_input_short'}, {'$ref': 'div-select.json', '$description': 'translations.json#/div_select'}, {'$ref': 'div-video.json', '$description': 'translations.json#/div_video'}], '$schema': 'http://json-schema.org/draft-07/schema'}, 'minItems': 1, '$description': 'translations.json#/div_pager_items'}, 'orientation': {'type': 'string', 'default_value': 'horizontal', 'enum': ['horizontal', 'vertical'], '$description': 'translations.json#/div_pager_orientation'}, 'restrict_parent_scroll': {'oneOf': [{'type': 'boolean'}, {'type': 'integer', 'enum': [0, 1]}]}, 'default_item': {'type': 'integer', 'constraint': 'number >= 0'}, 'infinite_scroll': {'oneOf': [{'type': 'boolean'}, {'type': 'integer', 'enum': [0, 1]}]}}}], 'required': ['type', 'items', 'layout_mode'], '$schema': 'http://json-schema.org/draft-07/schema'}, rule='required')
 return data

def validate_div_pager_layout_mode_json(data, custom_formats={}, name_prefix=None):
 data_any_of_count20 = 0
 if not data_any_of_count20:
  try:
   validate_div_page_size_json(data, custom_formats, (name_prefix or "data") + "")
   data_any_of_count20 += 1
  except JsonSchemaValueException: pass
 if not data_any_of_count20:
  try:
   validate_div_neighbour_page_size_json(data, custom_formats, (name_prefix or "data") + "")
   data_any_of_count20 += 1
  except JsonSchemaValueException: pass
 if not data_any_of_count20:
  if not (isinstance(data, str) and '@' in data):
   raise JsonSchemaValueException("" + (name_prefix or "data") + " cannot be validated by any definition", value=data, name="" + (name_prefix or "data") + "", definition={'anyOf': [{'type': 'object', '$description': 'translations.json#/div_page_size', 'properties': {'type': {'type': 'string', 'enum': ['percentage']}, 'page_width': {'$ref': 'div-percentage-size.json', '$description': 'translations.json#/div_page_size_page_width'}}, 'required': ['type', 'page_width'], '$schema': 'http://json-schema.org/draft-07/schema'}, {'type': 'object', '$description': 'translations.json#/div_neighbour_page_size', 'properties': {'type': {'type': 'string', 'enum': ['fixed']}, 'neighbour_page_width': {'$ref': 'div-fixed-size.json', '$description': 'translations.json#/div_neighbour_page_size_neighbour_page_width'}}, 'required': ['type', 'neighbour_page_width'], '$schema': 'http://json-schema.org/draft-07/schema'}], '$schema': 'http://json-schema.org/draft-07/schema'}, rule='anyOf')
 return data

def validate_div_neighbour_page_size_json(data, custom_formats={}, name_prefix=None):
 if not isinstance(data, (dict)):
  if not (isinstance(data, str) and '@' in data):
   raise JsonSchemaValueException("" + (name_prefix or "data") + " must be object", value=data, name="" + (name_prefix or "data") + "", definition={'type': 'object', '$description': 'translations.json#/div_neighbour_page_size', 'properties': {'type': {'type': 'string', 'enum': ['fixed']}, 'neighbour_page_width': {'type': 'object', '$description': 'translations.json#/div_fixed_size', 'codegen': {'divan': {'forced_properties_order': ['value']}}, 'properties': {'value': {'$ref': 'common.json#/non_negative_integer', '$description': 'translations.json#/div_fixed_size_value'}, 'unit': {'$ref': 'div-size-unit.json', '$description': 'translations.json#/div_fixed_size_unit', 'default_value': 'dp'}, 'type': {'type': 'string', 'enum': ['fixed']}}, 'required': ['value', 'type'], '$schema': 'http://json-schema.org/draft-07/schema'}}, 'required': ['type', 'neighbour_page_width'], '$schema': 'http://json-schema.org/draft-07/schema'}, rule='type')
 data_is_dict = isinstance(data, dict)
 if data_is_dict:
  data__missing_keys = set(['type', 'neighbour_page_width']) - data.keys()
  if data__missing_keys:
   if not (isinstance(data, str) and '@' in data):
    raise JsonSchemaValueException("" + (name_prefix or "data") + " must contain " + (str(sorted(data__missing_keys)) + " properties"), value=data, name="" + (name_prefix or "data") + "", definition={'type': 'object', '$description': 'translations.json#/div_neighbour_page_size', 'properties': {'type': {'type': 'string', 'enum': ['fixed']}, 'neighbour_page_width': {'type': 'object', '$description': 'translations.json#/div_fixed_size', 'codegen': {'divan': {'forced_properties_order': ['value']}}, 'properties': {'value': {'$ref': 'common.json#/non_negative_integer', '$description': 'translations.json#/div_fixed_size_value'}, 'unit': {'$ref': 'div-size-unit.json', '$description': 'translations.json#/div_fixed_size_unit', 'default_value': 'dp'}, 'type': {'type': 'string', 'enum': ['fixed']}}, 'required': ['value', 'type'], '$schema': 'http://json-schema.org/draft-07/schema'}}, 'required': ['type', 'neighbour_page_width'], '$schema': 'http://json-schema.org/draft-07/schema'}, rule='required')
  data_keys = set(data.keys())
  if "type" in data_keys:
   data_keys.remove("type")
   data__type = data["type"]
   if not isinstance(data__type, (str)):
    if not (isinstance(data__type, str) and '@' in data__type):
     raise JsonSchemaValueException("" + (name_prefix or "data") + ".type must be string", value=data__type, name="" + (name_prefix or "data") + ".type", definition={'type': 'string', 'enum': ['fixed']}, rule='type')
   if data__type not in ['fixed']:
    if not (isinstance(data__type, str) and '@' in data__type):
     raise JsonSchemaValueException("" + (name_prefix or "data") + ".type must be one of ['fixed']", value=data__type, name="" + (name_prefix or "data") + ".type", definition={'type': 'string', 'enum': ['fixed']}, rule='enum')
  if "neighbour_page_width" in data_keys:
   data_keys.remove("neighbour_page_width")
   data__neighbourpagewidth = data["neighbour_page_width"]
   validate_div_fixed_size_json(data__neighbourpagewidth, custom_formats, (name_prefix or "data") + ".neighbour_page_width")
 return data

def validate_div_page_size_json(data, custom_formats={}, name_prefix=None):
 if not isinstance(data, (dict)):
  if not (isinstance(data, str) and '@' in data):
   raise JsonSchemaValueException("" + (name_prefix or "data") + " must be object", value=data, name="" + (name_prefix or "data") + "", definition={'type': 'object', '$description': 'translations.json#/div_page_size', 'properties': {'type': {'type': 'string', 'enum': ['percentage']}, 'page_width': {'type': 'object', '$description': 'translations.json#/div_percentage_size', 'properties': {'value': {'$ref': 'common.json#/positive_number', '$description': 'translations.json#/div_percentage_size_value'}, 'type': {'type': 'string', 'enum': ['percentage']}}, 'required': ['type', 'value'], '$schema': 'http://json-schema.org/draft-07/schema'}}, 'required': ['type', 'page_width'], '$schema': 'http://json-schema.org/draft-07/schema'}, rule='type')
 data_is_dict = isinstance(data, dict)
 if data_is_dict:
  data__missing_keys = set(['type', 'page_width']) - data.keys()
  if data__missing_keys:
   if not (isinstance(data, str) and '@' in data):
    raise JsonSchemaValueException("" + (name_prefix or "data") + " must contain " + (str(sorted(data__missing_keys)) + " properties"), value=data, name="" + (name_prefix or "data") + "", definition={'type': 'object', '$description': 'translations.json#/div_page_size', 'properties': {'type': {'type': 'string', 'enum': ['percentage']}, 'page_width': {'type': 'object', '$description': 'translations.json#/div_percentage_size', 'properties': {'value': {'$ref': 'common.json#/positive_number', '$description': 'translations.json#/div_percentage_size_value'}, 'type': {'type': 'string', 'enum': ['percentage']}}, 'required': ['type', 'value'], '$schema': 'http://json-schema.org/draft-07/schema'}}, 'required': ['type', 'page_width'], '$schema': 'http://json-schema.org/draft-07/schema'}, rule='required')
  data_keys = set(data.keys())
  if "type" in data_keys:
   data_keys.remove("type")
   data__type = data["type"]
   if not isinstance(data__type, (str)):
    if not (isinstance(data__type, str) and '@' in data__type):
     raise JsonSchemaValueException("" + (name_prefix or "data") + ".type must be string", value=data__type, name="" + (name_prefix or "data") + ".type", definition={'type': 'string', 'enum': ['percentage']}, rule='type')
   if data__type not in ['percentage']:
    if not (isinstance(data__type, str) and '@' in data__type):
     raise JsonSchemaValueException("" + (name_prefix or "data") + ".type must be one of ['percentage']", value=data__type, name="" + (name_prefix or "data") + ".type", definition={'type': 'string', 'enum': ['percentage']}, rule='enum')
  if "page_width" in data_keys:
   data_keys.remove("page_width")
   data__pagewidth = data["page_width"]
   validate_div_percentage_size_json(data__pagewidth, custom_formats, (name_prefix or "data") + ".page_width")
 return data

def validate_div_percentage_size_json(data, custom_formats={}, name_prefix=None):
 if not isinstance(data, (dict)):
  if not (isinstance(data, str) and '@' in data):
   raise JsonSchemaValueException("" + (name_prefix or "data") + " must be object", value=data, name="" + (name_prefix or "data") + "", definition={'type': 'object', '$description': 'translations.json#/div_percentage_size', 'properties': {'value': {'type': 'number', 'constraint': 'number > 0'}, 'type': {'type': 'string', 'enum': ['percentage']}}, 'required': ['type', 'value'], '$schema': 'http://json-schema.org/draft-07/schema'}, rule='type')
 data_is_dict = isinstance(data, dict)
 if data_is_dict:
  data__missing_keys = set(['type', 'value']) - data.keys()
  if data__missing_keys:
   if not (isinstance(data, str) and '@' in data):
    raise JsonSchemaValueException("" + (name_prefix or "data") + " must contain " + (str(sorted(data__missing_keys)) + " properties"), value=data, name="" + (name_prefix or "data") + "", definition={'type': 'object', '$description': 'translations.json#/div_percentage_size', 'properties': {'value': {'type': 'number', 'constraint': 'number > 0'}, 'type': {'type': 'string', 'enum': ['percentage']}}, 'required': ['type', 'value'], '$schema': 'http://json-schema.org/draft-07/schema'}, rule='required')
  data_keys = set(data.keys())
  if "value" in data_keys:
   data_keys.remove("value")
   data__value = data["value"]
   validate_common_json__positive_number(data__value, custom_formats, (name_prefix or "data") + ".value")
  if "type" in data_keys:
   data_keys.remove("type")
   data__type = data["type"]
   if not isinstance(data__type, (str)):
    if not (isinstance(data__type, str) and '@' in data__type):
     raise JsonSchemaValueException("" + (name_prefix or "data") + ".type must be string", value=data__type, name="" + (name_prefix or "data") + ".type", definition={'type': 'string', 'enum': ['percentage']}, rule='type')
   if data__type not in ['percentage']:
    if not (isinstance(data__type, str) and '@' in data__type):
     raise JsonSchemaValueException("" + (name_prefix or "data") + ".type must be one of ['percentage']", value=data__type, name="" + (name_prefix or "data") + ".type", definition={'type': 'string', 'enum': ['percentage']}, rule='enum')
 return data

def validate_div_gallery_json(data, custom_formats={}, name_prefix=None):
 validate_div_base_json(data, custom_formats, (name_prefix or "data") + "")
 data_is_dict = isinstance(data, dict)
 if data_is_dict:
  data_keys = set(data.keys())
  if "type" in data_keys:
   data_keys.remove("type")
   data__type = data["type"]
   if not isinstance(data__type, (str)):
    if not (isinstance(data__type, str) and '@' in data__type):
     raise JsonSchemaValueException("" + (name_prefix or "data") + ".type must be string", value=data__type, name="" + (name_prefix or "data") + ".type", definition={'type': 'string', 'enum': ['gallery']}, rule='type')
   if data__type not in ['gallery']:
    if not (isinstance(data__type, str) and '@' in data__type):
     raise JsonSchemaValueException("" + (name_prefix or "data") + ".type must be one of ['gallery']", value=data__type, name="" + (name_prefix or "data") + ".type", definition={'type': 'string', 'enum': ['gallery']}, rule='enum')
  if "cross_content_alignment" in data_keys:
   data_keys.remove("cross_content_alignment")
   data__crosscontentalignment = data["cross_content_alignment"]
   if not isinstance(data__crosscontentalignment, (str)):
    if not (isinstance(data__crosscontentalignment, str) and '@' in data__crosscontentalignment):
     raise JsonSchemaValueException("" + (name_prefix or "data") + ".cross_content_alignment must be string", value=data__crosscontentalignment, name="" + (name_prefix or "data") + ".cross_content_alignment", definition={'$description': 'translations.json#/div_gallery_cross_content_alignment', 'version': '2.1', 'type': 'string', 'enum': ['start', 'center', 'end'], 'default_value': 'start'}, rule='type')
   if data__crosscontentalignment not in ['start', 'center', 'end']:
    if not (isinstance(data__crosscontentalignment, str) and '@' in data__crosscontentalignment):
     raise JsonSchemaValueException("" + (name_prefix or "data") + ".cross_content_alignment must be one of ['start', 'center', 'end']", value=data__crosscontentalignment, name="" + (name_prefix or "data") + ".cross_content_alignment", definition={'$description': 'translations.json#/div_gallery_cross_content_alignment', 'version': '2.1', 'type': 'string', 'enum': ['start', 'center', 'end'], 'default_value': 'start'}, rule='enum')
  if "column_count" in data_keys:
   data_keys.remove("column_count")
   data__columncount = data["column_count"]
   validate_common_json__positive_integer(data__columncount, custom_formats, (name_prefix or "data") + ".column_count")
  if "item_spacing" in data_keys:
   data_keys.remove("item_spacing")
   data__itemspacing = data["item_spacing"]
   validate_common_json__non_negative_integer(data__itemspacing, custom_formats, (name_prefix or "data") + ".item_spacing")
  if "cross_spacing" in data_keys:
   data_keys.remove("cross_spacing")
   data__crossspacing = data["cross_spacing"]
   validate_common_json__non_negative_integer(data__crossspacing, custom_formats, (name_prefix or "data") + ".cross_spacing")
  if "scroll_mode" in data_keys:
   data_keys.remove("scroll_mode")
   data__scrollmode = data["scroll_mode"]
   if not isinstance(data__scrollmode, (str)):
    if not (isinstance(data__scrollmode, str) and '@' in data__scrollmode):
     raise JsonSchemaValueException("" + (name_prefix or "data") + ".scroll_mode must be string", value=data__scrollmode, name="" + (name_prefix or "data") + ".scroll_mode", definition={'type': 'string', 'default_value': 'default', 'enum': ['paging', 'default'], '$description': 'translations.json#/div_gallery_scroll_mode'}, rule='type')
   if data__scrollmode not in ['paging', 'default']:
    if not (isinstance(data__scrollmode, str) and '@' in data__scrollmode):
     raise JsonSchemaValueException("" + (name_prefix or "data") + ".scroll_mode must be one of ['paging', 'default']", value=data__scrollmode, name="" + (name_prefix or "data") + ".scroll_mode", definition={'type': 'string', 'default_value': 'default', 'enum': ['paging', 'default'], '$description': 'translations.json#/div_gallery_scroll_mode'}, rule='enum')
  if "items" in data_keys:
   data_keys.remove("items")
   data__items = data["items"]
   if not isinstance(data__items, (list, tuple)):
    if not (isinstance(data__items, str) and '@' in data__items):
     raise JsonSchemaValueException("" + (name_prefix or "data") + ".items must be array", value=data__items, name="" + (name_prefix or "data") + ".items", definition={'type': 'array', 'items': {'generate_case_for_templates_kotlinDsl': True, 'generate_case_for_templates_typescript': True, 'anyOf': [{'$ref': 'div-image.json', '$description': 'translations.json#/div_image_short'}, {'$ref': 'div-gif-image.json', '$description': 'translations.json#/div_gif_image_short'}, {'$ref': 'div-text.json', '$description': 'translations.json#/div_text_short'}, {'$ref': 'div-separator.json', '$description': 'translations.json#/div_separator_short'}, {'$ref': 'div-container.json', '$description': 'translations.json#/div_container_short'}, {'$ref': 'div-grid.json', '$description': 'translations.json#/div_grid_short'}, {'$ref': 'div-gallery.json', '$description': 'translations.json#/div_gallery_short'}, {'$ref': 'div-pager.json', '$description': 'translations.json#/div_pager_short'}, {'$ref': 'div-tabs.json', '$description': 'translations.json#/div_tabs_short'}, {'$ref': 'div-state.json', '$description': 'translations.json#/div_state_short'}, {'$ref': 'div-custom.json', '$description': 'translations.json#/div_custom_short'}, {'$ref': 'div-indicator.json', '$description': 'translations.json#/div_indicator_short'}, {'$ref': 'div-slider.json', '$description': 'translations.json#/div_slider_short'}, {'$ref': 'div-input.json', '$description': 'translations.json#/div_input_short'}, {'$ref': 'div-select.json', '$description': 'translations.json#/div_select'}, {'$ref': 'div-video.json', '$description': 'translations.json#/div_video'}], '$schema': 'http://json-schema.org/draft-07/schema'}, 'minItems': 1, '$description': 'translations.json#/div_gallery_items'}, rule='type')
   data__items_is_list = isinstance(data__items, (list, tuple))
   if data__items_is_list:
    data__items_len = len(data__items)
    if data__items_len < 1:
     if not (isinstance(data__items, str) and '@' in data__items):
      raise JsonSchemaValueException("" + (name_prefix or "data") + ".items must contain at least 1 items", value=data__items, name="" + (name_prefix or "data") + ".items", definition={'type': 'array', 'items': {'generate_case_for_templates_kotlinDsl': True, 'generate_case_for_templates_typescript': True, 'anyOf': [{'$ref': 'div-image.json', '$description': 'translations.json#/div_image_short'}, {'$ref': 'div-gif-image.json', '$description': 'translations.json#/div_gif_image_short'}, {'$ref': 'div-text.json', '$description': 'translations.json#/div_text_short'}, {'$ref': 'div-separator.json', '$description': 'translations.json#/div_separator_short'}, {'$ref': 'div-container.json', '$description': 'translations.json#/div_container_short'}, {'$ref': 'div-grid.json', '$description': 'translations.json#/div_grid_short'}, {'$ref': 'div-gallery.json', '$description': 'translations.json#/div_gallery_short'}, {'$ref': 'div-pager.json', '$description': 'translations.json#/div_pager_short'}, {'$ref': 'div-tabs.json', '$description': 'translations.json#/div_tabs_short'}, {'$ref': 'div-state.json', '$description': 'translations.json#/div_state_short'}, {'$ref': 'div-custom.json', '$description': 'translations.json#/div_custom_short'}, {'$ref': 'div-indicator.json', '$description': 'translations.json#/div_indicator_short'}, {'$ref': 'div-slider.json', '$description': 'translations.json#/div_slider_short'}, {'$ref': 'div-input.json', '$description': 'translations.json#/div_input_short'}, {'$ref': 'div-select.json', '$description': 'translations.json#/div_select'}, {'$ref': 'div-video.json', '$description': 'translations.json#/div_video'}], '$schema': 'http://json-schema.org/draft-07/schema'}, 'minItems': 1, '$description': 'translations.json#/div_gallery_items'}, rule='minItems')
    for data__items_x, data__items_item in enumerate(data__items):
     validate_div_json(data__items_item, custom_formats, (name_prefix or "data") + ".items[{data__items_x}]".format(**locals()))
  if "orientation" in data_keys:
   data_keys.remove("orientation")
   data__orientation = data["orientation"]
   if not isinstance(data__orientation, (str)):
    if not (isinstance(data__orientation, str) and '@' in data__orientation):
     raise JsonSchemaValueException("" + (name_prefix or "data") + ".orientation must be string", value=data__orientation, name="" + (name_prefix or "data") + ".orientation", definition={'type': 'string', 'default_value': 'horizontal', 'enum': ['horizontal', 'vertical'], '$description': 'translations.json#/div_gallery_orientation'}, rule='type')
   if data__orientation not in ['horizontal', 'vertical']:
    if not (isinstance(data__orientation, str) and '@' in data__orientation):
     raise JsonSchemaValueException("" + (name_prefix or "data") + ".orientation must be one of ['horizontal', 'vertical']", value=data__orientation, name="" + (name_prefix or "data") + ".orientation", definition={'type': 'string', 'default_value': 'horizontal', 'enum': ['horizontal', 'vertical'], '$description': 'translations.json#/div_gallery_orientation'}, rule='enum')
  if "restrict_parent_scroll" in data_keys:
   data_keys.remove("restrict_parent_scroll")
   data__restrictparentscroll = data["restrict_parent_scroll"]
   validate_common_json__boolean_int(data__restrictparentscroll, custom_formats, (name_prefix or "data") + ".restrict_parent_scroll")
  if "default_item" in data_keys:
   data_keys.remove("default_item")
   data__defaultitem = data["default_item"]
   validate_common_json__non_negative_integer(data__defaultitem, custom_formats, (name_prefix or "data") + ".default_item")
 data_is_dict = isinstance(data, dict)
 if data_is_dict:
  data__missing_keys = set(['type', 'items']) - data.keys()
  if data__missing_keys:
   if not (isinstance(data, str) and '@' in data):
    raise JsonSchemaValueException("" + (name_prefix or "data") + " must contain " + (str(sorted(data__missing_keys)) + " properties"), value=data, name="" + (name_prefix or "data") + "", definition={'java_extends': 'DivBlockWithId', '$description': 'translations.json#/div_gallery', 'codegen': {'swift': {'generate_optional_arguments': False}}, 'allOf': [{'protocol_name': 'div-base', 'codegen': {'swift': {'super_protocol': 'DivBlockModeling'}, 'documentation': {'include_in_toc': True}}, 'type': 'object', 'properties': {'id': {'$ref': 'common.json#/non_empty_string', 'supports_expressions': False, '$description': 'translations.json#/div_base_id'}, 'border': {'$ref': 'div-border.json', '$description': 'translations.json#/div_base_border'}, 'width': {'$ref': 'div-size.json', 'default_value': '{"type": "match_parent"}', '$description': 'translations.json#/div_base_width'}, 'height': {'$ref': 'div-size.json', 'default_value': '{"type": "wrap_content"}', '$description': 'translations.json#/div_base_height'}, 'background': {'type': 'array', 'items': {'$ref': 'div-background.json'}, 'minItems': 1, '$description': 'translations.json#/div_base_background'}, 'paddings': {'$ref': 'div-edge-insets.json', '$description': 'translations.json#/div_base_paddings'}, 'margins': {'$ref': 'div-edge-insets.json', '$description': 'translations.json#/div_base_margins'}, 'alpha': {'type': 'number', 'default_value': '1.0', 'constraint': 'number >= 0.0 && number <= 1.0', '$description': 'translations.json#/div_base_alpha'}, 'alignment_vertical': {'$ref': 'div-alignment-vertical.json', '$description': 'translations.json#/div_base_alignment_vertical'}, 'alignment_horizontal': {'$ref': 'div-alignment-horizontal.json', '$description': 'translations.json#/div_base_alignment_horizontal'}, 'row_span': {'$ref': 'common.json#/non_negative_integer', '$description': 'translations.json#/div_base_row_span'}, 'column_span': {'$ref': 'common.json#/non_negative_integer', '$description': 'translations.json#/div_base_column_span'}, 'visibility_action': {'$ref': 'div-visibility-action.json', '$description': 'translations.json#/div_base_visibility_action'}, 'visibility_actions': {'type': 'array', 'items': {'$ref': 'div-visibility-action.json'}, 'minItems': 1, '$description': 'translations.json#/div_base_visibility_actions'}, 'disappear_actions': {'type': 'array', 'items': {'$ref': 'div-disappear-action.json'}, 'minItems': 1, '$description': 'translations.json#/div_base_disappear_actions'}, 'tooltips': {'type': 'array', 'items': {'$ref': 'div-tooltip.json'}, 'minItems': 1, '$description': 'translations.json#/div_base_tooltips'}, 'accessibility': {'$ref': 'div-accessibility.json', '$description': 'translations.json#/div_base_accessibility'}, 'extensions': {'type': 'array', 'items': {'$ref': 'div-extension.json'}, 'minItems': 1, '$description': 'translations.json#/div_base_extensions'}, 'transition_triggers': {'type': 'array', 'items': {'$ref': 'div-transition-trigger.json'}, 'minItems': 1, 'supports_expressions': False, '$description': 'translations.json#/div_base_transition_triggers'}, 'transition_in': {'$ref': 'div-appearance-transition.json', '$description': 'translations.json#/div_base_transition_in'}, 'transition_change': {'$ref': 'div-change-transition.json', '$description': 'translations.json#/div_base_transition_change'}, 'transition_out': {'$ref': 'div-appearance-transition.json', '$description': 'translations.json#/div_base_transition_out'}, 'selected_actions': {'type': 'array', 'items': {'$ref': 'div-action.json'}, 'minItems': 1, '$description': 'translations.json#/div_base_selected_actions'}, 'focus': {'$ref': 'div-focus.json', '$description': 'translations.json#/div_base_focus', 'platforms': ['android', 'ios']}, 'visibility': {'$ref': 'div-visibility.json', '$description': 'translations.json#/div_base_visibility', 'default_value': 'visible'}, 'transform': {'$ref': 'div-transform.json', '$description': 'translations.json#/div_base_transform'}}, '$schema': 'http://json-schema.org/draft-07/schema'}, {'properties': {'type': {'type': 'string', 'enum': ['gallery']}, 'cross_content_alignment': {'$description': 'translations.json#/div_gallery_cross_content_alignment', 'version': '2.1', 'type': 'string', 'enum': ['start', 'center', 'end'], 'default_value': 'start'}, 'column_count': {'type': 'integer', 'constraint': 'number > 0'}, 'item_spacing': {'type': 'integer', 'constraint': 'number >= 0'}, 'cross_spacing': {'type': 'integer', 'constraint': 'number >= 0'}, 'scroll_mode': {'type': 'string', 'default_value': 'default', 'enum': ['paging', 'default'], '$description': 'translations.json#/div_gallery_scroll_mode'}, 'items': {'type': 'array', 'items': {'generate_case_for_templates_kotlinDsl': True, 'generate_case_for_templates_typescript': True, 'anyOf': [{'$ref': 'div-image.json', '$description': 'translations.json#/div_image_short'}, {'$ref': 'div-gif-image.json', '$description': 'translations.json#/div_gif_image_short'}, {'$ref': 'div-text.json', '$description': 'translations.json#/div_text_short'}, {'$ref': 'div-separator.json', '$description': 'translations.json#/div_separator_short'}, {'$ref': 'div-container.json', '$description': 'translations.json#/div_container_short'}, {'$ref': 'div-grid.json', '$description': 'translations.json#/div_grid_short'}, {'$ref': 'div-gallery.json', '$description': 'translations.json#/div_gallery_short'}, {'$ref': 'div-pager.json', '$description': 'translations.json#/div_pager_short'}, {'$ref': 'div-tabs.json', '$description': 'translations.json#/div_tabs_short'}, {'$ref': 'div-state.json', '$description': 'translations.json#/div_state_short'}, {'$ref': 'div-custom.json', '$description': 'translations.json#/div_custom_short'}, {'$ref': 'div-indicator.json', '$description': 'translations.json#/div_indicator_short'}, {'$ref': 'div-slider.json', '$description': 'translations.json#/div_slider_short'}, {'$ref': 'div-input.json', '$description': 'translations.json#/div_input_short'}, {'$ref': 'div-select.json', '$description': 'translations.json#/div_select'}, {'$ref': 'div-video.json', '$description': 'translations.json#/div_video'}], '$schema': 'http://json-schema.org/draft-07/schema'}, 'minItems': 1, '$description': 'translations.json#/div_gallery_items'}, 'orientation': {'type': 'string', 'default_value': 'horizontal', 'enum': ['horizontal', 'vertical'], '$description': 'translations.json#/div_gallery_orientation'}, 'restrict_parent_scroll': {'oneOf': [{'type': 'boolean'}, {'type': 'integer', 'enum': [0, 1]}]}, 'default_item': {'type': 'integer', 'constraint': 'number >= 0'}}}], 'required': ['type', 'items'], '$schema': 'http://json-schema.org/draft-07/schema'}, rule='required')
 return data

def validate_div_grid_json(data, custom_formats={}, name_prefix=None):
 validate_div_base_json(data, custom_formats, (name_prefix or "data") + "")
 validate_div_actionable_json(data, custom_formats, (name_prefix or "data") + "")
 data_is_dict = isinstance(data, dict)
 if data_is_dict:
  data_keys = set(data.keys())
  if "content_alignment_vertical" in data_keys:
   data_keys.remove("content_alignment_vertical")
   data__contentalignmentvertical = data["content_alignment_vertical"]
   validate_div_alignment_vertical_json(data__contentalignmentvertical, custom_formats, (name_prefix or "data") + ".content_alignment_vertical")
  if "content_alignment_horizontal" in data_keys:
   data_keys.remove("content_alignment_horizontal")
   data__contentalignmenthorizontal = data["content_alignment_horizontal"]
   validate_div_alignment_horizontal_json(data__contentalignmenthorizontal, custom_formats, (name_prefix or "data") + ".content_alignment_horizontal")
  if "items" in data_keys:
   data_keys.remove("items")
   data__items = data["items"]
   if not isinstance(data__items, (list, tuple)):
    if not (isinstance(data__items, str) and '@' in data__items):
     raise JsonSchemaValueException("" + (name_prefix or "data") + ".items must be array", value=data__items, name="" + (name_prefix or "data") + ".items", definition={'type': 'array', 'items': {'generate_case_for_templates_kotlinDsl': True, 'generate_case_for_templates_typescript': True, 'anyOf': [{'$ref': 'div-image.json', '$description': 'translations.json#/div_image_short'}, {'$ref': 'div-gif-image.json', '$description': 'translations.json#/div_gif_image_short'}, {'$ref': 'div-text.json', '$description': 'translations.json#/div_text_short'}, {'$ref': 'div-separator.json', '$description': 'translations.json#/div_separator_short'}, {'$ref': 'div-container.json', '$description': 'translations.json#/div_container_short'}, {'$ref': 'div-grid.json', '$description': 'translations.json#/div_grid_short'}, {'$ref': 'div-gallery.json', '$description': 'translations.json#/div_gallery_short'}, {'$ref': 'div-pager.json', '$description': 'translations.json#/div_pager_short'}, {'$ref': 'div-tabs.json', '$description': 'translations.json#/div_tabs_short'}, {'$ref': 'div-state.json', '$description': 'translations.json#/div_state_short'}, {'$ref': 'div-custom.json', '$description': 'translations.json#/div_custom_short'}, {'$ref': 'div-indicator.json', '$description': 'translations.json#/div_indicator_short'}, {'$ref': 'div-slider.json', '$description': 'translations.json#/div_slider_short'}, {'$ref': 'div-input.json', '$description': 'translations.json#/div_input_short'}, {'$ref': 'div-select.json', '$description': 'translations.json#/div_select'}, {'$ref': 'div-video.json', '$description': 'translations.json#/div_video'}], '$schema': 'http://json-schema.org/draft-07/schema'}, 'minItems': 1, 'strictParsing': True, '$description': 'translations.json#/div_grid_items'}, rule='type')
   data__items_is_list = isinstance(data__items, (list, tuple))
   if data__items_is_list:
    data__items_len = len(data__items)
    if data__items_len < 1:
     if not (isinstance(data__items, str) and '@' in data__items):
      raise JsonSchemaValueException("" + (name_prefix or "data") + ".items must contain at least 1 items", value=data__items, name="" + (name_prefix or "data") + ".items", definition={'type': 'array', 'items': {'generate_case_for_templates_kotlinDsl': True, 'generate_case_for_templates_typescript': True, 'anyOf': [{'$ref': 'div-image.json', '$description': 'translations.json#/div_image_short'}, {'$ref': 'div-gif-image.json', '$description': 'translations.json#/div_gif_image_short'}, {'$ref': 'div-text.json', '$description': 'translations.json#/div_text_short'}, {'$ref': 'div-separator.json', '$description': 'translations.json#/div_separator_short'}, {'$ref': 'div-container.json', '$description': 'translations.json#/div_container_short'}, {'$ref': 'div-grid.json', '$description': 'translations.json#/div_grid_short'}, {'$ref': 'div-gallery.json', '$description': 'translations.json#/div_gallery_short'}, {'$ref': 'div-pager.json', '$description': 'translations.json#/div_pager_short'}, {'$ref': 'div-tabs.json', '$description': 'translations.json#/div_tabs_short'}, {'$ref': 'div-state.json', '$description': 'translations.json#/div_state_short'}, {'$ref': 'div-custom.json', '$description': 'translations.json#/div_custom_short'}, {'$ref': 'div-indicator.json', '$description': 'translations.json#/div_indicator_short'}, {'$ref': 'div-slider.json', '$description': 'translations.json#/div_slider_short'}, {'$ref': 'div-input.json', '$description': 'translations.json#/div_input_short'}, {'$ref': 'div-select.json', '$description': 'translations.json#/div_select'}, {'$ref': 'div-video.json', '$description': 'translations.json#/div_video'}], '$schema': 'http://json-schema.org/draft-07/schema'}, 'minItems': 1, 'strictParsing': True, '$description': 'translations.json#/div_grid_items'}, rule='minItems')
    for data__items_x, data__items_item in enumerate(data__items):
     validate_div_json(data__items_item, custom_formats, (name_prefix or "data") + ".items[{data__items_x}]".format(**locals()))
  if "column_count" in data_keys:
   data_keys.remove("column_count")
   data__columncount = data["column_count"]
   validate_common_json__non_negative_integer(data__columncount, custom_formats, (name_prefix or "data") + ".column_count")
  if "type" in data_keys:
   data_keys.remove("type")
   data__type = data["type"]
   if not isinstance(data__type, (str)):
    if not (isinstance(data__type, str) and '@' in data__type):
     raise JsonSchemaValueException("" + (name_prefix or "data") + ".type must be string", value=data__type, name="" + (name_prefix or "data") + ".type", definition={'type': 'string', 'enum': ['grid']}, rule='type')
   if data__type not in ['grid']:
    if not (isinstance(data__type, str) and '@' in data__type):
     raise JsonSchemaValueException("" + (name_prefix or "data") + ".type must be one of ['grid']", value=data__type, name="" + (name_prefix or "data") + ".type", definition={'type': 'string', 'enum': ['grid']}, rule='enum')
 data_is_dict = isinstance(data, dict)
 if data_is_dict:
  data__missing_keys = set(['items', 'column_count', 'type']) - data.keys()
  if data__missing_keys:
   if not (isinstance(data, str) and '@' in data):
    raise JsonSchemaValueException("" + (name_prefix or "data") + " must contain " + (str(sorted(data__missing_keys)) + " properties"), value=data, name="" + (name_prefix or "data") + "", definition={'java_extends': 'DivBlockWithId', '$description': 'translations.json#/div_grid', 'codegen': {'swift': {'generate_optional_arguments': False}}, 'allOf': [{'protocol_name': 'div-base', 'codegen': {'swift': {'super_protocol': 'DivBlockModeling'}, 'documentation': {'include_in_toc': True}}, 'type': 'object', 'properties': {'id': {'$ref': 'common.json#/non_empty_string', 'supports_expressions': False, '$description': 'translations.json#/div_base_id'}, 'border': {'$ref': 'div-border.json', '$description': 'translations.json#/div_base_border'}, 'width': {'$ref': 'div-size.json', 'default_value': '{"type": "match_parent"}', '$description': 'translations.json#/div_base_width'}, 'height': {'$ref': 'div-size.json', 'default_value': '{"type": "wrap_content"}', '$description': 'translations.json#/div_base_height'}, 'background': {'type': 'array', 'items': {'$ref': 'div-background.json'}, 'minItems': 1, '$description': 'translations.json#/div_base_background'}, 'paddings': {'$ref': 'div-edge-insets.json', '$description': 'translations.json#/div_base_paddings'}, 'margins': {'$ref': 'div-edge-insets.json', '$description': 'translations.json#/div_base_margins'}, 'alpha': {'type': 'number', 'default_value': '1.0', 'constraint': 'number >= 0.0 && number <= 1.0', '$description': 'translations.json#/div_base_alpha'}, 'alignment_vertical': {'$ref': 'div-alignment-vertical.json', '$description': 'translations.json#/div_base_alignment_vertical'}, 'alignment_horizontal': {'$ref': 'div-alignment-horizontal.json', '$description': 'translations.json#/div_base_alignment_horizontal'}, 'row_span': {'$ref': 'common.json#/non_negative_integer', '$description': 'translations.json#/div_base_row_span'}, 'column_span': {'$ref': 'common.json#/non_negative_integer', '$description': 'translations.json#/div_base_column_span'}, 'visibility_action': {'$ref': 'div-visibility-action.json', '$description': 'translations.json#/div_base_visibility_action'}, 'visibility_actions': {'type': 'array', 'items': {'$ref': 'div-visibility-action.json'}, 'minItems': 1, '$description': 'translations.json#/div_base_visibility_actions'}, 'disappear_actions': {'type': 'array', 'items': {'$ref': 'div-disappear-action.json'}, 'minItems': 1, '$description': 'translations.json#/div_base_disappear_actions'}, 'tooltips': {'type': 'array', 'items': {'$ref': 'div-tooltip.json'}, 'minItems': 1, '$description': 'translations.json#/div_base_tooltips'}, 'accessibility': {'$ref': 'div-accessibility.json', '$description': 'translations.json#/div_base_accessibility'}, 'extensions': {'type': 'array', 'items': {'$ref': 'div-extension.json'}, 'minItems': 1, '$description': 'translations.json#/div_base_extensions'}, 'transition_triggers': {'type': 'array', 'items': {'$ref': 'div-transition-trigger.json'}, 'minItems': 1, 'supports_expressions': False, '$description': 'translations.json#/div_base_transition_triggers'}, 'transition_in': {'$ref': 'div-appearance-transition.json', '$description': 'translations.json#/div_base_transition_in'}, 'transition_change': {'$ref': 'div-change-transition.json', '$description': 'translations.json#/div_base_transition_change'}, 'transition_out': {'$ref': 'div-appearance-transition.json', '$description': 'translations.json#/div_base_transition_out'}, 'selected_actions': {'type': 'array', 'items': {'$ref': 'div-action.json'}, 'minItems': 1, '$description': 'translations.json#/div_base_selected_actions'}, 'focus': {'$ref': 'div-focus.json', '$description': 'translations.json#/div_base_focus', 'platforms': ['android', 'ios']}, 'visibility': {'$ref': 'div-visibility.json', '$description': 'translations.json#/div_base_visibility', 'default_value': 'visible'}, 'transform': {'$ref': 'div-transform.json', '$description': 'translations.json#/div_base_transform'}}, '$schema': 'http://json-schema.org/draft-07/schema'}, {'properties': {'action': {'$ref': 'div-action.json', '$description': 'translations.json#/div_actionable_action'}, 'actions': {'type': 'array', 'items': {'$ref': 'div-action.json'}, 'minItems': 1, '$description': 'translations.json#/div_actionable_actions'}, 'longtap_actions': {'type': 'array', 'items': {'$ref': 'div-action.json'}, 'minItems': 1, '$description': 'translations.json#/div_actionable_longtap_actions'}, 'doubletap_actions': {'type': 'array', 'items': {'$ref': 'div-action.json'}, 'minItems': 1, '$description': 'translations.json#/div_actionable_doubletap_actions'}, 'action_animation': {'$ref': 'div-animation.json', 'default_value': '{"name": "fade", "start_value": 1, "end_value": 0.6, "duration": 100 }', '$description': 'translations.json#/div_actionable_action_animation'}}, '$schema': 'http://json-schema.org/draft-07/schema'}, {'properties': {'content_alignment_vertical': {'type': 'string', 'enum': ['top', 'center', 'bottom', 'baseline'], '$schema': 'http://json-schema.org/draft-07/schema'}, 'content_alignment_horizontal': {'type': 'string', 'enum': ['left', 'center', 'right', 'start', 'end'], '$schema': 'http://json-schema.org/draft-07/schema'}, 'items': {'type': 'array', 'items': {'generate_case_for_templates_kotlinDsl': True, 'generate_case_for_templates_typescript': True, 'anyOf': [{'$ref': 'div-image.json', '$description': 'translations.json#/div_image_short'}, {'$ref': 'div-gif-image.json', '$description': 'translations.json#/div_gif_image_short'}, {'$ref': 'div-text.json', '$description': 'translations.json#/div_text_short'}, {'$ref': 'div-separator.json', '$description': 'translations.json#/div_separator_short'}, {'$ref': 'div-container.json', '$description': 'translations.json#/div_container_short'}, {'$ref': 'div-grid.json', '$description': 'translations.json#/div_grid_short'}, {'$ref': 'div-gallery.json', '$description': 'translations.json#/div_gallery_short'}, {'$ref': 'div-pager.json', '$description': 'translations.json#/div_pager_short'}, {'$ref': 'div-tabs.json', '$description': 'translations.json#/div_tabs_short'}, {'$ref': 'div-state.json', '$description': 'translations.json#/div_state_short'}, {'$ref': 'div-custom.json', '$description': 'translations.json#/div_custom_short'}, {'$ref': 'div-indicator.json', '$description': 'translations.json#/div_indicator_short'}, {'$ref': 'div-slider.json', '$description': 'translations.json#/div_slider_short'}, {'$ref': 'div-input.json', '$description': 'translations.json#/div_input_short'}, {'$ref': 'div-select.json', '$description': 'translations.json#/div_select'}, {'$ref': 'div-video.json', '$description': 'translations.json#/div_video'}], '$schema': 'http://json-schema.org/draft-07/schema'}, 'minItems': 1, 'strictParsing': True, '$description': 'translations.json#/div_grid_items'}, 'column_count': {'type': 'integer', 'constraint': 'number >= 0'}, 'type': {'type': 'string', 'enum': ['grid']}}}], 'required': ['items', 'column_count', 'type'], '$schema': 'http://json-schema.org/draft-07/schema'}, rule='required')
 return data

def validate_div_actionable_json(data, custom_formats={}, name_prefix=None):
 data_is_dict = isinstance(data, dict)
 if data_is_dict:
  data_keys = set(data.keys())
  if "action" in data_keys:
   data_keys.remove("action")
   data__action = data["action"]
   validate_div_action_json(data__action, custom_formats, (name_prefix or "data") + ".action")
  if "actions" in data_keys:
   data_keys.remove("actions")
   data__actions = data["actions"]
   if not isinstance(data__actions, (list, tuple)):
    if not (isinstance(data__actions, str) and '@' in data__actions):
     raise JsonSchemaValueException("" + (name_prefix or "data") + ".actions must be array", value=data__actions, name="" + (name_prefix or "data") + ".actions", definition={'type': 'array', 'items': {'definitions': {'menu_item': {'type': 'object', 'properties': {'text': {'$ref': 'common.json#/non_empty_string', '$description': 'translations.json#/div_action_menu_item_text'}, 'action': {'$ref': 'div-action.json', '$description': 'translations.json#/div_action_menu_item_action'}, 'actions': {'type': 'array', 'items': {'$ref': 'div-action.json'}, 'minItems': 1, '$description': 'translations.json#/div_action_menu_item_actions'}}, 'required': ['text']}}, 'allOf': [{'$ref': 'div-action-base.json'}, {'type': 'object', '$description': 'translations.json#/div_action', 'properties': {'menu_items': {'type': 'array', 'items': {'$ref': '#/definitions/menu_item'}, '$description': 'translations.json#/div_action_menu_items', 'platforms': ['android', 'ios']}, 'log_url': {'$ref': 'common.json#/url', '$description': 'translations.json#/div_action_log_url'}, 'target': {'type': 'string', 'enum': ['_self', '_blank'], 'force_enum_field': True, '$description': 'translations.json#/div_action_target', 'platforms': ['web'], 'code_generation_disabled_swift': True}}, 'required': ['log_id']}], '$schema': 'http://json-schema.org/draft-07/schema'}, 'minItems': 1, '$description': 'translations.json#/div_actionable_actions'}, rule='type')
   data__actions_is_list = isinstance(data__actions, (list, tuple))
   if data__actions_is_list:
    data__actions_len = len(data__actions)
    if data__actions_len < 1:
     if not (isinstance(data__actions, str) and '@' in data__actions):
      raise JsonSchemaValueException("" + (name_prefix or "data") + ".actions must contain at least 1 items", value=data__actions, name="" + (name_prefix or "data") + ".actions", definition={'type': 'array', 'items': {'definitions': {'menu_item': {'type': 'object', 'properties': {'text': {'$ref': 'common.json#/non_empty_string', '$description': 'translations.json#/div_action_menu_item_text'}, 'action': {'$ref': 'div-action.json', '$description': 'translations.json#/div_action_menu_item_action'}, 'actions': {'type': 'array', 'items': {'$ref': 'div-action.json'}, 'minItems': 1, '$description': 'translations.json#/div_action_menu_item_actions'}}, 'required': ['text']}}, 'allOf': [{'$ref': 'div-action-base.json'}, {'type': 'object', '$description': 'translations.json#/div_action', 'properties': {'menu_items': {'type': 'array', 'items': {'$ref': '#/definitions/menu_item'}, '$description': 'translations.json#/div_action_menu_items', 'platforms': ['android', 'ios']}, 'log_url': {'$ref': 'common.json#/url', '$description': 'translations.json#/div_action_log_url'}, 'target': {'type': 'string', 'enum': ['_self', '_blank'], 'force_enum_field': True, '$description': 'translations.json#/div_action_target', 'platforms': ['web'], 'code_generation_disabled_swift': True}}, 'required': ['log_id']}], '$schema': 'http://json-schema.org/draft-07/schema'}, 'minItems': 1, '$description': 'translations.json#/div_actionable_actions'}, rule='minItems')
    for data__actions_x, data__actions_item in enumerate(data__actions):
     validate_div_action_json(data__actions_item, custom_formats, (name_prefix or "data") + ".actions[{data__actions_x}]".format(**locals()))
  if "longtap_actions" in data_keys:
   data_keys.remove("longtap_actions")
   data__longtapactions = data["longtap_actions"]
   if not isinstance(data__longtapactions, (list, tuple)):
    if not (isinstance(data__longtapactions, str) and '@' in data__longtapactions):
     raise JsonSchemaValueException("" + (name_prefix or "data") + ".longtap_actions must be array", value=data__longtapactions, name="" + (name_prefix or "data") + ".longtap_actions", definition={'type': 'array', 'items': {'definitions': {'menu_item': {'type': 'object', 'properties': {'text': {'$ref': 'common.json#/non_empty_string', '$description': 'translations.json#/div_action_menu_item_text'}, 'action': {'$ref': 'div-action.json', '$description': 'translations.json#/div_action_menu_item_action'}, 'actions': {'type': 'array', 'items': {'$ref': 'div-action.json'}, 'minItems': 1, '$description': 'translations.json#/div_action_menu_item_actions'}}, 'required': ['text']}}, 'allOf': [{'$ref': 'div-action-base.json'}, {'type': 'object', '$description': 'translations.json#/div_action', 'properties': {'menu_items': {'type': 'array', 'items': {'$ref': '#/definitions/menu_item'}, '$description': 'translations.json#/div_action_menu_items', 'platforms': ['android', 'ios']}, 'log_url': {'$ref': 'common.json#/url', '$description': 'translations.json#/div_action_log_url'}, 'target': {'type': 'string', 'enum': ['_self', '_blank'], 'force_enum_field': True, '$description': 'translations.json#/div_action_target', 'platforms': ['web'], 'code_generation_disabled_swift': True}}, 'required': ['log_id']}], '$schema': 'http://json-schema.org/draft-07/schema'}, 'minItems': 1, '$description': 'translations.json#/div_actionable_longtap_actions'}, rule='type')
   data__longtapactions_is_list = isinstance(data__longtapactions, (list, tuple))
   if data__longtapactions_is_list:
    data__longtapactions_len = len(data__longtapactions)
    if data__longtapactions_len < 1:
     if not (isinstance(data__longtapactions, str) and '@' in data__longtapactions):
      raise JsonSchemaValueException("" + (name_prefix or "data") + ".longtap_actions must contain at least 1 items", value=data__longtapactions, name="" + (name_prefix or "data") + ".longtap_actions", definition={'type': 'array', 'items': {'definitions': {'menu_item': {'type': 'object', 'properties': {'text': {'$ref': 'common.json#/non_empty_string', '$description': 'translations.json#/div_action_menu_item_text'}, 'action': {'$ref': 'div-action.json', '$description': 'translations.json#/div_action_menu_item_action'}, 'actions': {'type': 'array', 'items': {'$ref': 'div-action.json'}, 'minItems': 1, '$description': 'translations.json#/div_action_menu_item_actions'}}, 'required': ['text']}}, 'allOf': [{'$ref': 'div-action-base.json'}, {'type': 'object', '$description': 'translations.json#/div_action', 'properties': {'menu_items': {'type': 'array', 'items': {'$ref': '#/definitions/menu_item'}, '$description': 'translations.json#/div_action_menu_items', 'platforms': ['android', 'ios']}, 'log_url': {'$ref': 'common.json#/url', '$description': 'translations.json#/div_action_log_url'}, 'target': {'type': 'string', 'enum': ['_self', '_blank'], 'force_enum_field': True, '$description': 'translations.json#/div_action_target', 'platforms': ['web'], 'code_generation_disabled_swift': True}}, 'required': ['log_id']}], '$schema': 'http://json-schema.org/draft-07/schema'}, 'minItems': 1, '$description': 'translations.json#/div_actionable_longtap_actions'}, rule='minItems')
    for data__longtapactions_x, data__longtapactions_item in enumerate(data__longtapactions):
     validate_div_action_json(data__longtapactions_item, custom_formats, (name_prefix or "data") + ".longtap_actions[{data__longtapactions_x}]".format(**locals()))
  if "doubletap_actions" in data_keys:
   data_keys.remove("doubletap_actions")
   data__doubletapactions = data["doubletap_actions"]
   if not isinstance(data__doubletapactions, (list, tuple)):
    if not (isinstance(data__doubletapactions, str) and '@' in data__doubletapactions):
     raise JsonSchemaValueException("" + (name_prefix or "data") + ".doubletap_actions must be array", value=data__doubletapactions, name="" + (name_prefix or "data") + ".doubletap_actions", definition={'type': 'array', 'items': {'definitions': {'menu_item': {'type': 'object', 'properties': {'text': {'$ref': 'common.json#/non_empty_string', '$description': 'translations.json#/div_action_menu_item_text'}, 'action': {'$ref': 'div-action.json', '$description': 'translations.json#/div_action_menu_item_action'}, 'actions': {'type': 'array', 'items': {'$ref': 'div-action.json'}, 'minItems': 1, '$description': 'translations.json#/div_action_menu_item_actions'}}, 'required': ['text']}}, 'allOf': [{'$ref': 'div-action-base.json'}, {'type': 'object', '$description': 'translations.json#/div_action', 'properties': {'menu_items': {'type': 'array', 'items': {'$ref': '#/definitions/menu_item'}, '$description': 'translations.json#/div_action_menu_items', 'platforms': ['android', 'ios']}, 'log_url': {'$ref': 'common.json#/url', '$description': 'translations.json#/div_action_log_url'}, 'target': {'type': 'string', 'enum': ['_self', '_blank'], 'force_enum_field': True, '$description': 'translations.json#/div_action_target', 'platforms': ['web'], 'code_generation_disabled_swift': True}}, 'required': ['log_id']}], '$schema': 'http://json-schema.org/draft-07/schema'}, 'minItems': 1, '$description': 'translations.json#/div_actionable_doubletap_actions'}, rule='type')
   data__doubletapactions_is_list = isinstance(data__doubletapactions, (list, tuple))
   if data__doubletapactions_is_list:
    data__doubletapactions_len = len(data__doubletapactions)
    if data__doubletapactions_len < 1:
     if not (isinstance(data__doubletapactions, str) and '@' in data__doubletapactions):
      raise JsonSchemaValueException("" + (name_prefix or "data") + ".doubletap_actions must contain at least 1 items", value=data__doubletapactions, name="" + (name_prefix or "data") + ".doubletap_actions", definition={'type': 'array', 'items': {'definitions': {'menu_item': {'type': 'object', 'properties': {'text': {'$ref': 'common.json#/non_empty_string', '$description': 'translations.json#/div_action_menu_item_text'}, 'action': {'$ref': 'div-action.json', '$description': 'translations.json#/div_action_menu_item_action'}, 'actions': {'type': 'array', 'items': {'$ref': 'div-action.json'}, 'minItems': 1, '$description': 'translations.json#/div_action_menu_item_actions'}}, 'required': ['text']}}, 'allOf': [{'$ref': 'div-action-base.json'}, {'type': 'object', '$description': 'translations.json#/div_action', 'properties': {'menu_items': {'type': 'array', 'items': {'$ref': '#/definitions/menu_item'}, '$description': 'translations.json#/div_action_menu_items', 'platforms': ['android', 'ios']}, 'log_url': {'$ref': 'common.json#/url', '$description': 'translations.json#/div_action_log_url'}, 'target': {'type': 'string', 'enum': ['_self', '_blank'], 'force_enum_field': True, '$description': 'translations.json#/div_action_target', 'platforms': ['web'], 'code_generation_disabled_swift': True}}, 'required': ['log_id']}], '$schema': 'http://json-schema.org/draft-07/schema'}, 'minItems': 1, '$description': 'translations.json#/div_actionable_doubletap_actions'}, rule='minItems')
    for data__doubletapactions_x, data__doubletapactions_item in enumerate(data__doubletapactions):
     validate_div_action_json(data__doubletapactions_item, custom_formats, (name_prefix or "data") + ".doubletap_actions[{data__doubletapactions_x}]".format(**locals()))
  if "action_animation" in data_keys:
   data_keys.remove("action_animation")
   data__actionanimation = data["action_animation"]
   validate_div_animation_json(data__actionanimation, custom_formats, (name_prefix or "data") + ".action_animation")
 return data

def validate_div_container_json(data, custom_formats={}, name_prefix=None):
 validate_div_base_json(data, custom_formats, (name_prefix or "data") + "")
 validate_div_actionable_json(data, custom_formats, (name_prefix or "data") + "")
 data_is_dict = isinstance(data, dict)
 if data_is_dict:
  data_keys = set(data.keys())
  if "type" in data_keys:
   data_keys.remove("type")
   data__type = data["type"]
   if not isinstance(data__type, (str)):
    if not (isinstance(data__type, str) and '@' in data__type):
     raise JsonSchemaValueException("" + (name_prefix or "data") + ".type must be string", value=data__type, name="" + (name_prefix or "data") + ".type", definition={'type': 'string', 'enum': ['container']}, rule='type')
   if data__type not in ['container']:
    if not (isinstance(data__type, str) and '@' in data__type):
     raise JsonSchemaValueException("" + (name_prefix or "data") + ".type must be one of ['container']", value=data__type, name="" + (name_prefix or "data") + ".type", definition={'type': 'string', 'enum': ['container']}, rule='enum')
  if "content_alignment_vertical" in data_keys:
   data_keys.remove("content_alignment_vertical")
   data__contentalignmentvertical = data["content_alignment_vertical"]
   validate_div_content_alignment_vertical_json(data__contentalignmentvertical, custom_formats, (name_prefix or "data") + ".content_alignment_vertical")
  if "content_alignment_horizontal" in data_keys:
   data_keys.remove("content_alignment_horizontal")
   data__contentalignmenthorizontal = data["content_alignment_horizontal"]
   validate_div_content_alignment_horizontal_json(data__contentalignmenthorizontal, custom_formats, (name_prefix or "data") + ".content_alignment_horizontal")
  if "orientation" in data_keys:
   data_keys.remove("orientation")
   data__orientation = data["orientation"]
   if not isinstance(data__orientation, (str)):
    if not (isinstance(data__orientation, str) and '@' in data__orientation):
     raise JsonSchemaValueException("" + (name_prefix or "data") + ".orientation must be string", value=data__orientation, name="" + (name_prefix or "data") + ".orientation", definition={'type': 'string', 'enum': ['vertical', 'horizontal', 'overlap'], 'default_value': 'vertical', '$description': 'translations.json#/div_container_orientation'}, rule='type')
   if data__orientation not in ['vertical', 'horizontal', 'overlap']:
    if not (isinstance(data__orientation, str) and '@' in data__orientation):
     raise JsonSchemaValueException("" + (name_prefix or "data") + ".orientation must be one of ['vertical', 'horizontal', 'overlap']", value=data__orientation, name="" + (name_prefix or "data") + ".orientation", definition={'type': 'string', 'enum': ['vertical', 'horizontal', 'overlap'], 'default_value': 'vertical', '$description': 'translations.json#/div_container_orientation'}, rule='enum')
  if "layout_mode" in data_keys:
   data_keys.remove("layout_mode")
   data__layoutmode = data["layout_mode"]
   if not isinstance(data__layoutmode, (str)):
    if not (isinstance(data__layoutmode, str) and '@' in data__layoutmode):
     raise JsonSchemaValueException("" + (name_prefix or "data") + ".layout_mode must be string", value=data__layoutmode, name="" + (name_prefix or "data") + ".layout_mode", definition={'type': 'string', 'enum': ['no_wrap', 'wrap'], 'default_value': 'no_wrap', '$description': 'translations.json#/div_container_layout_mode'}, rule='type')
   if data__layoutmode not in ['no_wrap', 'wrap']:
    if not (isinstance(data__layoutmode, str) and '@' in data__layoutmode):
     raise JsonSchemaValueException("" + (name_prefix or "data") + ".layout_mode must be one of ['no_wrap', 'wrap']", value=data__layoutmode, name="" + (name_prefix or "data") + ".layout_mode", definition={'type': 'string', 'enum': ['no_wrap', 'wrap'], 'default_value': 'no_wrap', '$description': 'translations.json#/div_container_layout_mode'}, rule='enum')
  if "separator" in data_keys:
   data_keys.remove("separator")
   data__separator = data["separator"]
   validate_div_container_json__definitions_separator(data__separator, custom_formats, (name_prefix or "data") + ".separator")
  if "line_separator" in data_keys:
   data_keys.remove("line_separator")
   data__lineseparator = data["line_separator"]
   validate_div_container_json__definitions_separator(data__lineseparator, custom_formats, (name_prefix or "data") + ".line_separator")
  if "items" in data_keys:
   data_keys.remove("items")
   data__items = data["items"]
   if not isinstance(data__items, (list, tuple)):
    if not (isinstance(data__items, str) and '@' in data__items):
     raise JsonSchemaValueException("" + (name_prefix or "data") + ".items must be array", value=data__items, name="" + (name_prefix or "data") + ".items", definition={'type': 'array', 'items': {'generate_case_for_templates_kotlinDsl': True, 'generate_case_for_templates_typescript': True, 'anyOf': [{'$ref': 'div-image.json', '$description': 'translations.json#/div_image_short'}, {'$ref': 'div-gif-image.json', '$description': 'translations.json#/div_gif_image_short'}, {'$ref': 'div-text.json', '$description': 'translations.json#/div_text_short'}, {'$ref': 'div-separator.json', '$description': 'translations.json#/div_separator_short'}, {'$ref': 'div-container.json', '$description': 'translations.json#/div_container_short'}, {'$ref': 'div-grid.json', '$description': 'translations.json#/div_grid_short'}, {'$ref': 'div-gallery.json', '$description': 'translations.json#/div_gallery_short'}, {'$ref': 'div-pager.json', '$description': 'translations.json#/div_pager_short'}, {'$ref': 'div-tabs.json', '$description': 'translations.json#/div_tabs_short'}, {'$ref': 'div-state.json', '$description': 'translations.json#/div_state_short'}, {'$ref': 'div-custom.json', '$description': 'translations.json#/div_custom_short'}, {'$ref': 'div-indicator.json', '$description': 'translations.json#/div_indicator_short'}, {'$ref': 'div-slider.json', '$description': 'translations.json#/div_slider_short'}, {'$ref': 'div-input.json', '$description': 'translations.json#/div_input_short'}, {'$ref': 'div-select.json', '$description': 'translations.json#/div_select'}, {'$ref': 'div-video.json', '$description': 'translations.json#/div_video'}], '$schema': 'http://json-schema.org/draft-07/schema'}, 'minItems': 1, '$description': 'translations.json#/div_container_items'}, rule='type')
   data__items_is_list = isinstance(data__items, (list, tuple))
   if data__items_is_list:
    data__items_len = len(data__items)
    if data__items_len < 1:
     if not (isinstance(data__items, str) and '@' in data__items):
      raise JsonSchemaValueException("" + (name_prefix or "data") + ".items must contain at least 1 items", value=data__items, name="" + (name_prefix or "data") + ".items", definition={'type': 'array', 'items': {'generate_case_for_templates_kotlinDsl': True, 'generate_case_for_templates_typescript': True, 'anyOf': [{'$ref': 'div-image.json', '$description': 'translations.json#/div_image_short'}, {'$ref': 'div-gif-image.json', '$description': 'translations.json#/div_gif_image_short'}, {'$ref': 'div-text.json', '$description': 'translations.json#/div_text_short'}, {'$ref': 'div-separator.json', '$description': 'translations.json#/div_separator_short'}, {'$ref': 'div-container.json', '$description': 'translations.json#/div_container_short'}, {'$ref': 'div-grid.json', '$description': 'translations.json#/div_grid_short'}, {'$ref': 'div-gallery.json', '$description': 'translations.json#/div_gallery_short'}, {'$ref': 'div-pager.json', '$description': 'translations.json#/div_pager_short'}, {'$ref': 'div-tabs.json', '$description': 'translations.json#/div_tabs_short'}, {'$ref': 'div-state.json', '$description': 'translations.json#/div_state_short'}, {'$ref': 'div-custom.json', '$description': 'translations.json#/div_custom_short'}, {'$ref': 'div-indicator.json', '$description': 'translations.json#/div_indicator_short'}, {'$ref': 'div-slider.json', '$description': 'translations.json#/div_slider_short'}, {'$ref': 'div-input.json', '$description': 'translations.json#/div_input_short'}, {'$ref': 'div-select.json', '$description': 'translations.json#/div_select'}, {'$ref': 'div-video.json', '$description': 'translations.json#/div_video'}], '$schema': 'http://json-schema.org/draft-07/schema'}, 'minItems': 1, '$description': 'translations.json#/div_container_items'}, rule='minItems')
    for data__items_x, data__items_item in enumerate(data__items):
     validate_div_json(data__items_item, custom_formats, (name_prefix or "data") + ".items[{data__items_x}]".format(**locals()))
  if "aspect" in data_keys:
   data_keys.remove("aspect")
   data__aspect = data["aspect"]
   validate_div_aspect_json(data__aspect, custom_formats, (name_prefix or "data") + ".aspect")
 data_is_dict = isinstance(data, dict)
 if data_is_dict:
  data__missing_keys = set(['type', 'items']) - data.keys()
  if data__missing_keys:
   if not (isinstance(data, str) and '@' in data):
    raise JsonSchemaValueException("" + (name_prefix or "data") + " must contain " + (str(sorted(data__missing_keys)) + " properties"), value=data, name="" + (name_prefix or "data") + "", definition={'java_extends': 'DivBlockWithId', '$description': 'translations.json#/div_container', 'codegen': {'divan': {'forced_properties_order': ['orientation'], 'factories': {'row': {'vararg_property': 'items', 'inlines': {'orientation': 'horizontal'}}, 'column': {'vararg_property': 'items', 'inlines': {'orientation': 'vertical'}}, 'stack': {'vararg_property': 'items', 'inlines': {'orientation': 'overlap'}}}}, 'swift': {'generate_optional_arguments': False}}, 'definitions': {'separator': {'type': 'object', 'properties': {'show_at_start': {'oneOf': [{'type': 'boolean'}, {'type': 'integer', 'enum': [0, 1]}]}, 'show_between': {'oneOf': [{'type': 'boolean'}, {'type': 'integer', 'enum': [0, 1]}]}, 'show_at_end': {'oneOf': [{'type': 'boolean'}, {'type': 'integer', 'enum': [0, 1]}]}, 'style': {'anyOf': [{'$ref': 'div-shape-drawable.json', '$description': 'translations.json#/div_shape_drawable'}], '$schema': 'http://json-schema.org/draft-07/schema'}, 'margins': {'type': 'object', '$description': 'translations.json#/div_edge_insets', 'properties': {'left': {'$ref': 'common.json#/non_negative_integer', 'default_value': '0', '$description': 'translations.json#/div_edge_insets_left'}, 'right': {'$ref': 'common.json#/non_negative_integer', 'default_value': '0', '$description': 'translations.json#/div_edge_insets_right'}, 'top': {'$ref': 'common.json#/non_negative_integer', 'default_value': '0', '$description': 'translations.json#/div_edge_insets_top'}, 'bottom': {'$ref': 'common.json#/non_negative_integer', 'default_value': '0', '$description': 'translations.json#/div_edge_insets_bottom'}, 'start': {'$ref': 'common.json#/non_negative_integer', '$description': 'translations.json#/div_edge_insets_start', 'platforms': []}, 'end': {'$ref': 'common.json#/non_negative_integer', '$description': 'translations.json#/div_edge_insets_end', 'platforms': []}, 'unit': {'$ref': 'div-size-unit.json', 'default_value': 'dp'}}, '$schema': 'http://json-schema.org/draft-07/schema'}}, 'required': ['style']}}, 'allOf': [{'protocol_name': 'div-base', 'codegen': {'swift': {'super_protocol': 'DivBlockModeling'}, 'documentation': {'include_in_toc': True}}, 'type': 'object', 'properties': {'id': {'$ref': 'common.json#/non_empty_string', 'supports_expressions': False, '$description': 'translations.json#/div_base_id'}, 'border': {'$ref': 'div-border.json', '$description': 'translations.json#/div_base_border'}, 'width': {'$ref': 'div-size.json', 'default_value': '{"type": "match_parent"}', '$description': 'translations.json#/div_base_width'}, 'height': {'$ref': 'div-size.json', 'default_value': '{"type": "wrap_content"}', '$description': 'translations.json#/div_base_height'}, 'background': {'type': 'array', 'items': {'$ref': 'div-background.json'}, 'minItems': 1, '$description': 'translations.json#/div_base_background'}, 'paddings': {'$ref': 'div-edge-insets.json', '$description': 'translations.json#/div_base_paddings'}, 'margins': {'$ref': 'div-edge-insets.json', '$description': 'translations.json#/div_base_margins'}, 'alpha': {'type': 'number', 'default_value': '1.0', 'constraint': 'number >= 0.0 && number <= 1.0', '$description': 'translations.json#/div_base_alpha'}, 'alignment_vertical': {'$ref': 'div-alignment-vertical.json', '$description': 'translations.json#/div_base_alignment_vertical'}, 'alignment_horizontal': {'$ref': 'div-alignment-horizontal.json', '$description': 'translations.json#/div_base_alignment_horizontal'}, 'row_span': {'$ref': 'common.json#/non_negative_integer', '$description': 'translations.json#/div_base_row_span'}, 'column_span': {'$ref': 'common.json#/non_negative_integer', '$description': 'translations.json#/div_base_column_span'}, 'visibility_action': {'$ref': 'div-visibility-action.json', '$description': 'translations.json#/div_base_visibility_action'}, 'visibility_actions': {'type': 'array', 'items': {'$ref': 'div-visibility-action.json'}, 'minItems': 1, '$description': 'translations.json#/div_base_visibility_actions'}, 'disappear_actions': {'type': 'array', 'items': {'$ref': 'div-disappear-action.json'}, 'minItems': 1, '$description': 'translations.json#/div_base_disappear_actions'}, 'tooltips': {'type': 'array', 'items': {'$ref': 'div-tooltip.json'}, 'minItems': 1, '$description': 'translations.json#/div_base_tooltips'}, 'accessibility': {'$ref': 'div-accessibility.json', '$description': 'translations.json#/div_base_accessibility'}, 'extensions': {'type': 'array', 'items': {'$ref': 'div-extension.json'}, 'minItems': 1, '$description': 'translations.json#/div_base_extensions'}, 'transition_triggers': {'type': 'array', 'items': {'$ref': 'div-transition-trigger.json'}, 'minItems': 1, 'supports_expressions': False, '$description': 'translations.json#/div_base_transition_triggers'}, 'transition_in': {'$ref': 'div-appearance-transition.json', '$description': 'translations.json#/div_base_transition_in'}, 'transition_change': {'$ref': 'div-change-transition.json', '$description': 'translations.json#/div_base_transition_change'}, 'transition_out': {'$ref': 'div-appearance-transition.json', '$description': 'translations.json#/div_base_transition_out'}, 'selected_actions': {'type': 'array', 'items': {'$ref': 'div-action.json'}, 'minItems': 1, '$description': 'translations.json#/div_base_selected_actions'}, 'focus': {'$ref': 'div-focus.json', '$description': 'translations.json#/div_base_focus', 'platforms': ['android', 'ios']}, 'visibility': {'$ref': 'div-visibility.json', '$description': 'translations.json#/div_base_visibility', 'default_value': 'visible'}, 'transform': {'$ref': 'div-transform.json', '$description': 'translations.json#/div_base_transform'}}, '$schema': 'http://json-schema.org/draft-07/schema'}, {'properties': {'action': {'$ref': 'div-action.json', '$description': 'translations.json#/div_actionable_action'}, 'actions': {'type': 'array', 'items': {'$ref': 'div-action.json'}, 'minItems': 1, '$description': 'translations.json#/div_actionable_actions'}, 'longtap_actions': {'type': 'array', 'items': {'$ref': 'div-action.json'}, 'minItems': 1, '$description': 'translations.json#/div_actionable_longtap_actions'}, 'doubletap_actions': {'type': 'array', 'items': {'$ref': 'div-action.json'}, 'minItems': 1, '$description': 'translations.json#/div_actionable_doubletap_actions'}, 'action_animation': {'$ref': 'div-animation.json', 'default_value': '{"name": "fade", "start_value": 1, "end_value": 0.6, "duration": 100 }', '$description': 'translations.json#/div_actionable_action_animation'}}, '$schema': 'http://json-schema.org/draft-07/schema'}, {'properties': {'type': {'type': 'string', 'enum': ['container']}, 'content_alignment_vertical': {'type': 'string', 'enum': ['top', 'center', 'bottom', 'baseline', 'space-between', 'space-around', 'space-evenly'], '$schema': 'http://json-schema.org/draft-07/schema'}, 'content_alignment_horizontal': {'type': 'string', 'enum': ['left', 'center', 'right', 'start', 'end', 'space-between', 'space-around', 'space-evenly'], '$schema': 'http://json-schema.org/draft-07/schema'}, 'orientation': {'type': 'string', 'enum': ['vertical', 'horizontal', 'overlap'], 'default_value': 'vertical', '$description': 'translations.json#/div_container_orientation'}, 'layout_mode': {'type': 'string', 'enum': ['no_wrap', 'wrap'], 'default_value': 'no_wrap', '$description': 'translations.json#/div_container_layout_mode'}, 'separator': {'type': 'object', 'properties': {'show_at_start': {'$ref': 'common.json#/boolean_int', '$description': 'translations.json#/div_container_separator_show_at_start', 'default_value': 'false'}, 'show_between': {'$ref': 'common.json#/boolean_int', '$description': 'translations.json#/div_container_separator_show_between', 'default_value': 'true'}, 'show_at_end': {'$ref': 'common.json#/boolean_int', '$description': 'translations.json#/div_container_separator_show_at_end', 'default_value': 'false'}, 'style': {'$ref': 'div-drawable.json', '$description': 'translations.json#/div_container_separator_style'}, 'margins': {'$ref': 'div-edge-insets.json', '$description': 'translations.json#/div_base_margins'}}, 'required': ['style']}, 'line_separator': {'type': 'object', 'properties': {'show_at_start': {'$ref': 'common.json#/boolean_int', '$description': 'translations.json#/div_container_separator_show_at_start', 'default_value': 'false'}, 'show_between': {'$ref': 'common.json#/boolean_int', '$description': 'translations.json#/div_container_separator_show_between', 'default_value': 'true'}, 'show_at_end': {'$ref': 'common.json#/boolean_int', '$description': 'translations.json#/div_container_separator_show_at_end', 'default_value': 'false'}, 'style': {'$ref': 'div-drawable.json', '$description': 'translations.json#/div_container_separator_style'}, 'margins': {'$ref': 'div-edge-insets.json', '$description': 'translations.json#/div_base_margins'}}, 'required': ['style']}, 'items': {'type': 'array', 'items': {'generate_case_for_templates_kotlinDsl': True, 'generate_case_for_templates_typescript': True, 'anyOf': [{'$ref': 'div-image.json', '$description': 'translations.json#/div_image_short'}, {'$ref': 'div-gif-image.json', '$description': 'translations.json#/div_gif_image_short'}, {'$ref': 'div-text.json', '$description': 'translations.json#/div_text_short'}, {'$ref': 'div-separator.json', '$description': 'translations.json#/div_separator_short'}, {'$ref': 'div-container.json', '$description': 'translations.json#/div_container_short'}, {'$ref': 'div-grid.json', '$description': 'translations.json#/div_grid_short'}, {'$ref': 'div-gallery.json', '$description': 'translations.json#/div_gallery_short'}, {'$ref': 'div-pager.json', '$description': 'translations.json#/div_pager_short'}, {'$ref': 'div-tabs.json', '$description': 'translations.json#/div_tabs_short'}, {'$ref': 'div-state.json', '$description': 'translations.json#/div_state_short'}, {'$ref': 'div-custom.json', '$description': 'translations.json#/div_custom_short'}, {'$ref': 'div-indicator.json', '$description': 'translations.json#/div_indicator_short'}, {'$ref': 'div-slider.json', '$description': 'translations.json#/div_slider_short'}, {'$ref': 'div-input.json', '$description': 'translations.json#/div_input_short'}, {'$ref': 'div-select.json', '$description': 'translations.json#/div_select'}, {'$ref': 'div-video.json', '$description': 'translations.json#/div_video'}], '$schema': 'http://json-schema.org/draft-07/schema'}, 'minItems': 1, '$description': 'translations.json#/div_container_items'}, 'aspect': {'type': 'object', '$description': 'translations.json#/div_aspect', 'properties': {'ratio': {'$ref': 'common.json#/positive_number', '$description': 'translations.json#/div_aspect_ratio'}}, 'required': ['ratio'], '$schema': 'http://json-schema.org/draft-07/schema'}}}], 'required': ['type', 'items'], '$schema': 'http://json-schema.org/draft-07/schema'}, rule='required')
 return data

def validate_div_container_json__definitions_separator(data, custom_formats={}, name_prefix=None):
 if not isinstance(data, (dict)):
  if not (isinstance(data, str) and '@' in data):
   raise JsonSchemaValueException("" + (name_prefix or "data") + " must be object", value=data, name="" + (name_prefix or "data") + "", definition={'type': 'object', 'properties': {'show_at_start': {'oneOf': [{'type': 'boolean'}, {'type': 'integer', 'enum': [0, 1]}]}, 'show_between': {'oneOf': [{'type': 'boolean'}, {'type': 'integer', 'enum': [0, 1]}]}, 'show_at_end': {'oneOf': [{'type': 'boolean'}, {'type': 'integer', 'enum': [0, 1]}]}, 'style': {'anyOf': [{'$ref': 'div-shape-drawable.json', '$description': 'translations.json#/div_shape_drawable'}], '$schema': 'http://json-schema.org/draft-07/schema'}, 'margins': {'type': 'object', '$description': 'translations.json#/div_edge_insets', 'properties': {'left': {'$ref': 'common.json#/non_negative_integer', 'default_value': '0', '$description': 'translations.json#/div_edge_insets_left'}, 'right': {'$ref': 'common.json#/non_negative_integer', 'default_value': '0', '$description': 'translations.json#/div_edge_insets_right'}, 'top': {'$ref': 'common.json#/non_negative_integer', 'default_value': '0', '$description': 'translations.json#/div_edge_insets_top'}, 'bottom': {'$ref': 'common.json#/non_negative_integer', 'default_value': '0', '$description': 'translations.json#/div_edge_insets_bottom'}, 'start': {'$ref': 'common.json#/non_negative_integer', '$description': 'translations.json#/div_edge_insets_start', 'platforms': []}, 'end': {'$ref': 'common.json#/non_negative_integer', '$description': 'translations.json#/div_edge_insets_end', 'platforms': []}, 'unit': {'$ref': 'div-size-unit.json', 'default_value': 'dp'}}, '$schema': 'http://json-schema.org/draft-07/schema'}}, 'required': ['style']}, rule='type')
 data_is_dict = isinstance(data, dict)
 if data_is_dict:
  data__missing_keys = set(['style']) - data.keys()
  if data__missing_keys:
   if not (isinstance(data, str) and '@' in data):
    raise JsonSchemaValueException("" + (name_prefix or "data") + " must contain " + (str(sorted(data__missing_keys)) + " properties"), value=data, name="" + (name_prefix or "data") + "", definition={'type': 'object', 'properties': {'show_at_start': {'oneOf': [{'type': 'boolean'}, {'type': 'integer', 'enum': [0, 1]}]}, 'show_between': {'oneOf': [{'type': 'boolean'}, {'type': 'integer', 'enum': [0, 1]}]}, 'show_at_end': {'oneOf': [{'type': 'boolean'}, {'type': 'integer', 'enum': [0, 1]}]}, 'style': {'anyOf': [{'$ref': 'div-shape-drawable.json', '$description': 'translations.json#/div_shape_drawable'}], '$schema': 'http://json-schema.org/draft-07/schema'}, 'margins': {'type': 'object', '$description': 'translations.json#/div_edge_insets', 'properties': {'left': {'$ref': 'common.json#/non_negative_integer', 'default_value': '0', '$description': 'translations.json#/div_edge_insets_left'}, 'right': {'$ref': 'common.json#/non_negative_integer', 'default_value': '0', '$description': 'translations.json#/div_edge_insets_right'}, 'top': {'$ref': 'common.json#/non_negative_integer', 'default_value': '0', '$description': 'translations.json#/div_edge_insets_top'}, 'bottom': {'$ref': 'common.json#/non_negative_integer', 'default_value': '0', '$description': 'translations.json#/div_edge_insets_bottom'}, 'start': {'$ref': 'common.json#/non_negative_integer', '$description': 'translations.json#/div_edge_insets_start', 'platforms': []}, 'end': {'$ref': 'common.json#/non_negative_integer', '$description': 'translations.json#/div_edge_insets_end', 'platforms': []}, 'unit': {'$ref': 'div-size-unit.json', 'default_value': 'dp'}}, '$schema': 'http://json-schema.org/draft-07/schema'}}, 'required': ['style']}, rule='required')
  data_keys = set(data.keys())
  if "show_at_start" in data_keys:
   data_keys.remove("show_at_start")
   data__showatstart = data["show_at_start"]
   validate_common_json__boolean_int(data__showatstart, custom_formats, (name_prefix or "data") + ".show_at_start")
  if "show_between" in data_keys:
   data_keys.remove("show_between")
   data__showbetween = data["show_between"]
   validate_common_json__boolean_int(data__showbetween, custom_formats, (name_prefix or "data") + ".show_between")
  if "show_at_end" in data_keys:
   data_keys.remove("show_at_end")
   data__showatend = data["show_at_end"]
   validate_common_json__boolean_int(data__showatend, custom_formats, (name_prefix or "data") + ".show_at_end")
  if "style" in data_keys:
   data_keys.remove("style")
   data__style = data["style"]
   validate_div_drawable_json(data__style, custom_formats, (name_prefix or "data") + ".style")
  if "margins" in data_keys:
   data_keys.remove("margins")
   data__margins = data["margins"]
   validate_div_edge_insets_json(data__margins, custom_formats, (name_prefix or "data") + ".margins")
 return data

def validate_div_content_alignment_horizontal_json(data, custom_formats={}, name_prefix=None):
 if not isinstance(data, (str)):
  if not (isinstance(data, str) and '@' in data):
   raise JsonSchemaValueException("" + (name_prefix or "data") + " must be string", value=data, name="" + (name_prefix or "data") + "", definition={'type': 'string', 'enum': ['left', 'center', 'right', 'start', 'end', 'space-between', 'space-around', 'space-evenly'], '$schema': 'http://json-schema.org/draft-07/schema'}, rule='type')
 if data not in ['left', 'center', 'right', 'start', 'end', 'space-between', 'space-around', 'space-evenly']:
  if not (isinstance(data, str) and '@' in data):
   raise JsonSchemaValueException("" + (name_prefix or "data") + " must be one of ['left', 'center', 'right', 'start', 'end', 'space-between', 'space-around', 'space-evenly']", value=data, name="" + (name_prefix or "data") + "", definition={'type': 'string', 'enum': ['left', 'center', 'right', 'start', 'end', 'space-between', 'space-around', 'space-evenly'], '$schema': 'http://json-schema.org/draft-07/schema'}, rule='enum')
 return data

def validate_div_content_alignment_vertical_json(data, custom_formats={}, name_prefix=None):
 if not isinstance(data, (str)):
  if not (isinstance(data, str) and '@' in data):
   raise JsonSchemaValueException("" + (name_prefix or "data") + " must be string", value=data, name="" + (name_prefix or "data") + "", definition={'type': 'string', 'enum': ['top', 'center', 'bottom', 'baseline', 'space-between', 'space-around', 'space-evenly'], '$schema': 'http://json-schema.org/draft-07/schema'}, rule='type')
 if data not in ['top', 'center', 'bottom', 'baseline', 'space-between', 'space-around', 'space-evenly']:
  if not (isinstance(data, str) and '@' in data):
   raise JsonSchemaValueException("" + (name_prefix or "data") + " must be one of ['top', 'center', 'bottom', 'baseline', 'space-between', 'space-around', 'space-evenly']", value=data, name="" + (name_prefix or "data") + "", definition={'type': 'string', 'enum': ['top', 'center', 'bottom', 'baseline', 'space-between', 'space-around', 'space-evenly'], '$schema': 'http://json-schema.org/draft-07/schema'}, rule='enum')
 return data

def validate_div_separator_json(data, custom_formats={}, name_prefix=None):
 validate_div_base_json(data, custom_formats, (name_prefix or "data") + "")
 validate_div_actionable_json(data, custom_formats, (name_prefix or "data") + "")
 data_is_dict = isinstance(data, dict)
 if data_is_dict:
  data__missing_keys = set(['type']) - data.keys()
  if data__missing_keys:
   if not (isinstance(data, str) and '@' in data):
    raise JsonSchemaValueException("" + (name_prefix or "data") + " must contain " + (str(sorted(data__missing_keys)) + " properties"), value=data, name="" + (name_prefix or "data") + "", definition={'properties': {'delimiter_style': {'type': 'object', 'properties': {'color': {'$ref': 'common.json#/color', 'default_value': '#14000000', '$description': 'translations.json#/div_separator_style_color'}, 'orientation': {'type': 'string', 'enum': ['vertical', 'horizontal'], 'default_value': 'horizontal', '$description': 'translations.json#/div_separator_style_orientation'}}}, 'type': {'type': 'string', 'enum': ['separator']}}, 'required': ['type']}, rule='required')
  data_keys = set(data.keys())
  if "delimiter_style" in data_keys:
   data_keys.remove("delimiter_style")
   data__delimiterstyle = data["delimiter_style"]
   validate_div_separator_json__definitions_style(data__delimiterstyle, custom_formats, (name_prefix or "data") + ".delimiter_style")
  if "type" in data_keys:
   data_keys.remove("type")
   data__type = data["type"]
   if not isinstance(data__type, (str)):
    if not (isinstance(data__type, str) and '@' in data__type):
     raise JsonSchemaValueException("" + (name_prefix or "data") + ".type must be string", value=data__type, name="" + (name_prefix or "data") + ".type", definition={'type': 'string', 'enum': ['separator']}, rule='type')
   if data__type not in ['separator']:
    if not (isinstance(data__type, str) and '@' in data__type):
     raise JsonSchemaValueException("" + (name_prefix or "data") + ".type must be one of ['separator']", value=data__type, name="" + (name_prefix or "data") + ".type", definition={'type': 'string', 'enum': ['separator']}, rule='enum')
 return data

def validate_div_separator_json__definitions_style(data, custom_formats={}, name_prefix=None):
 if not isinstance(data, (dict)):
  if not (isinstance(data, str) and '@' in data):
   raise JsonSchemaValueException("" + (name_prefix or "data") + " must be object", value=data, name="" + (name_prefix or "data") + "", definition={'type': 'object', 'properties': {'color': {'type': 'string', 'format': 'color'}, 'orientation': {'type': 'string', 'enum': ['vertical', 'horizontal'], 'default_value': 'horizontal', '$description': 'translations.json#/div_separator_style_orientation'}}}, rule='type')
 data_is_dict = isinstance(data, dict)
 if data_is_dict:
  data_keys = set(data.keys())
  if "color" in data_keys:
   data_keys.remove("color")
   data__color = data["color"]
   validate_common_json__color(data__color, custom_formats, (name_prefix or "data") + ".color")
  if "orientation" in data_keys:
   data_keys.remove("orientation")
   data__orientation = data["orientation"]
   if not isinstance(data__orientation, (str)):
    if not (isinstance(data__orientation, str) and '@' in data__orientation):
     raise JsonSchemaValueException("" + (name_prefix or "data") + ".orientation must be string", value=data__orientation, name="" + (name_prefix or "data") + ".orientation", definition={'type': 'string', 'enum': ['vertical', 'horizontal'], 'default_value': 'horizontal', '$description': 'translations.json#/div_separator_style_orientation'}, rule='type')
   if data__orientation not in ['vertical', 'horizontal']:
    if not (isinstance(data__orientation, str) and '@' in data__orientation):
     raise JsonSchemaValueException("" + (name_prefix or "data") + ".orientation must be one of ['vertical', 'horizontal']", value=data__orientation, name="" + (name_prefix or "data") + ".orientation", definition={'type': 'string', 'enum': ['vertical', 'horizontal'], 'default_value': 'horizontal', '$description': 'translations.json#/div_separator_style_orientation'}, rule='enum')
 return data

def validate_div_text_json(data, custom_formats={}, name_prefix=None):
 validate_div_base_json(data, custom_formats, (name_prefix or "data") + "")
 validate_div_actionable_json(data, custom_formats, (name_prefix or "data") + "")
 data_is_dict = isinstance(data, dict)
 if data_is_dict:
  data_keys = set(data.keys())
  if "type" in data_keys:
   data_keys.remove("type")
   data__type = data["type"]
   if not isinstance(data__type, (str)):
    if not (isinstance(data__type, str) and '@' in data__type):
     raise JsonSchemaValueException("" + (name_prefix or "data") + ".type must be string", value=data__type, name="" + (name_prefix or "data") + ".type", definition={'type': 'string', 'enum': ['text']}, rule='type')
   if data__type not in ['text']:
    if not (isinstance(data__type, str) and '@' in data__type):
     raise JsonSchemaValueException("" + (name_prefix or "data") + ".type must be one of ['text']", value=data__type, name="" + (name_prefix or "data") + ".type", definition={'type': 'string', 'enum': ['text']}, rule='enum')
  if "font_size" in data_keys:
   data_keys.remove("font_size")
   data__fontsize = data["font_size"]
   validate_common_json__non_negative_integer(data__fontsize, custom_formats, (name_prefix or "data") + ".font_size")
  if "font_family" in data_keys:
   data_keys.remove("font_family")
   data__fontfamily = data["font_family"]
   validate_common_json__non_empty_string(data__fontfamily, custom_formats, (name_prefix or "data") + ".font_family")
  if "font_size_unit" in data_keys:
   data_keys.remove("font_size_unit")
   data__fontsizeunit = data["font_size_unit"]
   validate_div_size_unit_json(data__fontsizeunit, custom_formats, (name_prefix or "data") + ".font_size_unit")
  if "line_height" in data_keys:
   data_keys.remove("line_height")
   data__lineheight = data["line_height"]
   validate_common_json__non_negative_integer(data__lineheight, custom_formats, (name_prefix or "data") + ".line_height")
  if "max_lines" in data_keys:
   data_keys.remove("max_lines")
   data__maxlines = data["max_lines"]
   validate_common_json__non_negative_integer(data__maxlines, custom_formats, (name_prefix or "data") + ".max_lines")
  if "min_hidden_lines" in data_keys:
   data_keys.remove("min_hidden_lines")
   data__minhiddenlines = data["min_hidden_lines"]
   validate_common_json__non_negative_integer(data__minhiddenlines, custom_formats, (name_prefix or "data") + ".min_hidden_lines")
  if "auto_ellipsize" in data_keys:
   data_keys.remove("auto_ellipsize")
   data__autoellipsize = data["auto_ellipsize"]
   validate_common_json__boolean_int(data__autoellipsize, custom_formats, (name_prefix or "data") + ".auto_ellipsize")
  if "letter_spacing" in data_keys:
   data_keys.remove("letter_spacing")
   data__letterspacing = data["letter_spacing"]
   if not isinstance(data__letterspacing, (int, float, Decimal)) or isinstance(data__letterspacing, bool):
    if not (isinstance(data__letterspacing, str) and '@' in data__letterspacing):
     raise JsonSchemaValueException("" + (name_prefix or "data") + ".letter_spacing must be number", value=data__letterspacing, name="" + (name_prefix or "data") + ".letter_spacing", definition={'type': 'number', 'default_value': '0', '$description': 'translations.json#/div_text_letter_spacing'}, rule='type')
  if "font_weight" in data_keys:
   data_keys.remove("font_weight")
   data__fontweight = data["font_weight"]
   validate_div_font_weight_json(data__fontweight, custom_formats, (name_prefix or "data") + ".font_weight")
  if "text_alignment_horizontal" in data_keys:
   data_keys.remove("text_alignment_horizontal")
   data__textalignmenthorizontal = data["text_alignment_horizontal"]
   validate_div_alignment_horizontal_json(data__textalignmenthorizontal, custom_formats, (name_prefix or "data") + ".text_alignment_horizontal")
  if "text_alignment_vertical" in data_keys:
   data_keys.remove("text_alignment_vertical")
   data__textalignmentvertical = data["text_alignment_vertical"]
   validate_div_alignment_vertical_json(data__textalignmentvertical, custom_formats, (name_prefix or "data") + ".text_alignment_vertical")
  if "text_color" in data_keys:
   data_keys.remove("text_color")
   data__textcolor = data["text_color"]
   validate_common_json__color(data__textcolor, custom_formats, (name_prefix or "data") + ".text_color")
  if "focused_text_color" in data_keys:
   data_keys.remove("focused_text_color")
   data__focusedtextcolor = data["focused_text_color"]
   validate_common_json__color(data__focusedtextcolor, custom_formats, (name_prefix or "data") + ".focused_text_color")
  if "text_gradient" in data_keys:
   data_keys.remove("text_gradient")
   data__textgradient = data["text_gradient"]
   validate_div_text_gradient_json(data__textgradient, custom_formats, (name_prefix or "data") + ".text_gradient")
  if "text" in data_keys:
   data_keys.remove("text")
   data__text = data["text"]
   validate_common_json__non_empty_string(data__text, custom_formats, (name_prefix or "data") + ".text")
  if "underline" in data_keys:
   data_keys.remove("underline")
   data__underline = data["underline"]
   validate_div_line_style_json(data__underline, custom_formats, (name_prefix or "data") + ".underline")
  if "strike" in data_keys:
   data_keys.remove("strike")
   data__strike = data["strike"]
   validate_div_line_style_json(data__strike, custom_formats, (name_prefix or "data") + ".strike")
  if "ranges" in data_keys:
   data_keys.remove("ranges")
   data__ranges = data["ranges"]
   if not isinstance(data__ranges, (list, tuple)):
    if not (isinstance(data__ranges, str) and '@' in data__ranges):
     raise JsonSchemaValueException("" + (name_prefix or "data") + ".ranges must be array", value=data__ranges, name="" + (name_prefix or "data") + ".ranges", definition={'type': 'array', 'items': {'type': 'object', 'properties': {'start': {'$ref': 'common.json#/non_negative_integer', '$description': 'translations.json#/div_text_range_start'}, 'end': {'$ref': 'common.json#/positive_integer', '$description': 'translations.json#/div_text_range_end'}, 'font_size': {'$ref': 'common.json#/non_negative_integer', '$description': 'translations.json#/div_font_size'}, 'font_family': {'$ref': 'common.json#/non_empty_string', '$description': 'translations.json#/div_font_family'}, 'font_size_unit': {'$ref': 'div-size-unit.json', 'default_value': 'sp', '$description': 'translations.json#/div_font_size_unit', 'platforms': ['android', 'ios']}, 'letter_spacing': {'type': 'number', '$description': 'translations.json#/div_text_range_letter_spacing'}, 'font_weight': {'$ref': 'div-font-weight.json', '$description': 'translations.json#/div_font_weight'}, 'text_color': {'$ref': 'common.json#/color', '$description': 'translations.json#/div_text_color'}, 'underline': {'$ref': 'div-line-style.json', '$description': 'translations.json#/div_text_range_underline'}, 'strike': {'$ref': 'div-line-style.json', '$description': 'translations.json#/div_text_range_strike'}, 'actions': {'type': 'array', 'items': {'$ref': 'div-action.json'}, 'minItems': 1, '$description': 'translations.json#/div_text_range_actions'}, 'line_height': {'$ref': 'common.json#/non_negative_integer', '$description': 'translations.json#/div_text_range_line_height'}, 'top_offset': {'$ref': 'common.json#/non_negative_integer', '$description': 'translations.json#/div_text_range_top_offset'}, 'border': {'$ref': 'div-text-range-border.json', '$description': 'translations.json#/div_text_range_border'}, 'background': {'$ref': 'div-text-range-background.json', '$description': 'translations.json#/div_text_range_background'}, 'text_shadow': {'$ref': 'div-shadow.json', '$description': 'translations.json#/div_text_range_shadow', 'platforms': ['android']}}, 'required': ['start', 'end'], '$description': 'translations.json#/div_text_range'}, 'minItems': 1, '$description': 'translations.json#/div_text_ranges'}, rule='type')
   data__ranges_is_list = isinstance(data__ranges, (list, tuple))
   if data__ranges_is_list:
    data__ranges_len = len(data__ranges)
    if data__ranges_len < 1:
     if not (isinstance(data__ranges, str) and '@' in data__ranges):
      raise JsonSchemaValueException("" + (name_prefix or "data") + ".ranges must contain at least 1 items", value=data__ranges, name="" + (name_prefix or "data") + ".ranges", definition={'type': 'array', 'items': {'type': 'object', 'properties': {'start': {'$ref': 'common.json#/non_negative_integer', '$description': 'translations.json#/div_text_range_start'}, 'end': {'$ref': 'common.json#/positive_integer', '$description': 'translations.json#/div_text_range_end'}, 'font_size': {'$ref': 'common.json#/non_negative_integer', '$description': 'translations.json#/div_font_size'}, 'font_family': {'$ref': 'common.json#/non_empty_string', '$description': 'translations.json#/div_font_family'}, 'font_size_unit': {'$ref': 'div-size-unit.json', 'default_value': 'sp', '$description': 'translations.json#/div_font_size_unit', 'platforms': ['android', 'ios']}, 'letter_spacing': {'type': 'number', '$description': 'translations.json#/div_text_range_letter_spacing'}, 'font_weight': {'$ref': 'div-font-weight.json', '$description': 'translations.json#/div_font_weight'}, 'text_color': {'$ref': 'common.json#/color', '$description': 'translations.json#/div_text_color'}, 'underline': {'$ref': 'div-line-style.json', '$description': 'translations.json#/div_text_range_underline'}, 'strike': {'$ref': 'div-line-style.json', '$description': 'translations.json#/div_text_range_strike'}, 'actions': {'type': 'array', 'items': {'$ref': 'div-action.json'}, 'minItems': 1, '$description': 'translations.json#/div_text_range_actions'}, 'line_height': {'$ref': 'common.json#/non_negative_integer', '$description': 'translations.json#/div_text_range_line_height'}, 'top_offset': {'$ref': 'common.json#/non_negative_integer', '$description': 'translations.json#/div_text_range_top_offset'}, 'border': {'$ref': 'div-text-range-border.json', '$description': 'translations.json#/div_text_range_border'}, 'background': {'$ref': 'div-text-range-background.json', '$description': 'translations.json#/div_text_range_background'}, 'text_shadow': {'$ref': 'div-shadow.json', '$description': 'translations.json#/div_text_range_shadow', 'platforms': ['android']}}, 'required': ['start', 'end'], '$description': 'translations.json#/div_text_range'}, 'minItems': 1, '$description': 'translations.json#/div_text_ranges'}, rule='minItems')
    for data__ranges_x, data__ranges_item in enumerate(data__ranges):
     validate_div_text_json__definitions_range(data__ranges_item, custom_formats, (name_prefix or "data") + ".ranges[{data__ranges_x}]".format(**locals()))
  if "images" in data_keys:
   data_keys.remove("images")
   data__images = data["images"]
   if not isinstance(data__images, (list, tuple)):
    if not (isinstance(data__images, str) and '@' in data__images):
     raise JsonSchemaValueException("" + (name_prefix or "data") + ".images must be array", value=data__images, name="" + (name_prefix or "data") + ".images", definition={'type': 'array', 'items': {'type': 'object', 'properties': {'start': {'$ref': 'common.json#/non_negative_integer', '$description': 'translations.json#/div_text_image_start'}, 'url': {'$ref': 'common.json#/url', '$description': 'translations.json#/div_text_image_url'}, 'width': {'$ref': 'div-fixed-size.json', 'default_value': '{"type": "fixed","value":20}', '$description': 'translations.json#/div_text_image_width'}, 'height': {'$ref': 'div-fixed-size.json', 'default_value': '{"type": "fixed","value":20}', '$description': 'translations.json#/div_text_image_height'}, 'tint_color': {'$ref': 'common.json#/color', '$description': 'translations.json#/div_text_image_tint_color'}, 'tint_mode': {'$ref': 'div-blend-mode.json', 'default_value': 'source_in', '$description': 'translations.json#/div_text_image_tint_mode', 'platforms': ['android', 'web']}}, 'required': ['url', 'start'], '$description': 'translations.json#/div_text_image'}, 'minItems': 1, '$description': 'translations.json#/div_text_images'}, rule='type')
   data__images_is_list = isinstance(data__images, (list, tuple))
   if data__images_is_list:
    data__images_len = len(data__images)
    if data__images_len < 1:
     if not (isinstance(data__images, str) and '@' in data__images):
      raise JsonSchemaValueException("" + (name_prefix or "data") + ".images must contain at least 1 items", value=data__images, name="" + (name_prefix or "data") + ".images", definition={'type': 'array', 'items': {'type': 'object', 'properties': {'start': {'$ref': 'common.json#/non_negative_integer', '$description': 'translations.json#/div_text_image_start'}, 'url': {'$ref': 'common.json#/url', '$description': 'translations.json#/div_text_image_url'}, 'width': {'$ref': 'div-fixed-size.json', 'default_value': '{"type": "fixed","value":20}', '$description': 'translations.json#/div_text_image_width'}, 'height': {'$ref': 'div-fixed-size.json', 'default_value': '{"type": "fixed","value":20}', '$description': 'translations.json#/div_text_image_height'}, 'tint_color': {'$ref': 'common.json#/color', '$description': 'translations.json#/div_text_image_tint_color'}, 'tint_mode': {'$ref': 'div-blend-mode.json', 'default_value': 'source_in', '$description': 'translations.json#/div_text_image_tint_mode', 'platforms': ['android', 'web']}}, 'required': ['url', 'start'], '$description': 'translations.json#/div_text_image'}, 'minItems': 1, '$description': 'translations.json#/div_text_images'}, rule='minItems')
    for data__images_x, data__images_item in enumerate(data__images):
     validate_div_text_json__definitions_image(data__images_item, custom_formats, (name_prefix or "data") + ".images[{data__images_x}]".format(**locals()))
  if "ellipsis" in data_keys:
   data_keys.remove("ellipsis")
   data__ellipsis = data["ellipsis"]
   validate_div_text_json__definitions_ellipsis(data__ellipsis, custom_formats, (name_prefix or "data") + ".ellipsis")
  if "selectable" in data_keys:
   data_keys.remove("selectable")
   data__selectable = data["selectable"]
   validate_common_json__boolean_int(data__selectable, custom_formats, (name_prefix or "data") + ".selectable")
  if "truncate" in data_keys:
   data_keys.remove("truncate")
   data__truncate = data["truncate"]
   if not isinstance(data__truncate, (str)):
    if not (isinstance(data__truncate, str) and '@' in data__truncate):
     raise JsonSchemaValueException("" + (name_prefix or "data") + ".truncate must be string", value=data__truncate, name="" + (name_prefix or "data") + ".truncate", definition={'type': 'string', 'enum': ['none', 'start', 'end', 'middle'], 'default_value': 'end', '$description': 'translations.json#/div_text_truncate', 'deprecated': True, 'code_generation_disabled_kotlin': True, 'code_generation_disabled_swift': True}, rule='type')
   if data__truncate not in ['none', 'start', 'end', 'middle']:
    if not (isinstance(data__truncate, str) and '@' in data__truncate):
     raise JsonSchemaValueException("" + (name_prefix or "data") + ".truncate must be one of ['none', 'start', 'end', 'middle']", value=data__truncate, name="" + (name_prefix or "data") + ".truncate", definition={'type': 'string', 'enum': ['none', 'start', 'end', 'middle'], 'default_value': 'end', '$description': 'translations.json#/div_text_truncate', 'deprecated': True, 'code_generation_disabled_kotlin': True, 'code_generation_disabled_swift': True}, rule='enum')
  if "text_shadow" in data_keys:
   data_keys.remove("text_shadow")
   data__textshadow = data["text_shadow"]
   validate_div_shadow_json(data__textshadow, custom_formats, (name_prefix or "data") + ".text_shadow")
 data_is_dict = isinstance(data, dict)
 if data_is_dict:
  data__missing_keys = set(['type', 'text']) - data.keys()
  if data__missing_keys:
   if not (isinstance(data, str) and '@' in data):
    raise JsonSchemaValueException("" + (name_prefix or "data") + " must contain " + (str(sorted(data__missing_keys)) + " properties"), value=data, name="" + (name_prefix or "data") + "", definition={'java_extends': 'DivBlockWithId', '$description': 'translations.json#/div_text', 'codegen': {'divan': {'forced_properties_order': ['text']}}, 'definitions': {'range': {'type': 'object', 'properties': {'start': {'type': 'integer', 'constraint': 'number >= 0'}, 'end': {'type': 'integer', 'constraint': 'number > 0'}, 'font_size': {'type': 'integer', 'constraint': 'number >= 0'}, 'font_family': {'type': 'string', 'minLength': 1, 'clientMinLength': 1}, 'font_size_unit': {'type': 'string', 'enum': ['dp', 'sp', 'px'], '$description': 'translations.json#/div_size_unit', 'platforms': ['android', 'ios'], '$schema': 'http://json-schema.org/draft-07/schema'}, 'letter_spacing': {'type': 'number', '$description': 'translations.json#/div_text_range_letter_spacing'}, 'font_weight': {'type': 'string', 'enum': ['light', 'medium', 'regular', 'bold'], '$schema': 'http://json-schema.org/draft-07/schema'}, 'text_color': {'type': 'string', 'format': 'color'}, 'underline': {'type': 'string', '$description': 'translations.json#/div_line_style', 'enum': ['none', 'single'], '$schema': 'http://json-schema.org/draft-07/schema'}, 'strike': {'type': 'string', '$description': 'translations.json#/div_line_style', 'enum': ['none', 'single'], '$schema': 'http://json-schema.org/draft-07/schema'}, 'actions': {'type': 'array', 'items': {'definitions': {'menu_item': {'type': 'object', 'properties': {'text': {'$ref': 'common.json#/non_empty_string', '$description': 'translations.json#/div_action_menu_item_text'}, 'action': {'$ref': 'div-action.json', '$description': 'translations.json#/div_action_menu_item_action'}, 'actions': {'type': 'array', 'items': {'$ref': 'div-action.json'}, 'minItems': 1, '$description': 'translations.json#/div_action_menu_item_actions'}}, 'required': ['text']}}, 'allOf': [{'$ref': 'div-action-base.json'}, {'type': 'object', '$description': 'translations.json#/div_action', 'properties': {'menu_items': {'type': 'array', 'items': {'$ref': '#/definitions/menu_item'}, '$description': 'translations.json#/div_action_menu_items', 'platforms': ['android', 'ios']}, 'log_url': {'$ref': 'common.json#/url', '$description': 'translations.json#/div_action_log_url'}, 'target': {'type': 'string', 'enum': ['_self', '_blank'], 'force_enum_field': True, '$description': 'translations.json#/div_action_target', 'platforms': ['web'], 'code_generation_disabled_swift': True}}, 'required': ['log_id']}], '$schema': 'http://json-schema.org/draft-07/schema'}, 'minItems': 1, '$description': 'translations.json#/div_text_range_actions'}, 'line_height': {'type': 'integer', 'constraint': 'number >= 0'}, 'top_offset': {'type': 'integer', 'constraint': 'number >= 0'}, 'border': {'type': 'object', '$description': 'translations.json#/div_text_range_border', 'properties': {'stroke': {'$ref': 'div-stroke.json', '$description': 'translations.json#/div_border_stroke'}, 'corner_radius': {'$ref': 'common.json#/non_negative_integer', '$description': 'translations.json#/div_border_corner_radius'}}, '$schema': 'http://json-schema.org/draft-07/schema'}, 'background': {'anyOf': [{'$ref': 'div-solid-background.json', '$description': 'translations.json#/div_background_solid'}], '$schema': 'http://json-schema.org/draft-07/schema'}, 'text_shadow': {'type': 'object', '$description': 'translations.json#/div_shadow', 'properties': {'color': {'$ref': 'common.json#/color', '$description': 'translations.json#/div_shadow_color', 'default_value': '#000000'}, 'offset': {'$ref': 'div-point.json', '$description': 'translations.json#/div_shadow_offset'}, 'blur': {'$ref': 'common.json#/non_negative_integer', '$description': 'translations.json#/div_shadow_blur', 'default_value': '2'}, 'alpha': {'type': 'number', 'default_value': '0.19', 'constraint': 'number >= 0.0 && number <= 1.0', '$description': 'translations.json#/div_shadow_alpha'}}, 'required': ['offset'], '$schema': 'http://json-schema.org/draft-07/schema'}}, 'required': ['start', 'end'], '$description': 'translations.json#/div_text_range'}, 'image': {'type': 'object', 'properties': {'start': {'type': 'integer', 'constraint': 'number >= 0'}, 'url': {'type': 'string', 'format': 'uri'}, 'width': {'type': 'object', '$description': 'translations.json#/div_fixed_size', 'codegen': {'divan': {'forced_properties_order': ['value']}}, 'properties': {'value': {'$ref': 'common.json#/non_negative_integer', '$description': 'translations.json#/div_fixed_size_value'}, 'unit': {'$ref': 'div-size-unit.json', '$description': 'translations.json#/div_fixed_size_unit', 'default_value': 'dp'}, 'type': {'type': 'string', 'enum': ['fixed']}}, 'required': ['value', 'type'], '$schema': 'http://json-schema.org/draft-07/schema'}, 'height': {'type': 'object', '$description': 'translations.json#/div_fixed_size', 'codegen': {'divan': {'forced_properties_order': ['value']}}, 'properties': {'value': {'$ref': 'common.json#/non_negative_integer', '$description': 'translations.json#/div_fixed_size_value'}, 'unit': {'$ref': 'div-size-unit.json', '$description': 'translations.json#/div_fixed_size_unit', 'default_value': 'dp'}, 'type': {'type': 'string', 'enum': ['fixed']}}, 'required': ['value', 'type'], '$schema': 'http://json-schema.org/draft-07/schema'}, 'tint_color': {'type': 'string', 'format': 'color'}, 'tint_mode': {'type': 'string', 'enum': ['source_in', 'source_atop', 'darken', 'lighten', 'multiply', 'screen'], '$description': 'translations.json#/div_blend_mode', '$schema': 'http://json-schema.org/draft-07/schema'}}, 'required': ['url', 'start'], '$description': 'translations.json#/div_text_image'}, 'ellipsis': {'type': 'object', 'properties': {'text': {'type': 'string', 'minLength': 1, 'clientMinLength': 1}, 'actions': {'type': 'array', 'items': {'definitions': {'menu_item': {'type': 'object', 'properties': {'text': {'$ref': 'common.json#/non_empty_string', '$description': 'translations.json#/div_action_menu_item_text'}, 'action': {'$ref': 'div-action.json', '$description': 'translations.json#/div_action_menu_item_action'}, 'actions': {'type': 'array', 'items': {'$ref': 'div-action.json'}, 'minItems': 1, '$description': 'translations.json#/div_action_menu_item_actions'}}, 'required': ['text']}}, 'allOf': [{'$ref': 'div-action-base.json'}, {'type': 'object', '$description': 'translations.json#/div_action', 'properties': {'menu_items': {'type': 'array', 'items': {'$ref': '#/definitions/menu_item'}, '$description': 'translations.json#/div_action_menu_items', 'platforms': ['android', 'ios']}, 'log_url': {'$ref': 'common.json#/url', '$description': 'translations.json#/div_action_log_url'}, 'target': {'type': 'string', 'enum': ['_self', '_blank'], 'force_enum_field': True, '$description': 'translations.json#/div_action_target', 'platforms': ['web'], 'code_generation_disabled_swift': True}}, 'required': ['log_id']}], '$schema': 'http://json-schema.org/draft-07/schema'}, 'minItems': 1, '$description': 'translations.json#/div_text_ellipsis_actions'}, 'ranges': {'type': 'array', 'items': {'type': 'object', 'properties': {'start': {'$ref': 'common.json#/non_negative_integer', '$description': 'translations.json#/div_text_range_start'}, 'end': {'$ref': 'common.json#/positive_integer', '$description': 'translations.json#/div_text_range_end'}, 'font_size': {'$ref': 'common.json#/non_negative_integer', '$description': 'translations.json#/div_font_size'}, 'font_family': {'$ref': 'common.json#/non_empty_string', '$description': 'translations.json#/div_font_family'}, 'font_size_unit': {'$ref': 'div-size-unit.json', 'default_value': 'sp', '$description': 'translations.json#/div_font_size_unit', 'platforms': ['android', 'ios']}, 'letter_spacing': {'type': 'number', '$description': 'translations.json#/div_text_range_letter_spacing'}, 'font_weight': {'$ref': 'div-font-weight.json', '$description': 'translations.json#/div_font_weight'}, 'text_color': {'$ref': 'common.json#/color', '$description': 'translations.json#/div_text_color'}, 'underline': {'$ref': 'div-line-style.json', '$description': 'translations.json#/div_text_range_underline'}, 'strike': {'$ref': 'div-line-style.json', '$description': 'translations.json#/div_text_range_strike'}, 'actions': {'type': 'array', 'items': {'$ref': 'div-action.json'}, 'minItems': 1, '$description': 'translations.json#/div_text_range_actions'}, 'line_height': {'$ref': 'common.json#/non_negative_integer', '$description': 'translations.json#/div_text_range_line_height'}, 'top_offset': {'$ref': 'common.json#/non_negative_integer', '$description': 'translations.json#/div_text_range_top_offset'}, 'border': {'$ref': 'div-text-range-border.json', '$description': 'translations.json#/div_text_range_border'}, 'background': {'$ref': 'div-text-range-background.json', '$description': 'translations.json#/div_text_range_background'}, 'text_shadow': {'$ref': 'div-shadow.json', '$description': 'translations.json#/div_text_range_shadow', 'platforms': ['android']}}, 'required': ['start', 'end'], '$description': 'translations.json#/div_text_range'}, 'minItems': 1, '$description': 'translations.json#/div_text_ellipsis_ranges'}, 'images': {'type': 'array', 'items': {'type': 'object', 'properties': {'start': {'$ref': 'common.json#/non_negative_integer', '$description': 'translations.json#/div_text_image_start'}, 'url': {'$ref': 'common.json#/url', '$description': 'translations.json#/div_text_image_url'}, 'width': {'$ref': 'div-fixed-size.json', 'default_value': '{"type": "fixed","value":20}', '$description': 'translations.json#/div_text_image_width'}, 'height': {'$ref': 'div-fixed-size.json', 'default_value': '{"type": "fixed","value":20}', '$description': 'translations.json#/div_text_image_height'}, 'tint_color': {'$ref': 'common.json#/color', '$description': 'translations.json#/div_text_image_tint_color'}, 'tint_mode': {'$ref': 'div-blend-mode.json', 'default_value': 'source_in', '$description': 'translations.json#/div_text_image_tint_mode', 'platforms': ['android', 'web']}}, 'required': ['url', 'start'], '$description': 'translations.json#/div_text_image'}, 'minItems': 1, '$description': 'translations.json#/div_text_ellipsis_images'}}, 'required': ['text'], '$description': 'translations.json#/div_text_ellipsis', 'platforms': ['android', 'ios']}}, 'allOf': [{'protocol_name': 'div-base', 'codegen': {'swift': {'super_protocol': 'DivBlockModeling'}, 'documentation': {'include_in_toc': True}}, 'type': 'object', 'properties': {'id': {'$ref': 'common.json#/non_empty_string', 'supports_expressions': False, '$description': 'translations.json#/div_base_id'}, 'border': {'$ref': 'div-border.json', '$description': 'translations.json#/div_base_border'}, 'width': {'$ref': 'div-size.json', 'default_value': '{"type": "match_parent"}', '$description': 'translations.json#/div_base_width'}, 'height': {'$ref': 'div-size.json', 'default_value': '{"type": "wrap_content"}', '$description': 'translations.json#/div_base_height'}, 'background': {'type': 'array', 'items': {'$ref': 'div-background.json'}, 'minItems': 1, '$description': 'translations.json#/div_base_background'}, 'paddings': {'$ref': 'div-edge-insets.json', '$description': 'translations.json#/div_base_paddings'}, 'margins': {'$ref': 'div-edge-insets.json', '$description': 'translations.json#/div_base_margins'}, 'alpha': {'type': 'number', 'default_value': '1.0', 'constraint': 'number >= 0.0 && number <= 1.0', '$description': 'translations.json#/div_base_alpha'}, 'alignment_vertical': {'$ref': 'div-alignment-vertical.json', '$description': 'translations.json#/div_base_alignment_vertical'}, 'alignment_horizontal': {'$ref': 'div-alignment-horizontal.json', '$description': 'translations.json#/div_base_alignment_horizontal'}, 'row_span': {'$ref': 'common.json#/non_negative_integer', '$description': 'translations.json#/div_base_row_span'}, 'column_span': {'$ref': 'common.json#/non_negative_integer', '$description': 'translations.json#/div_base_column_span'}, 'visibility_action': {'$ref': 'div-visibility-action.json', '$description': 'translations.json#/div_base_visibility_action'}, 'visibility_actions': {'type': 'array', 'items': {'$ref': 'div-visibility-action.json'}, 'minItems': 1, '$description': 'translations.json#/div_base_visibility_actions'}, 'disappear_actions': {'type': 'array', 'items': {'$ref': 'div-disappear-action.json'}, 'minItems': 1, '$description': 'translations.json#/div_base_disappear_actions'}, 'tooltips': {'type': 'array', 'items': {'$ref': 'div-tooltip.json'}, 'minItems': 1, '$description': 'translations.json#/div_base_tooltips'}, 'accessibility': {'$ref': 'div-accessibility.json', '$description': 'translations.json#/div_base_accessibility'}, 'extensions': {'type': 'array', 'items': {'$ref': 'div-extension.json'}, 'minItems': 1, '$description': 'translations.json#/div_base_extensions'}, 'transition_triggers': {'type': 'array', 'items': {'$ref': 'div-transition-trigger.json'}, 'minItems': 1, 'supports_expressions': False, '$description': 'translations.json#/div_base_transition_triggers'}, 'transition_in': {'$ref': 'div-appearance-transition.json', '$description': 'translations.json#/div_base_transition_in'}, 'transition_change': {'$ref': 'div-change-transition.json', '$description': 'translations.json#/div_base_transition_change'}, 'transition_out': {'$ref': 'div-appearance-transition.json', '$description': 'translations.json#/div_base_transition_out'}, 'selected_actions': {'type': 'array', 'items': {'$ref': 'div-action.json'}, 'minItems': 1, '$description': 'translations.json#/div_base_selected_actions'}, 'focus': {'$ref': 'div-focus.json', '$description': 'translations.json#/div_base_focus', 'platforms': ['android', 'ios']}, 'visibility': {'$ref': 'div-visibility.json', '$description': 'translations.json#/div_base_visibility', 'default_value': 'visible'}, 'transform': {'$ref': 'div-transform.json', '$description': 'translations.json#/div_base_transform'}}, '$schema': 'http://json-schema.org/draft-07/schema'}, {'properties': {'action': {'$ref': 'div-action.json', '$description': 'translations.json#/div_actionable_action'}, 'actions': {'type': 'array', 'items': {'$ref': 'div-action.json'}, 'minItems': 1, '$description': 'translations.json#/div_actionable_actions'}, 'longtap_actions': {'type': 'array', 'items': {'$ref': 'div-action.json'}, 'minItems': 1, '$description': 'translations.json#/div_actionable_longtap_actions'}, 'doubletap_actions': {'type': 'array', 'items': {'$ref': 'div-action.json'}, 'minItems': 1, '$description': 'translations.json#/div_actionable_doubletap_actions'}, 'action_animation': {'$ref': 'div-animation.json', 'default_value': '{"name": "fade", "start_value": 1, "end_value": 0.6, "duration": 100 }', '$description': 'translations.json#/div_actionable_action_animation'}}, '$schema': 'http://json-schema.org/draft-07/schema'}, {'properties': {'type': {'type': 'string', 'enum': ['text']}, 'font_size': {'type': 'integer', 'constraint': 'number >= 0'}, 'font_family': {'type': 'string', 'minLength': 1, 'clientMinLength': 1}, 'font_size_unit': {'type': 'string', 'enum': ['dp', 'sp', 'px'], '$description': 'translations.json#/div_size_unit', 'platforms': ['android', 'ios'], '$schema': 'http://json-schema.org/draft-07/schema'}, 'line_height': {'type': 'integer', 'constraint': 'number >= 0'}, 'max_lines': {'type': 'integer', 'constraint': 'number >= 0'}, 'min_hidden_lines': {'type': 'integer', 'constraint': 'number >= 0'}, 'auto_ellipsize': {'oneOf': [{'type': 'boolean'}, {'type': 'integer', 'enum': [0, 1]}]}, 'letter_spacing': {'type': 'number', 'default_value': '0', '$description': 'translations.json#/div_text_letter_spacing'}, 'font_weight': {'type': 'string', 'enum': ['light', 'medium', 'regular', 'bold'], '$schema': 'http://json-schema.org/draft-07/schema'}, 'text_alignment_horizontal': {'type': 'string', 'enum': ['left', 'center', 'right', 'start', 'end'], '$schema': 'http://json-schema.org/draft-07/schema'}, 'text_alignment_vertical': {'type': 'string', 'enum': ['top', 'center', 'bottom', 'baseline'], '$schema': 'http://json-schema.org/draft-07/schema'}, 'text_color': {'type': 'string', 'format': 'color'}, 'focused_text_color': {'type': 'string', 'format': 'color'}, 'text_gradient': {'anyOf': [{'$ref': 'div-linear-gradient.json', '$description': 'translations.json#/div_gradient_linear'}, {'$ref': 'div-radial-gradient.json', '$description': 'translations.json#/div_gradient_radial'}], '$schema': 'http://json-schema.org/draft-07/schema'}, 'text': {'type': 'string', 'minLength': 1, 'clientMinLength': 1}, 'underline': {'type': 'string', '$description': 'translations.json#/div_line_style', 'enum': ['none', 'single'], '$schema': 'http://json-schema.org/draft-07/schema'}, 'strike': {'type': 'string', '$description': 'translations.json#/div_line_style', 'enum': ['none', 'single'], '$schema': 'http://json-schema.org/draft-07/schema'}, 'ranges': {'type': 'array', 'items': {'type': 'object', 'properties': {'start': {'$ref': 'common.json#/non_negative_integer', '$description': 'translations.json#/div_text_range_start'}, 'end': {'$ref': 'common.json#/positive_integer', '$description': 'translations.json#/div_text_range_end'}, 'font_size': {'$ref': 'common.json#/non_negative_integer', '$description': 'translations.json#/div_font_size'}, 'font_family': {'$ref': 'common.json#/non_empty_string', '$description': 'translations.json#/div_font_family'}, 'font_size_unit': {'$ref': 'div-size-unit.json', 'default_value': 'sp', '$description': 'translations.json#/div_font_size_unit', 'platforms': ['android', 'ios']}, 'letter_spacing': {'type': 'number', '$description': 'translations.json#/div_text_range_letter_spacing'}, 'font_weight': {'$ref': 'div-font-weight.json', '$description': 'translations.json#/div_font_weight'}, 'text_color': {'$ref': 'common.json#/color', '$description': 'translations.json#/div_text_color'}, 'underline': {'$ref': 'div-line-style.json', '$description': 'translations.json#/div_text_range_underline'}, 'strike': {'$ref': 'div-line-style.json', '$description': 'translations.json#/div_text_range_strike'}, 'actions': {'type': 'array', 'items': {'$ref': 'div-action.json'}, 'minItems': 1, '$description': 'translations.json#/div_text_range_actions'}, 'line_height': {'$ref': 'common.json#/non_negative_integer', '$description': 'translations.json#/div_text_range_line_height'}, 'top_offset': {'$ref': 'common.json#/non_negative_integer', '$description': 'translations.json#/div_text_range_top_offset'}, 'border': {'$ref': 'div-text-range-border.json', '$description': 'translations.json#/div_text_range_border'}, 'background': {'$ref': 'div-text-range-background.json', '$description': 'translations.json#/div_text_range_background'}, 'text_shadow': {'$ref': 'div-shadow.json', '$description': 'translations.json#/div_text_range_shadow', 'platforms': ['android']}}, 'required': ['start', 'end'], '$description': 'translations.json#/div_text_range'}, 'minItems': 1, '$description': 'translations.json#/div_text_ranges'}, 'images': {'type': 'array', 'items': {'type': 'object', 'properties': {'start': {'$ref': 'common.json#/non_negative_integer', '$description': 'translations.json#/div_text_image_start'}, 'url': {'$ref': 'common.json#/url', '$description': 'translations.json#/div_text_image_url'}, 'width': {'$ref': 'div-fixed-size.json', 'default_value': '{"type": "fixed","value":20}', '$description': 'translations.json#/div_text_image_width'}, 'height': {'$ref': 'div-fixed-size.json', 'default_value': '{"type": "fixed","value":20}', '$description': 'translations.json#/div_text_image_height'}, 'tint_color': {'$ref': 'common.json#/color', '$description': 'translations.json#/div_text_image_tint_color'}, 'tint_mode': {'$ref': 'div-blend-mode.json', 'default_value': 'source_in', '$description': 'translations.json#/div_text_image_tint_mode', 'platforms': ['android', 'web']}}, 'required': ['url', 'start'], '$description': 'translations.json#/div_text_image'}, 'minItems': 1, '$description': 'translations.json#/div_text_images'}, 'ellipsis': {'type': 'object', 'properties': {'text': {'$ref': 'common.json#/non_empty_string', '$description': 'translations.json#/div_text_ellipsis_text'}, 'actions': {'type': 'array', 'items': {'$ref': 'div-action.json'}, 'minItems': 1, '$description': 'translations.json#/div_text_ellipsis_actions'}, 'ranges': {'type': 'array', 'items': {'$ref': '#/definitions/range'}, 'minItems': 1, '$description': 'translations.json#/div_text_ellipsis_ranges'}, 'images': {'type': 'array', 'items': {'$ref': '#/definitions/image'}, 'minItems': 1, '$description': 'translations.json#/div_text_ellipsis_images'}}, 'required': ['text'], '$description': 'translations.json#/div_text_ellipsis', 'platforms': ['android', 'ios']}, 'selectable': {'oneOf': [{'type': 'boolean'}, {'type': 'integer', 'enum': [0, 1]}]}, 'truncate': {'type': 'string', 'enum': ['none', 'start', 'end', 'middle'], 'default_value': 'end', '$description': 'translations.json#/div_text_truncate', 'deprecated': True, 'code_generation_disabled_kotlin': True, 'code_generation_disabled_swift': True}, 'text_shadow': {'type': 'object', '$description': 'translations.json#/div_shadow', 'properties': {'color': {'$ref': 'common.json#/color', '$description': 'translations.json#/div_shadow_color', 'default_value': '#000000'}, 'offset': {'$ref': 'div-point.json', '$description': 'translations.json#/div_shadow_offset'}, 'blur': {'$ref': 'common.json#/non_negative_integer', '$description': 'translations.json#/div_shadow_blur', 'default_value': '2'}, 'alpha': {'type': 'number', 'default_value': '0.19', 'constraint': 'number >= 0.0 && number <= 1.0', '$description': 'translations.json#/div_shadow_alpha'}}, 'required': ['offset'], '$schema': 'http://json-schema.org/draft-07/schema'}}}], 'required': ['type', 'text'], '$schema': 'http://json-schema.org/draft-07/schema'}, rule='required')
 return data

def validate_div_text_json__definitions_ellipsis(data, custom_formats={}, name_prefix=None):
 if not isinstance(data, (dict)):
  if not (isinstance(data, str) and '@' in data):
   raise JsonSchemaValueException("" + (name_prefix or "data") + " must be object", value=data, name="" + (name_prefix or "data") + "", definition={'type': 'object', 'properties': {'text': {'type': 'string', 'minLength': 1, 'clientMinLength': 1}, 'actions': {'type': 'array', 'items': {'definitions': {'menu_item': {'type': 'object', 'properties': {'text': {'$ref': 'common.json#/non_empty_string', '$description': 'translations.json#/div_action_menu_item_text'}, 'action': {'$ref': 'div-action.json', '$description': 'translations.json#/div_action_menu_item_action'}, 'actions': {'type': 'array', 'items': {'$ref': 'div-action.json'}, 'minItems': 1, '$description': 'translations.json#/div_action_menu_item_actions'}}, 'required': ['text']}}, 'allOf': [{'$ref': 'div-action-base.json'}, {'type': 'object', '$description': 'translations.json#/div_action', 'properties': {'menu_items': {'type': 'array', 'items': {'$ref': '#/definitions/menu_item'}, '$description': 'translations.json#/div_action_menu_items', 'platforms': ['android', 'ios']}, 'log_url': {'$ref': 'common.json#/url', '$description': 'translations.json#/div_action_log_url'}, 'target': {'type': 'string', 'enum': ['_self', '_blank'], 'force_enum_field': True, '$description': 'translations.json#/div_action_target', 'platforms': ['web'], 'code_generation_disabled_swift': True}}, 'required': ['log_id']}], '$schema': 'http://json-schema.org/draft-07/schema'}, 'minItems': 1, '$description': 'translations.json#/div_text_ellipsis_actions'}, 'ranges': {'type': 'array', 'items': {'type': 'object', 'properties': {'start': {'$ref': 'common.json#/non_negative_integer', '$description': 'translations.json#/div_text_range_start'}, 'end': {'$ref': 'common.json#/positive_integer', '$description': 'translations.json#/div_text_range_end'}, 'font_size': {'$ref': 'common.json#/non_negative_integer', '$description': 'translations.json#/div_font_size'}, 'font_family': {'$ref': 'common.json#/non_empty_string', '$description': 'translations.json#/div_font_family'}, 'font_size_unit': {'$ref': 'div-size-unit.json', 'default_value': 'sp', '$description': 'translations.json#/div_font_size_unit', 'platforms': ['android', 'ios']}, 'letter_spacing': {'type': 'number', '$description': 'translations.json#/div_text_range_letter_spacing'}, 'font_weight': {'$ref': 'div-font-weight.json', '$description': 'translations.json#/div_font_weight'}, 'text_color': {'$ref': 'common.json#/color', '$description': 'translations.json#/div_text_color'}, 'underline': {'$ref': 'div-line-style.json', '$description': 'translations.json#/div_text_range_underline'}, 'strike': {'$ref': 'div-line-style.json', '$description': 'translations.json#/div_text_range_strike'}, 'actions': {'type': 'array', 'items': {'$ref': 'div-action.json'}, 'minItems': 1, '$description': 'translations.json#/div_text_range_actions'}, 'line_height': {'$ref': 'common.json#/non_negative_integer', '$description': 'translations.json#/div_text_range_line_height'}, 'top_offset': {'$ref': 'common.json#/non_negative_integer', '$description': 'translations.json#/div_text_range_top_offset'}, 'border': {'$ref': 'div-text-range-border.json', '$description': 'translations.json#/div_text_range_border'}, 'background': {'$ref': 'div-text-range-background.json', '$description': 'translations.json#/div_text_range_background'}, 'text_shadow': {'$ref': 'div-shadow.json', '$description': 'translations.json#/div_text_range_shadow', 'platforms': ['android']}}, 'required': ['start', 'end'], '$description': 'translations.json#/div_text_range'}, 'minItems': 1, '$description': 'translations.json#/div_text_ellipsis_ranges'}, 'images': {'type': 'array', 'items': {'type': 'object', 'properties': {'start': {'$ref': 'common.json#/non_negative_integer', '$description': 'translations.json#/div_text_image_start'}, 'url': {'$ref': 'common.json#/url', '$description': 'translations.json#/div_text_image_url'}, 'width': {'$ref': 'div-fixed-size.json', 'default_value': '{"type": "fixed","value":20}', '$description': 'translations.json#/div_text_image_width'}, 'height': {'$ref': 'div-fixed-size.json', 'default_value': '{"type": "fixed","value":20}', '$description': 'translations.json#/div_text_image_height'}, 'tint_color': {'$ref': 'common.json#/color', '$description': 'translations.json#/div_text_image_tint_color'}, 'tint_mode': {'$ref': 'div-blend-mode.json', 'default_value': 'source_in', '$description': 'translations.json#/div_text_image_tint_mode', 'platforms': ['android', 'web']}}, 'required': ['url', 'start'], '$description': 'translations.json#/div_text_image'}, 'minItems': 1, '$description': 'translations.json#/div_text_ellipsis_images'}}, 'required': ['text'], '$description': 'translations.json#/div_text_ellipsis', 'platforms': ['android', 'ios']}, rule='type')
 data_is_dict = isinstance(data, dict)
 if data_is_dict:
  data__missing_keys = set(['text']) - data.keys()
  if data__missing_keys:
   if not (isinstance(data, str) and '@' in data):
    raise JsonSchemaValueException("" + (name_prefix or "data") + " must contain " + (str(sorted(data__missing_keys)) + " properties"), value=data, name="" + (name_prefix or "data") + "", definition={'type': 'object', 'properties': {'text': {'type': 'string', 'minLength': 1, 'clientMinLength': 1}, 'actions': {'type': 'array', 'items': {'definitions': {'menu_item': {'type': 'object', 'properties': {'text': {'$ref': 'common.json#/non_empty_string', '$description': 'translations.json#/div_action_menu_item_text'}, 'action': {'$ref': 'div-action.json', '$description': 'translations.json#/div_action_menu_item_action'}, 'actions': {'type': 'array', 'items': {'$ref': 'div-action.json'}, 'minItems': 1, '$description': 'translations.json#/div_action_menu_item_actions'}}, 'required': ['text']}}, 'allOf': [{'$ref': 'div-action-base.json'}, {'type': 'object', '$description': 'translations.json#/div_action', 'properties': {'menu_items': {'type': 'array', 'items': {'$ref': '#/definitions/menu_item'}, '$description': 'translations.json#/div_action_menu_items', 'platforms': ['android', 'ios']}, 'log_url': {'$ref': 'common.json#/url', '$description': 'translations.json#/div_action_log_url'}, 'target': {'type': 'string', 'enum': ['_self', '_blank'], 'force_enum_field': True, '$description': 'translations.json#/div_action_target', 'platforms': ['web'], 'code_generation_disabled_swift': True}}, 'required': ['log_id']}], '$schema': 'http://json-schema.org/draft-07/schema'}, 'minItems': 1, '$description': 'translations.json#/div_text_ellipsis_actions'}, 'ranges': {'type': 'array', 'items': {'type': 'object', 'properties': {'start': {'$ref': 'common.json#/non_negative_integer', '$description': 'translations.json#/div_text_range_start'}, 'end': {'$ref': 'common.json#/positive_integer', '$description': 'translations.json#/div_text_range_end'}, 'font_size': {'$ref': 'common.json#/non_negative_integer', '$description': 'translations.json#/div_font_size'}, 'font_family': {'$ref': 'common.json#/non_empty_string', '$description': 'translations.json#/div_font_family'}, 'font_size_unit': {'$ref': 'div-size-unit.json', 'default_value': 'sp', '$description': 'translations.json#/div_font_size_unit', 'platforms': ['android', 'ios']}, 'letter_spacing': {'type': 'number', '$description': 'translations.json#/div_text_range_letter_spacing'}, 'font_weight': {'$ref': 'div-font-weight.json', '$description': 'translations.json#/div_font_weight'}, 'text_color': {'$ref': 'common.json#/color', '$description': 'translations.json#/div_text_color'}, 'underline': {'$ref': 'div-line-style.json', '$description': 'translations.json#/div_text_range_underline'}, 'strike': {'$ref': 'div-line-style.json', '$description': 'translations.json#/div_text_range_strike'}, 'actions': {'type': 'array', 'items': {'$ref': 'div-action.json'}, 'minItems': 1, '$description': 'translations.json#/div_text_range_actions'}, 'line_height': {'$ref': 'common.json#/non_negative_integer', '$description': 'translations.json#/div_text_range_line_height'}, 'top_offset': {'$ref': 'common.json#/non_negative_integer', '$description': 'translations.json#/div_text_range_top_offset'}, 'border': {'$ref': 'div-text-range-border.json', '$description': 'translations.json#/div_text_range_border'}, 'background': {'$ref': 'div-text-range-background.json', '$description': 'translations.json#/div_text_range_background'}, 'text_shadow': {'$ref': 'div-shadow.json', '$description': 'translations.json#/div_text_range_shadow', 'platforms': ['android']}}, 'required': ['start', 'end'], '$description': 'translations.json#/div_text_range'}, 'minItems': 1, '$description': 'translations.json#/div_text_ellipsis_ranges'}, 'images': {'type': 'array', 'items': {'type': 'object', 'properties': {'start': {'$ref': 'common.json#/non_negative_integer', '$description': 'translations.json#/div_text_image_start'}, 'url': {'$ref': 'common.json#/url', '$description': 'translations.json#/div_text_image_url'}, 'width': {'$ref': 'div-fixed-size.json', 'default_value': '{"type": "fixed","value":20}', '$description': 'translations.json#/div_text_image_width'}, 'height': {'$ref': 'div-fixed-size.json', 'default_value': '{"type": "fixed","value":20}', '$description': 'translations.json#/div_text_image_height'}, 'tint_color': {'$ref': 'common.json#/color', '$description': 'translations.json#/div_text_image_tint_color'}, 'tint_mode': {'$ref': 'div-blend-mode.json', 'default_value': 'source_in', '$description': 'translations.json#/div_text_image_tint_mode', 'platforms': ['android', 'web']}}, 'required': ['url', 'start'], '$description': 'translations.json#/div_text_image'}, 'minItems': 1, '$description': 'translations.json#/div_text_ellipsis_images'}}, 'required': ['text'], '$description': 'translations.json#/div_text_ellipsis', 'platforms': ['android', 'ios']}, rule='required')
  data_keys = set(data.keys())
  if "text" in data_keys:
   data_keys.remove("text")
   data__text = data["text"]
   validate_common_json__non_empty_string(data__text, custom_formats, (name_prefix or "data") + ".text")
  if "actions" in data_keys:
   data_keys.remove("actions")
   data__actions = data["actions"]
   if not isinstance(data__actions, (list, tuple)):
    if not (isinstance(data__actions, str) and '@' in data__actions):
     raise JsonSchemaValueException("" + (name_prefix or "data") + ".actions must be array", value=data__actions, name="" + (name_prefix or "data") + ".actions", definition={'type': 'array', 'items': {'definitions': {'menu_item': {'type': 'object', 'properties': {'text': {'$ref': 'common.json#/non_empty_string', '$description': 'translations.json#/div_action_menu_item_text'}, 'action': {'$ref': 'div-action.json', '$description': 'translations.json#/div_action_menu_item_action'}, 'actions': {'type': 'array', 'items': {'$ref': 'div-action.json'}, 'minItems': 1, '$description': 'translations.json#/div_action_menu_item_actions'}}, 'required': ['text']}}, 'allOf': [{'$ref': 'div-action-base.json'}, {'type': 'object', '$description': 'translations.json#/div_action', 'properties': {'menu_items': {'type': 'array', 'items': {'$ref': '#/definitions/menu_item'}, '$description': 'translations.json#/div_action_menu_items', 'platforms': ['android', 'ios']}, 'log_url': {'$ref': 'common.json#/url', '$description': 'translations.json#/div_action_log_url'}, 'target': {'type': 'string', 'enum': ['_self', '_blank'], 'force_enum_field': True, '$description': 'translations.json#/div_action_target', 'platforms': ['web'], 'code_generation_disabled_swift': True}}, 'required': ['log_id']}], '$schema': 'http://json-schema.org/draft-07/schema'}, 'minItems': 1, '$description': 'translations.json#/div_text_ellipsis_actions'}, rule='type')
   data__actions_is_list = isinstance(data__actions, (list, tuple))
   if data__actions_is_list:
    data__actions_len = len(data__actions)
    if data__actions_len < 1:
     if not (isinstance(data__actions, str) and '@' in data__actions):
      raise JsonSchemaValueException("" + (name_prefix or "data") + ".actions must contain at least 1 items", value=data__actions, name="" + (name_prefix or "data") + ".actions", definition={'type': 'array', 'items': {'definitions': {'menu_item': {'type': 'object', 'properties': {'text': {'$ref': 'common.json#/non_empty_string', '$description': 'translations.json#/div_action_menu_item_text'}, 'action': {'$ref': 'div-action.json', '$description': 'translations.json#/div_action_menu_item_action'}, 'actions': {'type': 'array', 'items': {'$ref': 'div-action.json'}, 'minItems': 1, '$description': 'translations.json#/div_action_menu_item_actions'}}, 'required': ['text']}}, 'allOf': [{'$ref': 'div-action-base.json'}, {'type': 'object', '$description': 'translations.json#/div_action', 'properties': {'menu_items': {'type': 'array', 'items': {'$ref': '#/definitions/menu_item'}, '$description': 'translations.json#/div_action_menu_items', 'platforms': ['android', 'ios']}, 'log_url': {'$ref': 'common.json#/url', '$description': 'translations.json#/div_action_log_url'}, 'target': {'type': 'string', 'enum': ['_self', '_blank'], 'force_enum_field': True, '$description': 'translations.json#/div_action_target', 'platforms': ['web'], 'code_generation_disabled_swift': True}}, 'required': ['log_id']}], '$schema': 'http://json-schema.org/draft-07/schema'}, 'minItems': 1, '$description': 'translations.json#/div_text_ellipsis_actions'}, rule='minItems')
    for data__actions_x, data__actions_item in enumerate(data__actions):
     validate_div_action_json(data__actions_item, custom_formats, (name_prefix or "data") + ".actions[{data__actions_x}]".format(**locals()))
  if "ranges" in data_keys:
   data_keys.remove("ranges")
   data__ranges = data["ranges"]
   if not isinstance(data__ranges, (list, tuple)):
    if not (isinstance(data__ranges, str) and '@' in data__ranges):
     raise JsonSchemaValueException("" + (name_prefix or "data") + ".ranges must be array", value=data__ranges, name="" + (name_prefix or "data") + ".ranges", definition={'type': 'array', 'items': {'type': 'object', 'properties': {'start': {'$ref': 'common.json#/non_negative_integer', '$description': 'translations.json#/div_text_range_start'}, 'end': {'$ref': 'common.json#/positive_integer', '$description': 'translations.json#/div_text_range_end'}, 'font_size': {'$ref': 'common.json#/non_negative_integer', '$description': 'translations.json#/div_font_size'}, 'font_family': {'$ref': 'common.json#/non_empty_string', '$description': 'translations.json#/div_font_family'}, 'font_size_unit': {'$ref': 'div-size-unit.json', 'default_value': 'sp', '$description': 'translations.json#/div_font_size_unit', 'platforms': ['android', 'ios']}, 'letter_spacing': {'type': 'number', '$description': 'translations.json#/div_text_range_letter_spacing'}, 'font_weight': {'$ref': 'div-font-weight.json', '$description': 'translations.json#/div_font_weight'}, 'text_color': {'$ref': 'common.json#/color', '$description': 'translations.json#/div_text_color'}, 'underline': {'$ref': 'div-line-style.json', '$description': 'translations.json#/div_text_range_underline'}, 'strike': {'$ref': 'div-line-style.json', '$description': 'translations.json#/div_text_range_strike'}, 'actions': {'type': 'array', 'items': {'$ref': 'div-action.json'}, 'minItems': 1, '$description': 'translations.json#/div_text_range_actions'}, 'line_height': {'$ref': 'common.json#/non_negative_integer', '$description': 'translations.json#/div_text_range_line_height'}, 'top_offset': {'$ref': 'common.json#/non_negative_integer', '$description': 'translations.json#/div_text_range_top_offset'}, 'border': {'$ref': 'div-text-range-border.json', '$description': 'translations.json#/div_text_range_border'}, 'background': {'$ref': 'div-text-range-background.json', '$description': 'translations.json#/div_text_range_background'}, 'text_shadow': {'$ref': 'div-shadow.json', '$description': 'translations.json#/div_text_range_shadow', 'platforms': ['android']}}, 'required': ['start', 'end'], '$description': 'translations.json#/div_text_range'}, 'minItems': 1, '$description': 'translations.json#/div_text_ellipsis_ranges'}, rule='type')
   data__ranges_is_list = isinstance(data__ranges, (list, tuple))
   if data__ranges_is_list:
    data__ranges_len = len(data__ranges)
    if data__ranges_len < 1:
     if not (isinstance(data__ranges, str) and '@' in data__ranges):
      raise JsonSchemaValueException("" + (name_prefix or "data") + ".ranges must contain at least 1 items", value=data__ranges, name="" + (name_prefix or "data") + ".ranges", definition={'type': 'array', 'items': {'type': 'object', 'properties': {'start': {'$ref': 'common.json#/non_negative_integer', '$description': 'translations.json#/div_text_range_start'}, 'end': {'$ref': 'common.json#/positive_integer', '$description': 'translations.json#/div_text_range_end'}, 'font_size': {'$ref': 'common.json#/non_negative_integer', '$description': 'translations.json#/div_font_size'}, 'font_family': {'$ref': 'common.json#/non_empty_string', '$description': 'translations.json#/div_font_family'}, 'font_size_unit': {'$ref': 'div-size-unit.json', 'default_value': 'sp', '$description': 'translations.json#/div_font_size_unit', 'platforms': ['android', 'ios']}, 'letter_spacing': {'type': 'number', '$description': 'translations.json#/div_text_range_letter_spacing'}, 'font_weight': {'$ref': 'div-font-weight.json', '$description': 'translations.json#/div_font_weight'}, 'text_color': {'$ref': 'common.json#/color', '$description': 'translations.json#/div_text_color'}, 'underline': {'$ref': 'div-line-style.json', '$description': 'translations.json#/div_text_range_underline'}, 'strike': {'$ref': 'div-line-style.json', '$description': 'translations.json#/div_text_range_strike'}, 'actions': {'type': 'array', 'items': {'$ref': 'div-action.json'}, 'minItems': 1, '$description': 'translations.json#/div_text_range_actions'}, 'line_height': {'$ref': 'common.json#/non_negative_integer', '$description': 'translations.json#/div_text_range_line_height'}, 'top_offset': {'$ref': 'common.json#/non_negative_integer', '$description': 'translations.json#/div_text_range_top_offset'}, 'border': {'$ref': 'div-text-range-border.json', '$description': 'translations.json#/div_text_range_border'}, 'background': {'$ref': 'div-text-range-background.json', '$description': 'translations.json#/div_text_range_background'}, 'text_shadow': {'$ref': 'div-shadow.json', '$description': 'translations.json#/div_text_range_shadow', 'platforms': ['android']}}, 'required': ['start', 'end'], '$description': 'translations.json#/div_text_range'}, 'minItems': 1, '$description': 'translations.json#/div_text_ellipsis_ranges'}, rule='minItems')
    for data__ranges_x, data__ranges_item in enumerate(data__ranges):
     validate_div_text_json__definitions_range(data__ranges_item, custom_formats, (name_prefix or "data") + ".ranges[{data__ranges_x}]".format(**locals()))
  if "images" in data_keys:
   data_keys.remove("images")
   data__images = data["images"]
   if not isinstance(data__images, (list, tuple)):
    if not (isinstance(data__images, str) and '@' in data__images):
     raise JsonSchemaValueException("" + (name_prefix or "data") + ".images must be array", value=data__images, name="" + (name_prefix or "data") + ".images", definition={'type': 'array', 'items': {'type': 'object', 'properties': {'start': {'$ref': 'common.json#/non_negative_integer', '$description': 'translations.json#/div_text_image_start'}, 'url': {'$ref': 'common.json#/url', '$description': 'translations.json#/div_text_image_url'}, 'width': {'$ref': 'div-fixed-size.json', 'default_value': '{"type": "fixed","value":20}', '$description': 'translations.json#/div_text_image_width'}, 'height': {'$ref': 'div-fixed-size.json', 'default_value': '{"type": "fixed","value":20}', '$description': 'translations.json#/div_text_image_height'}, 'tint_color': {'$ref': 'common.json#/color', '$description': 'translations.json#/div_text_image_tint_color'}, 'tint_mode': {'$ref': 'div-blend-mode.json', 'default_value': 'source_in', '$description': 'translations.json#/div_text_image_tint_mode', 'platforms': ['android', 'web']}}, 'required': ['url', 'start'], '$description': 'translations.json#/div_text_image'}, 'minItems': 1, '$description': 'translations.json#/div_text_ellipsis_images'}, rule='type')
   data__images_is_list = isinstance(data__images, (list, tuple))
   if data__images_is_list:
    data__images_len = len(data__images)
    if data__images_len < 1:
     if not (isinstance(data__images, str) and '@' in data__images):
      raise JsonSchemaValueException("" + (name_prefix or "data") + ".images must contain at least 1 items", value=data__images, name="" + (name_prefix or "data") + ".images", definition={'type': 'array', 'items': {'type': 'object', 'properties': {'start': {'$ref': 'common.json#/non_negative_integer', '$description': 'translations.json#/div_text_image_start'}, 'url': {'$ref': 'common.json#/url', '$description': 'translations.json#/div_text_image_url'}, 'width': {'$ref': 'div-fixed-size.json', 'default_value': '{"type": "fixed","value":20}', '$description': 'translations.json#/div_text_image_width'}, 'height': {'$ref': 'div-fixed-size.json', 'default_value': '{"type": "fixed","value":20}', '$description': 'translations.json#/div_text_image_height'}, 'tint_color': {'$ref': 'common.json#/color', '$description': 'translations.json#/div_text_image_tint_color'}, 'tint_mode': {'$ref': 'div-blend-mode.json', 'default_value': 'source_in', '$description': 'translations.json#/div_text_image_tint_mode', 'platforms': ['android', 'web']}}, 'required': ['url', 'start'], '$description': 'translations.json#/div_text_image'}, 'minItems': 1, '$description': 'translations.json#/div_text_ellipsis_images'}, rule='minItems')
    for data__images_x, data__images_item in enumerate(data__images):
     validate_div_text_json__definitions_image(data__images_item, custom_formats, (name_prefix or "data") + ".images[{data__images_x}]".format(**locals()))
 return data

def validate_div_text_json__definitions_image(data, custom_formats={}, name_prefix=None):
 if not isinstance(data, (dict)):
  if not (isinstance(data, str) and '@' in data):
   raise JsonSchemaValueException("" + (name_prefix or "data") + " must be object", value=data, name="" + (name_prefix or "data") + "", definition={'type': 'object', 'properties': {'start': {'type': 'integer', 'constraint': 'number >= 0'}, 'url': {'type': 'string', 'format': 'uri'}, 'width': {'type': 'object', '$description': 'translations.json#/div_fixed_size', 'codegen': {'divan': {'forced_properties_order': ['value']}}, 'properties': {'value': {'$ref': 'common.json#/non_negative_integer', '$description': 'translations.json#/div_fixed_size_value'}, 'unit': {'$ref': 'div-size-unit.json', '$description': 'translations.json#/div_fixed_size_unit', 'default_value': 'dp'}, 'type': {'type': 'string', 'enum': ['fixed']}}, 'required': ['value', 'type'], '$schema': 'http://json-schema.org/draft-07/schema'}, 'height': {'type': 'object', '$description': 'translations.json#/div_fixed_size', 'codegen': {'divan': {'forced_properties_order': ['value']}}, 'properties': {'value': {'$ref': 'common.json#/non_negative_integer', '$description': 'translations.json#/div_fixed_size_value'}, 'unit': {'$ref': 'div-size-unit.json', '$description': 'translations.json#/div_fixed_size_unit', 'default_value': 'dp'}, 'type': {'type': 'string', 'enum': ['fixed']}}, 'required': ['value', 'type'], '$schema': 'http://json-schema.org/draft-07/schema'}, 'tint_color': {'type': 'string', 'format': 'color'}, 'tint_mode': {'type': 'string', 'enum': ['source_in', 'source_atop', 'darken', 'lighten', 'multiply', 'screen'], '$description': 'translations.json#/div_blend_mode', '$schema': 'http://json-schema.org/draft-07/schema'}}, 'required': ['url', 'start'], '$description': 'translations.json#/div_text_image'}, rule='type')
 data_is_dict = isinstance(data, dict)
 if data_is_dict:
  data__missing_keys = set(['url', 'start']) - data.keys()
  if data__missing_keys:
   if not (isinstance(data, str) and '@' in data):
    raise JsonSchemaValueException("" + (name_prefix or "data") + " must contain " + (str(sorted(data__missing_keys)) + " properties"), value=data, name="" + (name_prefix or "data") + "", definition={'type': 'object', 'properties': {'start': {'type': 'integer', 'constraint': 'number >= 0'}, 'url': {'type': 'string', 'format': 'uri'}, 'width': {'type': 'object', '$description': 'translations.json#/div_fixed_size', 'codegen': {'divan': {'forced_properties_order': ['value']}}, 'properties': {'value': {'$ref': 'common.json#/non_negative_integer', '$description': 'translations.json#/div_fixed_size_value'}, 'unit': {'$ref': 'div-size-unit.json', '$description': 'translations.json#/div_fixed_size_unit', 'default_value': 'dp'}, 'type': {'type': 'string', 'enum': ['fixed']}}, 'required': ['value', 'type'], '$schema': 'http://json-schema.org/draft-07/schema'}, 'height': {'type': 'object', '$description': 'translations.json#/div_fixed_size', 'codegen': {'divan': {'forced_properties_order': ['value']}}, 'properties': {'value': {'$ref': 'common.json#/non_negative_integer', '$description': 'translations.json#/div_fixed_size_value'}, 'unit': {'$ref': 'div-size-unit.json', '$description': 'translations.json#/div_fixed_size_unit', 'default_value': 'dp'}, 'type': {'type': 'string', 'enum': ['fixed']}}, 'required': ['value', 'type'], '$schema': 'http://json-schema.org/draft-07/schema'}, 'tint_color': {'type': 'string', 'format': 'color'}, 'tint_mode': {'type': 'string', 'enum': ['source_in', 'source_atop', 'darken', 'lighten', 'multiply', 'screen'], '$description': 'translations.json#/div_blend_mode', '$schema': 'http://json-schema.org/draft-07/schema'}}, 'required': ['url', 'start'], '$description': 'translations.json#/div_text_image'}, rule='required')
  data_keys = set(data.keys())
  if "start" in data_keys:
   data_keys.remove("start")
   data__start = data["start"]
   validate_common_json__non_negative_integer(data__start, custom_formats, (name_prefix or "data") + ".start")
  if "url" in data_keys:
   data_keys.remove("url")
   data__url = data["url"]
   validate_common_json__url(data__url, custom_formats, (name_prefix or "data") + ".url")
  if "width" in data_keys:
   data_keys.remove("width")
   data__width = data["width"]
   validate_div_fixed_size_json(data__width, custom_formats, (name_prefix or "data") + ".width")
  if "height" in data_keys:
   data_keys.remove("height")
   data__height = data["height"]
   validate_div_fixed_size_json(data__height, custom_formats, (name_prefix or "data") + ".height")
  if "tint_color" in data_keys:
   data_keys.remove("tint_color")
   data__tintcolor = data["tint_color"]
   validate_common_json__color(data__tintcolor, custom_formats, (name_prefix or "data") + ".tint_color")
  if "tint_mode" in data_keys:
   data_keys.remove("tint_mode")
   data__tintmode = data["tint_mode"]
   validate_div_blend_mode_json(data__tintmode, custom_formats, (name_prefix or "data") + ".tint_mode")
 return data

def validate_div_blend_mode_json(data, custom_formats={}, name_prefix=None):
 if not isinstance(data, (str)):
  if not (isinstance(data, str) and '@' in data):
   raise JsonSchemaValueException("" + (name_prefix or "data") + " must be string", value=data, name="" + (name_prefix or "data") + "", definition={'type': 'string', 'enum': ['source_in', 'source_atop', 'darken', 'lighten', 'multiply', 'screen'], '$description': 'translations.json#/div_blend_mode', '$schema': 'http://json-schema.org/draft-07/schema'}, rule='type')
 if data not in ['source_in', 'source_atop', 'darken', 'lighten', 'multiply', 'screen']:
  if not (isinstance(data, str) and '@' in data):
   raise JsonSchemaValueException("" + (name_prefix or "data") + " must be one of ['source_in', 'source_atop', 'darken', 'lighten', 'multiply', 'screen']", value=data, name="" + (name_prefix or "data") + "", definition={'type': 'string', 'enum': ['source_in', 'source_atop', 'darken', 'lighten', 'multiply', 'screen'], '$description': 'translations.json#/div_blend_mode', '$schema': 'http://json-schema.org/draft-07/schema'}, rule='enum')
 return data

def validate_div_text_json__definitions_range(data, custom_formats={}, name_prefix=None):
 if not isinstance(data, (dict)):
  if not (isinstance(data, str) and '@' in data):
   raise JsonSchemaValueException("" + (name_prefix or "data") + " must be object", value=data, name="" + (name_prefix or "data") + "", definition={'type': 'object', 'properties': {'start': {'type': 'integer', 'constraint': 'number >= 0'}, 'end': {'type': 'integer', 'constraint': 'number > 0'}, 'font_size': {'type': 'integer', 'constraint': 'number >= 0'}, 'font_family': {'type': 'string', 'minLength': 1, 'clientMinLength': 1}, 'font_size_unit': {'type': 'string', 'enum': ['dp', 'sp', 'px'], '$description': 'translations.json#/div_size_unit', 'platforms': ['android', 'ios'], '$schema': 'http://json-schema.org/draft-07/schema'}, 'letter_spacing': {'type': 'number', '$description': 'translations.json#/div_text_range_letter_spacing'}, 'font_weight': {'type': 'string', 'enum': ['light', 'medium', 'regular', 'bold'], '$schema': 'http://json-schema.org/draft-07/schema'}, 'text_color': {'type': 'string', 'format': 'color'}, 'underline': {'type': 'string', '$description': 'translations.json#/div_line_style', 'enum': ['none', 'single'], '$schema': 'http://json-schema.org/draft-07/schema'}, 'strike': {'type': 'string', '$description': 'translations.json#/div_line_style', 'enum': ['none', 'single'], '$schema': 'http://json-schema.org/draft-07/schema'}, 'actions': {'type': 'array', 'items': {'definitions': {'menu_item': {'type': 'object', 'properties': {'text': {'$ref': 'common.json#/non_empty_string', '$description': 'translations.json#/div_action_menu_item_text'}, 'action': {'$ref': 'div-action.json', '$description': 'translations.json#/div_action_menu_item_action'}, 'actions': {'type': 'array', 'items': {'$ref': 'div-action.json'}, 'minItems': 1, '$description': 'translations.json#/div_action_menu_item_actions'}}, 'required': ['text']}}, 'allOf': [{'$ref': 'div-action-base.json'}, {'type': 'object', '$description': 'translations.json#/div_action', 'properties': {'menu_items': {'type': 'array', 'items': {'$ref': '#/definitions/menu_item'}, '$description': 'translations.json#/div_action_menu_items', 'platforms': ['android', 'ios']}, 'log_url': {'$ref': 'common.json#/url', '$description': 'translations.json#/div_action_log_url'}, 'target': {'type': 'string', 'enum': ['_self', '_blank'], 'force_enum_field': True, '$description': 'translations.json#/div_action_target', 'platforms': ['web'], 'code_generation_disabled_swift': True}}, 'required': ['log_id']}], '$schema': 'http://json-schema.org/draft-07/schema'}, 'minItems': 1, '$description': 'translations.json#/div_text_range_actions'}, 'line_height': {'type': 'integer', 'constraint': 'number >= 0'}, 'top_offset': {'type': 'integer', 'constraint': 'number >= 0'}, 'border': {'type': 'object', '$description': 'translations.json#/div_text_range_border', 'properties': {'stroke': {'$ref': 'div-stroke.json', '$description': 'translations.json#/div_border_stroke'}, 'corner_radius': {'$ref': 'common.json#/non_negative_integer', '$description': 'translations.json#/div_border_corner_radius'}}, '$schema': 'http://json-schema.org/draft-07/schema'}, 'background': {'anyOf': [{'$ref': 'div-solid-background.json', '$description': 'translations.json#/div_background_solid'}], '$schema': 'http://json-schema.org/draft-07/schema'}, 'text_shadow': {'type': 'object', '$description': 'translations.json#/div_shadow', 'properties': {'color': {'$ref': 'common.json#/color', '$description': 'translations.json#/div_shadow_color', 'default_value': '#000000'}, 'offset': {'$ref': 'div-point.json', '$description': 'translations.json#/div_shadow_offset'}, 'blur': {'$ref': 'common.json#/non_negative_integer', '$description': 'translations.json#/div_shadow_blur', 'default_value': '2'}, 'alpha': {'type': 'number', 'default_value': '0.19', 'constraint': 'number >= 0.0 && number <= 1.0', '$description': 'translations.json#/div_shadow_alpha'}}, 'required': ['offset'], '$schema': 'http://json-schema.org/draft-07/schema'}}, 'required': ['start', 'end'], '$description': 'translations.json#/div_text_range'}, rule='type')
 data_is_dict = isinstance(data, dict)
 if data_is_dict:
  data__missing_keys = set(['start', 'end']) - data.keys()
  if data__missing_keys:
   if not (isinstance(data, str) and '@' in data):
    raise JsonSchemaValueException("" + (name_prefix or "data") + " must contain " + (str(sorted(data__missing_keys)) + " properties"), value=data, name="" + (name_prefix or "data") + "", definition={'type': 'object', 'properties': {'start': {'type': 'integer', 'constraint': 'number >= 0'}, 'end': {'type': 'integer', 'constraint': 'number > 0'}, 'font_size': {'type': 'integer', 'constraint': 'number >= 0'}, 'font_family': {'type': 'string', 'minLength': 1, 'clientMinLength': 1}, 'font_size_unit': {'type': 'string', 'enum': ['dp', 'sp', 'px'], '$description': 'translations.json#/div_size_unit', 'platforms': ['android', 'ios'], '$schema': 'http://json-schema.org/draft-07/schema'}, 'letter_spacing': {'type': 'number', '$description': 'translations.json#/div_text_range_letter_spacing'}, 'font_weight': {'type': 'string', 'enum': ['light', 'medium', 'regular', 'bold'], '$schema': 'http://json-schema.org/draft-07/schema'}, 'text_color': {'type': 'string', 'format': 'color'}, 'underline': {'type': 'string', '$description': 'translations.json#/div_line_style', 'enum': ['none', 'single'], '$schema': 'http://json-schema.org/draft-07/schema'}, 'strike': {'type': 'string', '$description': 'translations.json#/div_line_style', 'enum': ['none', 'single'], '$schema': 'http://json-schema.org/draft-07/schema'}, 'actions': {'type': 'array', 'items': {'definitions': {'menu_item': {'type': 'object', 'properties': {'text': {'$ref': 'common.json#/non_empty_string', '$description': 'translations.json#/div_action_menu_item_text'}, 'action': {'$ref': 'div-action.json', '$description': 'translations.json#/div_action_menu_item_action'}, 'actions': {'type': 'array', 'items': {'$ref': 'div-action.json'}, 'minItems': 1, '$description': 'translations.json#/div_action_menu_item_actions'}}, 'required': ['text']}}, 'allOf': [{'$ref': 'div-action-base.json'}, {'type': 'object', '$description': 'translations.json#/div_action', 'properties': {'menu_items': {'type': 'array', 'items': {'$ref': '#/definitions/menu_item'}, '$description': 'translations.json#/div_action_menu_items', 'platforms': ['android', 'ios']}, 'log_url': {'$ref': 'common.json#/url', '$description': 'translations.json#/div_action_log_url'}, 'target': {'type': 'string', 'enum': ['_self', '_blank'], 'force_enum_field': True, '$description': 'translations.json#/div_action_target', 'platforms': ['web'], 'code_generation_disabled_swift': True}}, 'required': ['log_id']}], '$schema': 'http://json-schema.org/draft-07/schema'}, 'minItems': 1, '$description': 'translations.json#/div_text_range_actions'}, 'line_height': {'type': 'integer', 'constraint': 'number >= 0'}, 'top_offset': {'type': 'integer', 'constraint': 'number >= 0'}, 'border': {'type': 'object', '$description': 'translations.json#/div_text_range_border', 'properties': {'stroke': {'$ref': 'div-stroke.json', '$description': 'translations.json#/div_border_stroke'}, 'corner_radius': {'$ref': 'common.json#/non_negative_integer', '$description': 'translations.json#/div_border_corner_radius'}}, '$schema': 'http://json-schema.org/draft-07/schema'}, 'background': {'anyOf': [{'$ref': 'div-solid-background.json', '$description': 'translations.json#/div_background_solid'}], '$schema': 'http://json-schema.org/draft-07/schema'}, 'text_shadow': {'type': 'object', '$description': 'translations.json#/div_shadow', 'properties': {'color': {'$ref': 'common.json#/color', '$description': 'translations.json#/div_shadow_color', 'default_value': '#000000'}, 'offset': {'$ref': 'div-point.json', '$description': 'translations.json#/div_shadow_offset'}, 'blur': {'$ref': 'common.json#/non_negative_integer', '$description': 'translations.json#/div_shadow_blur', 'default_value': '2'}, 'alpha': {'type': 'number', 'default_value': '0.19', 'constraint': 'number >= 0.0 && number <= 1.0', '$description': 'translations.json#/div_shadow_alpha'}}, 'required': ['offset'], '$schema': 'http://json-schema.org/draft-07/schema'}}, 'required': ['start', 'end'], '$description': 'translations.json#/div_text_range'}, rule='required')
  data_keys = set(data.keys())
  if "start" in data_keys:
   data_keys.remove("start")
   data__start = data["start"]
   validate_common_json__non_negative_integer(data__start, custom_formats, (name_prefix or "data") + ".start")
  if "end" in data_keys:
   data_keys.remove("end")
   data__end = data["end"]
   validate_common_json__positive_integer(data__end, custom_formats, (name_prefix or "data") + ".end")
  if "font_size" in data_keys:
   data_keys.remove("font_size")
   data__fontsize = data["font_size"]
   validate_common_json__non_negative_integer(data__fontsize, custom_formats, (name_prefix or "data") + ".font_size")
  if "font_family" in data_keys:
   data_keys.remove("font_family")
   data__fontfamily = data["font_family"]
   validate_common_json__non_empty_string(data__fontfamily, custom_formats, (name_prefix or "data") + ".font_family")
  if "font_size_unit" in data_keys:
   data_keys.remove("font_size_unit")
   data__fontsizeunit = data["font_size_unit"]
   validate_div_size_unit_json(data__fontsizeunit, custom_formats, (name_prefix or "data") + ".font_size_unit")
  if "letter_spacing" in data_keys:
   data_keys.remove("letter_spacing")
   data__letterspacing = data["letter_spacing"]
   if not isinstance(data__letterspacing, (int, float, Decimal)) or isinstance(data__letterspacing, bool):
    if not (isinstance(data__letterspacing, str) and '@' in data__letterspacing):
     raise JsonSchemaValueException("" + (name_prefix or "data") + ".letter_spacing must be number", value=data__letterspacing, name="" + (name_prefix or "data") + ".letter_spacing", definition={'type': 'number', '$description': 'translations.json#/div_text_range_letter_spacing'}, rule='type')
  if "font_weight" in data_keys:
   data_keys.remove("font_weight")
   data__fontweight = data["font_weight"]
   validate_div_font_weight_json(data__fontweight, custom_formats, (name_prefix or "data") + ".font_weight")
  if "text_color" in data_keys:
   data_keys.remove("text_color")
   data__textcolor = data["text_color"]
   validate_common_json__color(data__textcolor, custom_formats, (name_prefix or "data") + ".text_color")
  if "underline" in data_keys:
   data_keys.remove("underline")
   data__underline = data["underline"]
   validate_div_line_style_json(data__underline, custom_formats, (name_prefix or "data") + ".underline")
  if "strike" in data_keys:
   data_keys.remove("strike")
   data__strike = data["strike"]
   validate_div_line_style_json(data__strike, custom_formats, (name_prefix or "data") + ".strike")
  if "actions" in data_keys:
   data_keys.remove("actions")
   data__actions = data["actions"]
   if not isinstance(data__actions, (list, tuple)):
    if not (isinstance(data__actions, str) and '@' in data__actions):
     raise JsonSchemaValueException("" + (name_prefix or "data") + ".actions must be array", value=data__actions, name="" + (name_prefix or "data") + ".actions", definition={'type': 'array', 'items': {'definitions': {'menu_item': {'type': 'object', 'properties': {'text': {'$ref': 'common.json#/non_empty_string', '$description': 'translations.json#/div_action_menu_item_text'}, 'action': {'$ref': 'div-action.json', '$description': 'translations.json#/div_action_menu_item_action'}, 'actions': {'type': 'array', 'items': {'$ref': 'div-action.json'}, 'minItems': 1, '$description': 'translations.json#/div_action_menu_item_actions'}}, 'required': ['text']}}, 'allOf': [{'$ref': 'div-action-base.json'}, {'type': 'object', '$description': 'translations.json#/div_action', 'properties': {'menu_items': {'type': 'array', 'items': {'$ref': '#/definitions/menu_item'}, '$description': 'translations.json#/div_action_menu_items', 'platforms': ['android', 'ios']}, 'log_url': {'$ref': 'common.json#/url', '$description': 'translations.json#/div_action_log_url'}, 'target': {'type': 'string', 'enum': ['_self', '_blank'], 'force_enum_field': True, '$description': 'translations.json#/div_action_target', 'platforms': ['web'], 'code_generation_disabled_swift': True}}, 'required': ['log_id']}], '$schema': 'http://json-schema.org/draft-07/schema'}, 'minItems': 1, '$description': 'translations.json#/div_text_range_actions'}, rule='type')
   data__actions_is_list = isinstance(data__actions, (list, tuple))
   if data__actions_is_list:
    data__actions_len = len(data__actions)
    if data__actions_len < 1:
     if not (isinstance(data__actions, str) and '@' in data__actions):
      raise JsonSchemaValueException("" + (name_prefix or "data") + ".actions must contain at least 1 items", value=data__actions, name="" + (name_prefix or "data") + ".actions", definition={'type': 'array', 'items': {'definitions': {'menu_item': {'type': 'object', 'properties': {'text': {'$ref': 'common.json#/non_empty_string', '$description': 'translations.json#/div_action_menu_item_text'}, 'action': {'$ref': 'div-action.json', '$description': 'translations.json#/div_action_menu_item_action'}, 'actions': {'type': 'array', 'items': {'$ref': 'div-action.json'}, 'minItems': 1, '$description': 'translations.json#/div_action_menu_item_actions'}}, 'required': ['text']}}, 'allOf': [{'$ref': 'div-action-base.json'}, {'type': 'object', '$description': 'translations.json#/div_action', 'properties': {'menu_items': {'type': 'array', 'items': {'$ref': '#/definitions/menu_item'}, '$description': 'translations.json#/div_action_menu_items', 'platforms': ['android', 'ios']}, 'log_url': {'$ref': 'common.json#/url', '$description': 'translations.json#/div_action_log_url'}, 'target': {'type': 'string', 'enum': ['_self', '_blank'], 'force_enum_field': True, '$description': 'translations.json#/div_action_target', 'platforms': ['web'], 'code_generation_disabled_swift': True}}, 'required': ['log_id']}], '$schema': 'http://json-schema.org/draft-07/schema'}, 'minItems': 1, '$description': 'translations.json#/div_text_range_actions'}, rule='minItems')
    for data__actions_x, data__actions_item in enumerate(data__actions):
     validate_div_action_json(data__actions_item, custom_formats, (name_prefix or "data") + ".actions[{data__actions_x}]".format(**locals()))
  if "line_height" in data_keys:
   data_keys.remove("line_height")
   data__lineheight = data["line_height"]
   validate_common_json__non_negative_integer(data__lineheight, custom_formats, (name_prefix or "data") + ".line_height")
  if "top_offset" in data_keys:
   data_keys.remove("top_offset")
   data__topoffset = data["top_offset"]
   validate_common_json__non_negative_integer(data__topoffset, custom_formats, (name_prefix or "data") + ".top_offset")
  if "border" in data_keys:
   data_keys.remove("border")
   data__border = data["border"]
   validate_div_text_range_border_json(data__border, custom_formats, (name_prefix or "data") + ".border")
  if "background" in data_keys:
   data_keys.remove("background")
   data__background = data["background"]
   validate_div_text_range_background_json(data__background, custom_formats, (name_prefix or "data") + ".background")
  if "text_shadow" in data_keys:
   data_keys.remove("text_shadow")
   data__textshadow = data["text_shadow"]
   validate_div_shadow_json(data__textshadow, custom_formats, (name_prefix or "data") + ".text_shadow")
 return data

def validate_div_text_range_background_json(data, custom_formats={}, name_prefix=None):
 data_any_of_count21 = 0
 if not data_any_of_count21:
  try:
   validate_div_solid_background_json(data, custom_formats, (name_prefix or "data") + "")
   data_any_of_count21 += 1
  except JsonSchemaValueException: pass
 if not data_any_of_count21:
  if not (isinstance(data, str) and '@' in data):
   raise JsonSchemaValueException("" + (name_prefix or "data") + " cannot be validated by any definition", value=data, name="" + (name_prefix or "data") + "", definition={'anyOf': [{'type': 'object', '$description': 'translations.json#/div_solid_background', 'codegen': {'divan': {'forced_properties_order': ['color']}}, 'properties': {'color': {'$ref': 'common.json#/color', '$description': 'translations.json#/div_solid_background_color'}, 'type': {'type': 'string', 'enum': ['solid']}}, 'required': ['color', 'type'], '$schema': 'http://json-schema.org/draft-07/schema'}], '$schema': 'http://json-schema.org/draft-07/schema'}, rule='anyOf')
 return data

def validate_div_text_range_border_json(data, custom_formats={}, name_prefix=None):
 if not isinstance(data, (dict)):
  if not (isinstance(data, str) and '@' in data):
   raise JsonSchemaValueException("" + (name_prefix or "data") + " must be object", value=data, name="" + (name_prefix or "data") + "", definition={'type': 'object', '$description': 'translations.json#/div_text_range_border', 'properties': {'stroke': {'type': 'object', '$description': 'translations.json#/div_stroke', 'properties': {'width': {'$ref': 'common.json#/non_negative_integer', 'default_value': '1', '$description': 'translations.json#/div_stroke_width'}, 'color': {'$ref': 'common.json#/color', '$description': 'translations.json#/div_stroke_color'}, 'unit': {'$ref': 'div-size-unit.json', 'default_value': 'dp'}}, 'required': ['color'], '$schema': 'http://json-schema.org/draft-07/schema'}, 'corner_radius': {'type': 'integer', 'constraint': 'number >= 0'}}, '$schema': 'http://json-schema.org/draft-07/schema'}, rule='type')
 data_is_dict = isinstance(data, dict)
 if data_is_dict:
  data_keys = set(data.keys())
  if "stroke" in data_keys:
   data_keys.remove("stroke")
   data__stroke = data["stroke"]
   validate_div_stroke_json(data__stroke, custom_formats, (name_prefix or "data") + ".stroke")
  if "corner_radius" in data_keys:
   data_keys.remove("corner_radius")
   data__cornerradius = data["corner_radius"]
   validate_common_json__non_negative_integer(data__cornerradius, custom_formats, (name_prefix or "data") + ".corner_radius")
 return data

def validate_div_line_style_json(data, custom_formats={}, name_prefix=None):
 if not isinstance(data, (str)):
  if not (isinstance(data, str) and '@' in data):
   raise JsonSchemaValueException("" + (name_prefix or "data") + " must be string", value=data, name="" + (name_prefix or "data") + "", definition={'type': 'string', '$description': 'translations.json#/div_line_style', 'enum': ['none', 'single'], '$schema': 'http://json-schema.org/draft-07/schema'}, rule='type')
 if data not in ['none', 'single']:
  if not (isinstance(data, str) and '@' in data):
   raise JsonSchemaValueException("" + (name_prefix or "data") + " must be one of ['none', 'single']", value=data, name="" + (name_prefix or "data") + "", definition={'type': 'string', '$description': 'translations.json#/div_line_style', 'enum': ['none', 'single'], '$schema': 'http://json-schema.org/draft-07/schema'}, rule='enum')
 return data

def validate_div_text_gradient_json(data, custom_formats={}, name_prefix=None):
 data_any_of_count22 = 0
 if not data_any_of_count22:
  try:
   validate_div_linear_gradient_json(data, custom_formats, (name_prefix or "data") + "")
   data_any_of_count22 += 1
  except JsonSchemaValueException: pass
 if not data_any_of_count22:
  try:
   validate_div_radial_gradient_json(data, custom_formats, (name_prefix or "data") + "")
   data_any_of_count22 += 1
  except JsonSchemaValueException: pass
 if not data_any_of_count22:
  if not (isinstance(data, str) and '@' in data):
   raise JsonSchemaValueException("" + (name_prefix or "data") + " cannot be validated by any definition", value=data, name="" + (name_prefix or "data") + "", definition={'anyOf': [{'type': 'object', '$description': 'translations.json#/div_gradient_linear', 'properties': {'colors': {'type': 'array', 'items': {'$ref': 'common.json#/color'}, 'minItems': 2, '$description': 'translations.json#/div_gradient_colors'}, 'angle': {'type': 'integer', 'constraint': 'number >= 0 && number <= 360', 'default_value': '0', '$description': 'translations.json#/div_gradient_linear_angle'}, 'type': {'type': 'string', 'enum': ['gradient']}}, 'required': ['colors', 'type'], '$schema': 'http://json-schema.org/draft-07/schema'}, {'type': 'object', '$description': 'translations.json#/div_gradient_radial', 'properties': {'colors': {'type': 'array', 'items': {'$ref': 'common.json#/color'}, 'minItems': 2, '$description': 'translations.json#/div_gradient_colors'}, 'radius': {'$ref': 'div-radial-gradient-radius.json', 'default_value': '{"type": "relative", "value": "farthest_corner" }', '$description': 'translations.json#/div_gradient_radial_radius'}, 'center_x': {'$ref': 'div-radial-gradient-center.json', 'default_value': '{"type": "relative", "value": 0.5 }', '$description': 'translations.json#/div_gradient_radial_center_x'}, 'center_y': {'$ref': 'div-radial-gradient-center.json', 'default_value': '{"type": "relative", "value": 0.5 }', '$description': 'translations.json#/div_gradient_radial_center_y'}, 'type': {'type': 'string', 'enum': ['radial_gradient']}}, 'required': ['colors', 'type'], '$schema': 'http://json-schema.org/draft-07/schema'}], '$schema': 'http://json-schema.org/draft-07/schema'}, rule='anyOf')
 return data

def validate_div_gif_image_json(data, custom_formats={}, name_prefix=None):
 validate_div_base_json(data, custom_formats, (name_prefix or "data") + "")
 validate_div_actionable_json(data, custom_formats, (name_prefix or "data") + "")
 validate_div_image_base_json(data, custom_formats, (name_prefix or "data") + "")
 data_is_dict = isinstance(data, dict)
 if data_is_dict:
  data_keys = set(data.keys())
  if "gif_url" in data_keys:
   data_keys.remove("gif_url")
   data__gifurl = data["gif_url"]
   validate_common_json__url(data__gifurl, custom_formats, (name_prefix or "data") + ".gif_url")
  if "type" in data_keys:
   data_keys.remove("type")
   data__type = data["type"]
   if not isinstance(data__type, (str)):
    if not (isinstance(data__type, str) and '@' in data__type):
     raise JsonSchemaValueException("" + (name_prefix or "data") + ".type must be string", value=data__type, name="" + (name_prefix or "data") + ".type", definition={'type': 'string', 'enum': ['gif']}, rule='type')
   if data__type not in ['gif']:
    if not (isinstance(data__type, str) and '@' in data__type):
     raise JsonSchemaValueException("" + (name_prefix or "data") + ".type must be one of ['gif']", value=data__type, name="" + (name_prefix or "data") + ".type", definition={'type': 'string', 'enum': ['gif']}, rule='enum')
 data_is_dict = isinstance(data, dict)
 if data_is_dict:
  data__missing_keys = set(['gif_url', 'type']) - data.keys()
  if data__missing_keys:
   if not (isinstance(data, str) and '@' in data):
    raise JsonSchemaValueException("" + (name_prefix or "data") + " must contain " + (str(sorted(data__missing_keys)) + " properties"), value=data, name="" + (name_prefix or "data") + "", definition={'java_extends': 'DivBlockWithId', '$description': 'translations.json#/div_gif_image', 'allOf': [{'protocol_name': 'div-base', 'codegen': {'swift': {'super_protocol': 'DivBlockModeling'}, 'documentation': {'include_in_toc': True}}, 'type': 'object', 'properties': {'id': {'$ref': 'common.json#/non_empty_string', 'supports_expressions': False, '$description': 'translations.json#/div_base_id'}, 'border': {'$ref': 'div-border.json', '$description': 'translations.json#/div_base_border'}, 'width': {'$ref': 'div-size.json', 'default_value': '{"type": "match_parent"}', '$description': 'translations.json#/div_base_width'}, 'height': {'$ref': 'div-size.json', 'default_value': '{"type": "wrap_content"}', '$description': 'translations.json#/div_base_height'}, 'background': {'type': 'array', 'items': {'$ref': 'div-background.json'}, 'minItems': 1, '$description': 'translations.json#/div_base_background'}, 'paddings': {'$ref': 'div-edge-insets.json', '$description': 'translations.json#/div_base_paddings'}, 'margins': {'$ref': 'div-edge-insets.json', '$description': 'translations.json#/div_base_margins'}, 'alpha': {'type': 'number', 'default_value': '1.0', 'constraint': 'number >= 0.0 && number <= 1.0', '$description': 'translations.json#/div_base_alpha'}, 'alignment_vertical': {'$ref': 'div-alignment-vertical.json', '$description': 'translations.json#/div_base_alignment_vertical'}, 'alignment_horizontal': {'$ref': 'div-alignment-horizontal.json', '$description': 'translations.json#/div_base_alignment_horizontal'}, 'row_span': {'$ref': 'common.json#/non_negative_integer', '$description': 'translations.json#/div_base_row_span'}, 'column_span': {'$ref': 'common.json#/non_negative_integer', '$description': 'translations.json#/div_base_column_span'}, 'visibility_action': {'$ref': 'div-visibility-action.json', '$description': 'translations.json#/div_base_visibility_action'}, 'visibility_actions': {'type': 'array', 'items': {'$ref': 'div-visibility-action.json'}, 'minItems': 1, '$description': 'translations.json#/div_base_visibility_actions'}, 'disappear_actions': {'type': 'array', 'items': {'$ref': 'div-disappear-action.json'}, 'minItems': 1, '$description': 'translations.json#/div_base_disappear_actions'}, 'tooltips': {'type': 'array', 'items': {'$ref': 'div-tooltip.json'}, 'minItems': 1, '$description': 'translations.json#/div_base_tooltips'}, 'accessibility': {'$ref': 'div-accessibility.json', '$description': 'translations.json#/div_base_accessibility'}, 'extensions': {'type': 'array', 'items': {'$ref': 'div-extension.json'}, 'minItems': 1, '$description': 'translations.json#/div_base_extensions'}, 'transition_triggers': {'type': 'array', 'items': {'$ref': 'div-transition-trigger.json'}, 'minItems': 1, 'supports_expressions': False, '$description': 'translations.json#/div_base_transition_triggers'}, 'transition_in': {'$ref': 'div-appearance-transition.json', '$description': 'translations.json#/div_base_transition_in'}, 'transition_change': {'$ref': 'div-change-transition.json', '$description': 'translations.json#/div_base_transition_change'}, 'transition_out': {'$ref': 'div-appearance-transition.json', '$description': 'translations.json#/div_base_transition_out'}, 'selected_actions': {'type': 'array', 'items': {'$ref': 'div-action.json'}, 'minItems': 1, '$description': 'translations.json#/div_base_selected_actions'}, 'focus': {'$ref': 'div-focus.json', '$description': 'translations.json#/div_base_focus', 'platforms': ['android', 'ios']}, 'visibility': {'$ref': 'div-visibility.json', '$description': 'translations.json#/div_base_visibility', 'default_value': 'visible'}, 'transform': {'$ref': 'div-transform.json', '$description': 'translations.json#/div_base_transform'}}, '$schema': 'http://json-schema.org/draft-07/schema'}, {'properties': {'action': {'$ref': 'div-action.json', '$description': 'translations.json#/div_actionable_action'}, 'actions': {'type': 'array', 'items': {'$ref': 'div-action.json'}, 'minItems': 1, '$description': 'translations.json#/div_actionable_actions'}, 'longtap_actions': {'type': 'array', 'items': {'$ref': 'div-action.json'}, 'minItems': 1, '$description': 'translations.json#/div_actionable_longtap_actions'}, 'doubletap_actions': {'type': 'array', 'items': {'$ref': 'div-action.json'}, 'minItems': 1, '$description': 'translations.json#/div_actionable_doubletap_actions'}, 'action_animation': {'$ref': 'div-animation.json', 'default_value': '{"name": "fade", "start_value": 1, "end_value": 0.6, "duration": 100 }', '$description': 'translations.json#/div_actionable_action_animation'}}, '$schema': 'http://json-schema.org/draft-07/schema'}, {'properties': {'placeholder_color': {'$ref': 'common.json#/color', 'default_value': '#14000000', '$description': 'translations.json#/div_image_base_placeholder_color'}, 'scale': {'$ref': 'div-image-scale.json', 'default_value': 'fill', '$description': 'translations.json#/div_image_base_scale'}, 'content_alignment_vertical': {'$ref': 'div-alignment-vertical.json', 'default_value': 'center', '$description': 'translations.json#/div_image_base_content_alignment_vertical'}, 'content_alignment_horizontal': {'$ref': 'div-alignment-horizontal.json', 'default_value': 'center', '$description': 'translations.json#/div_image_base_content_alignment_horizontal'}, 'preview': {'$ref': 'common.json#/non_empty_string', '$description': 'translations.json#/div_image_base_preview'}, 'preload_required': {'$ref': 'common.json#/boolean_int', 'default_value': 'false', '$description': 'translations.json#/div_image_base_preload_required', 'platforms': ['android']}, 'aspect': {'$ref': 'div-aspect.json', '$description': 'translations.json#/div_aspect'}}, '$schema': 'http://json-schema.org/draft-07/schema'}, {'properties': {'gif_url': {'type': 'string', 'format': 'uri'}, 'type': {'type': 'string', 'enum': ['gif']}}}], 'required': ['gif_url', 'type'], '$schema': 'http://json-schema.org/draft-07/schema'}, rule='required')
 return data

def validate_div_image_base_json(data, custom_formats={}, name_prefix=None):
 data_is_dict = isinstance(data, dict)
 if data_is_dict:
  data_keys = set(data.keys())
  if "placeholder_color" in data_keys:
   data_keys.remove("placeholder_color")
   data__placeholdercolor = data["placeholder_color"]
   validate_common_json__color(data__placeholdercolor, custom_formats, (name_prefix or "data") + ".placeholder_color")
  if "scale" in data_keys:
   data_keys.remove("scale")
   data__scale = data["scale"]
   validate_div_image_scale_json(data__scale, custom_formats, (name_prefix or "data") + ".scale")
  if "content_alignment_vertical" in data_keys:
   data_keys.remove("content_alignment_vertical")
   data__contentalignmentvertical = data["content_alignment_vertical"]
   validate_div_alignment_vertical_json(data__contentalignmentvertical, custom_formats, (name_prefix or "data") + ".content_alignment_vertical")
  if "content_alignment_horizontal" in data_keys:
   data_keys.remove("content_alignment_horizontal")
   data__contentalignmenthorizontal = data["content_alignment_horizontal"]
   validate_div_alignment_horizontal_json(data__contentalignmenthorizontal, custom_formats, (name_prefix or "data") + ".content_alignment_horizontal")
  if "preview" in data_keys:
   data_keys.remove("preview")
   data__preview = data["preview"]
   validate_common_json__non_empty_string(data__preview, custom_formats, (name_prefix or "data") + ".preview")
  if "preload_required" in data_keys:
   data_keys.remove("preload_required")
   data__preloadrequired = data["preload_required"]
   validate_common_json__boolean_int(data__preloadrequired, custom_formats, (name_prefix or "data") + ".preload_required")
  if "aspect" in data_keys:
   data_keys.remove("aspect")
   data__aspect = data["aspect"]
   validate_div_aspect_json(data__aspect, custom_formats, (name_prefix or "data") + ".aspect")
 return data

def validate_div_image_json(data, custom_formats={}, name_prefix=None):
 validate_div_base_json(data, custom_formats, (name_prefix or "data") + "")
 validate_div_actionable_json(data, custom_formats, (name_prefix or "data") + "")
 validate_div_image_base_json(data, custom_formats, (name_prefix or "data") + "")
 data_is_dict = isinstance(data, dict)
 if data_is_dict:
  data_keys = set(data.keys())
  if "image_url" in data_keys:
   data_keys.remove("image_url")
   data__imageurl = data["image_url"]
   validate_common_json__url(data__imageurl, custom_formats, (name_prefix or "data") + ".image_url")
  if "high_priority_preview_show" in data_keys:
   data_keys.remove("high_priority_preview_show")
   data__highprioritypreviewshow = data["high_priority_preview_show"]
   validate_common_json__boolean_int(data__highprioritypreviewshow, custom_formats, (name_prefix or "data") + ".high_priority_preview_show")
  if "type" in data_keys:
   data_keys.remove("type")
   data__type = data["type"]
   if not isinstance(data__type, (str)):
    if not (isinstance(data__type, str) and '@' in data__type):
     raise JsonSchemaValueException("" + (name_prefix or "data") + ".type must be string", value=data__type, name="" + (name_prefix or "data") + ".type", definition={'type': 'string', 'enum': ['image']}, rule='type')
   if data__type not in ['image']:
    if not (isinstance(data__type, str) and '@' in data__type):
     raise JsonSchemaValueException("" + (name_prefix or "data") + ".type must be one of ['image']", value=data__type, name="" + (name_prefix or "data") + ".type", definition={'type': 'string', 'enum': ['image']}, rule='enum')
  if "tint_mode" in data_keys:
   data_keys.remove("tint_mode")
   data__tintmode = data["tint_mode"]
   validate_div_blend_mode_json(data__tintmode, custom_formats, (name_prefix or "data") + ".tint_mode")
  if "tint_color" in data_keys:
   data_keys.remove("tint_color")
   data__tintcolor = data["tint_color"]
   validate_common_json__color(data__tintcolor, custom_formats, (name_prefix or "data") + ".tint_color")
  if "appearance_animation" in data_keys:
   data_keys.remove("appearance_animation")
   data__appearanceanimation = data["appearance_animation"]
   validate_div_fade_transition_json(data__appearanceanimation, custom_formats, (name_prefix or "data") + ".appearance_animation")
  if "filters" in data_keys:
   data_keys.remove("filters")
   data__filters = data["filters"]
   if not isinstance(data__filters, (list, tuple)):
    if not (isinstance(data__filters, str) and '@' in data__filters):
     raise JsonSchemaValueException("" + (name_prefix or "data") + ".filters must be array", value=data__filters, name="" + (name_prefix or "data") + ".filters", definition={'type': 'array', 'items': {'anyOf': [{'$ref': 'div-blur.json', '$description': 'translations.json#/div_filter'}, {'$ref': 'div-filter-rtl-mirror.json', '$description': 'translations.json#/div_filter_rtl_mirror', 'platforms': ['android']}], '$schema': 'http://json-schema.org/draft-07/schema'}, 'minItems': 1, '$description': 'translations.json#/div_filter'}, rule='type')
   data__filters_is_list = isinstance(data__filters, (list, tuple))
   if data__filters_is_list:
    data__filters_len = len(data__filters)
    if data__filters_len < 1:
     if not (isinstance(data__filters, str) and '@' in data__filters):
      raise JsonSchemaValueException("" + (name_prefix or "data") + ".filters must contain at least 1 items", value=data__filters, name="" + (name_prefix or "data") + ".filters", definition={'type': 'array', 'items': {'anyOf': [{'$ref': 'div-blur.json', '$description': 'translations.json#/div_filter'}, {'$ref': 'div-filter-rtl-mirror.json', '$description': 'translations.json#/div_filter_rtl_mirror', 'platforms': ['android']}], '$schema': 'http://json-schema.org/draft-07/schema'}, 'minItems': 1, '$description': 'translations.json#/div_filter'}, rule='minItems')
    for data__filters_x, data__filters_item in enumerate(data__filters):
     validate_div_filter_json(data__filters_item, custom_formats, (name_prefix or "data") + ".filters[{data__filters_x}]".format(**locals()))
 data_is_dict = isinstance(data, dict)
 if data_is_dict:
  data__missing_keys = set(['image_url', 'type']) - data.keys()
  if data__missing_keys:
   if not (isinstance(data, str) and '@' in data):
    raise JsonSchemaValueException("" + (name_prefix or "data") + " must contain " + (str(sorted(data__missing_keys)) + " properties"), value=data, name="" + (name_prefix or "data") + "", definition={'java_extends': 'DivBlockWithId', '$description': 'translations.json#/div_image', 'codegen': {'divan': {'forced_properties_order': ['image_url']}}, 'allOf': [{'protocol_name': 'div-base', 'codegen': {'swift': {'super_protocol': 'DivBlockModeling'}, 'documentation': {'include_in_toc': True}}, 'type': 'object', 'properties': {'id': {'$ref': 'common.json#/non_empty_string', 'supports_expressions': False, '$description': 'translations.json#/div_base_id'}, 'border': {'$ref': 'div-border.json', '$description': 'translations.json#/div_base_border'}, 'width': {'$ref': 'div-size.json', 'default_value': '{"type": "match_parent"}', '$description': 'translations.json#/div_base_width'}, 'height': {'$ref': 'div-size.json', 'default_value': '{"type": "wrap_content"}', '$description': 'translations.json#/div_base_height'}, 'background': {'type': 'array', 'items': {'$ref': 'div-background.json'}, 'minItems': 1, '$description': 'translations.json#/div_base_background'}, 'paddings': {'$ref': 'div-edge-insets.json', '$description': 'translations.json#/div_base_paddings'}, 'margins': {'$ref': 'div-edge-insets.json', '$description': 'translations.json#/div_base_margins'}, 'alpha': {'type': 'number', 'default_value': '1.0', 'constraint': 'number >= 0.0 && number <= 1.0', '$description': 'translations.json#/div_base_alpha'}, 'alignment_vertical': {'$ref': 'div-alignment-vertical.json', '$description': 'translations.json#/div_base_alignment_vertical'}, 'alignment_horizontal': {'$ref': 'div-alignment-horizontal.json', '$description': 'translations.json#/div_base_alignment_horizontal'}, 'row_span': {'$ref': 'common.json#/non_negative_integer', '$description': 'translations.json#/div_base_row_span'}, 'column_span': {'$ref': 'common.json#/non_negative_integer', '$description': 'translations.json#/div_base_column_span'}, 'visibility_action': {'$ref': 'div-visibility-action.json', '$description': 'translations.json#/div_base_visibility_action'}, 'visibility_actions': {'type': 'array', 'items': {'$ref': 'div-visibility-action.json'}, 'minItems': 1, '$description': 'translations.json#/div_base_visibility_actions'}, 'disappear_actions': {'type': 'array', 'items': {'$ref': 'div-disappear-action.json'}, 'minItems': 1, '$description': 'translations.json#/div_base_disappear_actions'}, 'tooltips': {'type': 'array', 'items': {'$ref': 'div-tooltip.json'}, 'minItems': 1, '$description': 'translations.json#/div_base_tooltips'}, 'accessibility': {'$ref': 'div-accessibility.json', '$description': 'translations.json#/div_base_accessibility'}, 'extensions': {'type': 'array', 'items': {'$ref': 'div-extension.json'}, 'minItems': 1, '$description': 'translations.json#/div_base_extensions'}, 'transition_triggers': {'type': 'array', 'items': {'$ref': 'div-transition-trigger.json'}, 'minItems': 1, 'supports_expressions': False, '$description': 'translations.json#/div_base_transition_triggers'}, 'transition_in': {'$ref': 'div-appearance-transition.json', '$description': 'translations.json#/div_base_transition_in'}, 'transition_change': {'$ref': 'div-change-transition.json', '$description': 'translations.json#/div_base_transition_change'}, 'transition_out': {'$ref': 'div-appearance-transition.json', '$description': 'translations.json#/div_base_transition_out'}, 'selected_actions': {'type': 'array', 'items': {'$ref': 'div-action.json'}, 'minItems': 1, '$description': 'translations.json#/div_base_selected_actions'}, 'focus': {'$ref': 'div-focus.json', '$description': 'translations.json#/div_base_focus', 'platforms': ['android', 'ios']}, 'visibility': {'$ref': 'div-visibility.json', '$description': 'translations.json#/div_base_visibility', 'default_value': 'visible'}, 'transform': {'$ref': 'div-transform.json', '$description': 'translations.json#/div_base_transform'}}, '$schema': 'http://json-schema.org/draft-07/schema'}, {'properties': {'action': {'$ref': 'div-action.json', '$description': 'translations.json#/div_actionable_action'}, 'actions': {'type': 'array', 'items': {'$ref': 'div-action.json'}, 'minItems': 1, '$description': 'translations.json#/div_actionable_actions'}, 'longtap_actions': {'type': 'array', 'items': {'$ref': 'div-action.json'}, 'minItems': 1, '$description': 'translations.json#/div_actionable_longtap_actions'}, 'doubletap_actions': {'type': 'array', 'items': {'$ref': 'div-action.json'}, 'minItems': 1, '$description': 'translations.json#/div_actionable_doubletap_actions'}, 'action_animation': {'$ref': 'div-animation.json', 'default_value': '{"name": "fade", "start_value": 1, "end_value": 0.6, "duration": 100 }', '$description': 'translations.json#/div_actionable_action_animation'}}, '$schema': 'http://json-schema.org/draft-07/schema'}, {'properties': {'placeholder_color': {'$ref': 'common.json#/color', 'default_value': '#14000000', '$description': 'translations.json#/div_image_base_placeholder_color'}, 'scale': {'$ref': 'div-image-scale.json', 'default_value': 'fill', '$description': 'translations.json#/div_image_base_scale'}, 'content_alignment_vertical': {'$ref': 'div-alignment-vertical.json', 'default_value': 'center', '$description': 'translations.json#/div_image_base_content_alignment_vertical'}, 'content_alignment_horizontal': {'$ref': 'div-alignment-horizontal.json', 'default_value': 'center', '$description': 'translations.json#/div_image_base_content_alignment_horizontal'}, 'preview': {'$ref': 'common.json#/non_empty_string', '$description': 'translations.json#/div_image_base_preview'}, 'preload_required': {'$ref': 'common.json#/boolean_int', 'default_value': 'false', '$description': 'translations.json#/div_image_base_preload_required', 'platforms': ['android']}, 'aspect': {'$ref': 'div-aspect.json', '$description': 'translations.json#/div_aspect'}}, '$schema': 'http://json-schema.org/draft-07/schema'}, {'properties': {'image_url': {'type': 'string', 'format': 'uri'}, 'high_priority_preview_show': {'oneOf': [{'type': 'boolean'}, {'type': 'integer', 'enum': [0, 1]}]}, 'type': {'type': 'string', 'enum': ['image']}, 'tint_mode': {'type': 'string', 'enum': ['source_in', 'source_atop', 'darken', 'lighten', 'multiply', 'screen'], '$description': 'translations.json#/div_blend_mode', '$schema': 'http://json-schema.org/draft-07/schema'}, 'tint_color': {'type': 'string', 'format': 'color'}, 'appearance_animation': {'$description': 'translations.json#/div_fade_transition', 'allOf': [{'$ref': 'div-transition-base.json'}, {'properties': {'type': {'type': 'string', 'enum': ['fade']}, 'alpha': {'type': 'number', 'constraint': 'number >= 0.0 && number <= 1.0', 'default_value': '0.0', '$description': 'translations.json#/div_fade_transition_alpha'}}}], 'required': ['type'], '$schema': 'http://json-schema.org/draft-07/schema'}, 'filters': {'type': 'array', 'items': {'anyOf': [{'$ref': 'div-blur.json', '$description': 'translations.json#/div_filter'}, {'$ref': 'div-filter-rtl-mirror.json', '$description': 'translations.json#/div_filter_rtl_mirror', 'platforms': ['android']}], '$schema': 'http://json-schema.org/draft-07/schema'}, 'minItems': 1, '$description': 'translations.json#/div_filter'}}}], 'required': ['image_url', 'type'], '$schema': 'http://json-schema.org/draft-07/schema'}, rule='required')
 return data
