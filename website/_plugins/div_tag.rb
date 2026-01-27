module Jekyll
  class DivTag < Liquid::Block
    def initialize(tag_name, markup, tokens)
      super
      @class = markup.strip
    end

    def render(context)
      content = super
      "<div class=\"#{@class}\">#{Jekyll::Renderer.new(context.registers[:site], {}).convert(content)}</div>"
    end
  end
end

Liquid::Template.register_tag('div_block', Jekyll::DivTag)