<script lang="ts">
	import { onMount } from 'svelte';
	
	// Props
	export let className: string | undefined = undefined;
	
	// State for tracking mouse position
	let isHovering = false;
	let mouseX = 0;
	let mouseY = 0;
	let cardRef: HTMLDivElement;
	
	function handleMouseMove(e: MouseEvent) {
		if (!cardRef) return;
		
		const rect = cardRef.getBoundingClientRect();
		
		// Calculate mouse position relative to the card
		mouseX = e.clientX - rect.left;
		mouseY = e.clientY - rect.top;
		
		// Update rotation based on mouse position
		const centerX = rect.width / 2;
		const centerY = rect.height / 2;
		const rotateX = ((mouseY - centerY) / centerY) * -8; // Inverse for natural rotation
		const rotateY = ((mouseX - centerX) / centerX) * 8;
		
		// Apply rotation transform
		cardRef.style.transform = `perspective(1000px) rotateX(${rotateX}deg) rotateY(${rotateY}deg)`;
	}
	
	function handleMouseEnter() {
		isHovering = true;
		
		// Reset any existing transform transition
		if (cardRef) {
			cardRef.style.transition = 'transform 0.1s ease-out';
		}
	}
	
	function handleMouseLeave() {
		isHovering = false;
		
		// Smoothly animate back to initial position
		if (cardRef) {
			cardRef.style.transition = 'transform 0.5s ease-out';
			cardRef.style.transform = 'perspective(1000px) rotateX(0deg) rotateY(0deg)';
		}
	}
	
	onMount(() => {
		// Ensure the card has perspective styling
		if (cardRef) {
			cardRef.style.transition = 'transform 0.5s ease-out';
		}
	});
</script>

<div
	bind:this={cardRef}
	class="card-container {className || ''}"
	on:mouseenter={handleMouseEnter}
	on:mousemove={handleMouseMove}
	on:mouseleave={handleMouseLeave}
	role="presentation"
>
	<div class="card-content" class:hovering={isHovering}>
		<slot />
	</div>
</div>

<style>
	/* Card styles */
	.card-container {
		border-radius: 12px;
		overflow: hidden;
		position: relative;
		transform-style: preserve-3d;
		will-change: transform;
		transform: perspective(1000px);
		background-color: transparent;
	}
	
	.card-content {
		height: 100%;
		width: 100%;
		position: relative;
		transform-style: preserve-3d;
		transition: all 0.3s ease;
	}
	
	.hovering {
		box-shadow: 0 15px 30px rgba(0, 0, 0, 0.1);
	}

	/* Apply the card effect only on devices with hover capability */
	@media (hover: hover) {
		.card-container {
			transform-style: preserve-3d;
		}
		
		.card-content {
			transform-style: preserve-3d;
		}
	}
</style>
