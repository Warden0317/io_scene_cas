bl_info = {
    "name": "Total War: Rome CAS format",
    "author": "Warden",
    "version": (0, 0, 1),
    "blender": (2, 80, 0),
    "location": "File > Import/Export",
    "description": "Total War: Rome CAS import/export tools",
    "wiki_url": "https://github.com/Warden0317/io_scene_cas/blob/master/README.md",
    "tracker_url": 'https://github.com/Warden0317/io_scene_cas/issues',
    "category": "Import-Export",
}

import bpy

from bpy.props import (
    CollectionProperty,
    StringProperty,
    BoolProperty,
    FloatProperty,
)

from bpy_extras.io_utils import (
    ImportHelper,
    ExportHelper,
)


class ImportCAS(bpy.types.Operator, ImportHelper):
    bl_idname = "import.cas"
    bl_label = "Import CAS"

    filter_glob: StringProperty(default="*.cas", options={'HIDDEN'})

    def execute(self, context):
        # import os
        from . import cas

        context.window.cursor_set('WAIT')

        print("Import", self.filepath)
        
        import_cas.load(self, context, self.filepath)

        # paths = [
        #     os.path.join(self.directory, name.name)
        #     for name in self.files
        # ]

        # if not paths:
        #     paths.append(self.filepath)

        # for path in paths:
        #     import_ply.load(self, context, path)

        context.window.cursor_set('DEFAULT')

        return {'FINISHED'}


def menu_func_import(self, context):
    self.layout.operator(ImportCAS.bl_idname, text="CAS (.cas)")


classes = {
    ImportCAS,
}

def register():
    for cls in classes:
        bpy.utils.register_class(cls)

    bpy.types.TOPBAR_MT_file_import.append(menu_func_import)


def unregister():
    for cls in classes:
        bpy.utils.unregister_class(cls)

    bpy.types.TOPBAR_MT_file_import.remove(menu_func_import)


if __name__ == "__main__":
    register()