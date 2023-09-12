from modeltranslation.translator import translator, TranslationOptions
from core.models import *

# Write every model for translation

class ProductTranslationOptions(TranslationOptions):
    fields = ('name', 'content',)


class BlogTranslationOptions(TranslationOptions):
    fields = ('title', 'content', )


class ProductCategoryTranslationOptions(TranslationOptions):
    fields = ('title', )


class BlogCategoryTranslationOptions(TranslationOptions):
    fields = ('title',)


class DiscountProductTranslationOptions(TranslationOptions):
    fields = ('name', 'content',)


class DiscountCategoryTranslationOptions(TranslationOptions):
    fields = ('title',)


class ColorTranslationOptions(TranslationOptions):
    fields = ('title',)


class SizeTranslationOptions(TranslationOptions):
    fields = ('title',)


translator.register(Product, ProductTranslationOptions)
translator.register(Blog, BlogTranslationOptions)
translator.register(ProductCategory, ProductCategoryTranslationOptions)
translator.register(Discount_category, DiscountCategoryTranslationOptions)
translator.register(Discount_Product, DiscountProductTranslationOptions)
translator.register(BlogCategory, BlogCategoryTranslationOptions)
translator.register(Colors, ColorTranslationOptions)
translator.register(Size, SizeTranslationOptions)