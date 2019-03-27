# -*- coding: utf-8 -*-
from Products.Five import BrowserView
from plone.app.contenttypes.utils import human_readable_size


class DocumentationView(BrowserView):
    def get_categories(self):
        return self.context.listFolderContents(
            contentFilter={"portal_type": "documentation_category"}
        )

    def get_sections(self, category):
        return category.listFolderContents(
            contentFilter={"portal_type": "documentation_section"}
        )

    def get_files(self, sections):
        return sections.listFolderContents(
            contentFilter={"portal_type": "documentation_file"}
        )

    def get_number_file(self, sections):
        return len(sections.getFolderContents())

    def human_readable_size(self, file):
        return human_readable_size(file.file.getSize())
