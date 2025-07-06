import asyncio


class Converter:

    @staticmethod
    async def _get_resolution(input_path):
        process = await asyncio.create_subprocess_exec(
            "ffprobe",
            "-v", "error",
            "-select_streams", "v:0",
            "-show_entries", "stream=width,height",
            "-of", "csv=p=0:s=x",
            input_path,
            stdout=asyncio.subprocess.PIPE,
            stderr=asyncio.subprocess.PIPE,
        )
        stdout, _ = await process.communicate()
        resolution = stdout.decode().strip()  # esempio: "1280x720"
        width, height = resolution.split("x")
        print(width, height)
        return width, height

    @staticmethod
    async def webm2mp4(input_path, output_path):
        width, height = await Converter._get_resolution(input_path)

        conversion = await asyncio.create_subprocess_exec(
            "ffmpeg",
            "-y",
            "-i", input_path,
            "-vf", f"scale={width}:{height},setsar=1",
            "-c:v", "libx264",
            "-preset", "fast",
            "-crf", "28",
            "-pix_fmt", "yuv420p",
            "-c:a", "aac",
            "-b:a", "96k",
            "-movflags", "+faststart",
            output_path,
        )
        await conversion.communicate()
        print("let's see if file converted (hopefully)")
        return conversion.returncode



