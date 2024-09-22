from .video import VideoService

write_to_json = VideoService().write_to_json
read_from_json = VideoService().read_from_json

__all__ = ['write_to_json', 'read_from_json']