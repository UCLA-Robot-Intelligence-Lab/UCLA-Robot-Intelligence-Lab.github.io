<script lang="ts">
	import { useViewportScroll, useTransform, Motion } from "svelte-motion";
	import { cn } from "../lib/utils.js";

	export let images: string[];
	export let className: string | undefined = undefined;

	let gridRef: HTMLDivElement;

	const { scrollYProgress } = useViewportScroll();

	const translateFirst = useTransform(scrollYProgress, [0, 1], [0, -200]);
	const translateSecond = useTransform(scrollYProgress, [0, 1], [0, 200]);
	const translateThird = useTransform(scrollYProgress, [0, 1], [0, -200]);

	const third = Math.ceil(images.length / 3);

	const firstPart = images.slice(0, third);
	const secondPart = images.slice(third, 2 * third);
	const thirdPart = images.slice(2 * third);
</script>

<div
	class={cn("w-full items-start overflow-y-auto", className)}
	bind:this={gridRef}
>
	<div
		class="mx-auto grid max-w-5xl gap-10 px-10 py-40"
		style="display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));"
		bind:this={gridRef}
	>
		<div class="grid gap-10">
			{#each firstPart as el, idx (`grid-1${idx}`)}
				<Motion let:motion style={{ y: translateFirst }}>
					<div use:motion>
						<img
							src={el}
							class="!m-0 h-80 w-full gap-10 rounded-lg object-cover object-left-top !p-0"
							height="400"
							width="400"
							alt="thumbnail"
						/>
					</div>
				</Motion>
			{/each}
		</div>
		<div class="grid gap-10">
			{#each secondPart as el, idx (`grid-2${idx}`)}
				<Motion let:motion style={{ y: translateSecond }}>
					<div use:motion>
						<img
							src={el}
							class="!m-0 h-80 w-full gap-10 rounded-lg object-cover object-left-top !p-0"
							height="400"
							width="400"
							alt="thumbnail"
						/>
					</div>
				</Motion>
			{/each}
		</div>
		<div class="grid gap-10">
			{#each thirdPart as el, idx (`grid-3${idx}`)}
				<Motion let:motion style={{ y: translateThird }}>
					<div use:motion>
						<img
							src={el}
							class="!m-0 h-80 w-full gap-10 rounded-lg object-cover object-left-top !p-0"
							height="400"
							width="400"
							alt="thumbnail"
						/>
					</div>
				</Motion>
			{/each}
		</div>
	</div>
</div>
