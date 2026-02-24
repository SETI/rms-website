module Jekyll
  class DivTag < Liquid::Block
    def initialize(tag_name, markup, tokens)
      super
      @class = markup.strip
    end

    def render(context)
+      site = context.registers[:site]
       content = super
-      converter = site.find_converter_instance(Jekyll::Converters::Markdown)
+      rendered = converter.convert(content)
+      "<div class=\"#{`@class`}\">#{rendered}</div>"    end
  end
end

Liquid::Template.register_tag('div_block', Jekyll::DivTag)