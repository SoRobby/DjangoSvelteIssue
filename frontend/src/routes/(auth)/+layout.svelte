<script lang="ts">
	import '../../app.css';
	import '../../styles/custom.css';
	import type { Snippet } from 'svelte';
	import { onMount } from 'svelte';

	let { children }: { children: Snippet } = $props();

	onMount(() => {
		// Add classes to root elements (html, body) for the login screen
		// to set the background color and height
		const addClasses = (element: HTMLElement, classes: string[]) => {
			classes.forEach((cls: string) => element.classList.add(cls));
		};

		const html = document.documentElement;
		const body = document.body;

		addClasses(html, ['bg-gray-50', 'h-full']);
		addClasses(body, ['h-full']);
	});
</script>

<main class="h-screen bg-zinc-50 px-4 sm:px-6 lg:px-8">
	{@render children()}
</main>
