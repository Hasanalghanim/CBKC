import Card from '@mui/material/Card';
import CardActions from '@mui/material/CardActions';
import CardContent from '@mui/material/CardContent';
import CardMedia from '@mui/material/CardMedia';
import Typography from '@mui/material/Typography';
import { formatDateTimeWithTimezone } from '../../../util/formatDates';
import TryoutsEditEventPopUpContent from './TryoutsEditEventPopUpContent';
import CBKCDialog from '../../../components/CBKCDialog';
import CBKCBreadCrumbs from '../../../components/CBKCBreadCrumbs';

const CBKCTryoutDetailMobile = ({ event, onUpdate }) => {
	return (
		<>
			<CBKCBreadCrumbs
				links={[
					{ url: '#/dashboard/tryouts_tab', name: 'Tryout Events' },
					{ url: `#/dashboard/tryouts_tab/${event.slug}`, name: event.name, active: true },
				]}
			/>
			<Card sx={{}}>
				<CardMedia
					component='img'
					height='250'
					image={`${import.meta.env.VITE_API_URL}${event.banner}`}
					alt={event.name}
				/>
				<CardContent>
					<Typography gutterBottom variant='h5' component='div'>
						{event.name}
					</Typography>
					<Typography variant='body2' sx={{ color: 'text.secondary' }}>
						{formatDateTimeWithTimezone(event.date)}
					</Typography>
					<Typography variant='body2' sx={{ color: 'text.secondary' }}>
						{event.venue}
					</Typography>
					<Typography variant='body2' sx={{ color: 'text.secondary' }}>
						{event.location}
					</Typography>
					<Typography variant='body2' sx={{ color: 'text.secondary' }}>
						{event.description}
					</Typography>
				</CardContent>
				<CardActions>
					<CBKCDialog
						buttonName={'Edit Event'}
						popUpTitle={'Edit Event'}
						submitBtn={'Save Edits'}
						popupText={'After Saving edits you will be unable to retrieve previous data'}
						dialogSize={'md'}
						submitFunc={onUpdate}>
						{({ control, setValue, register, watch }) => (
							<>
								<TryoutsEditEventPopUpContent
									control={control}
									setValue={setValue}
									register={register}
									originalData={event}
								/>
							</>
						)}
					</CBKCDialog>
				</CardActions>
			</Card>
		</>
	);
};

export default CBKCTryoutDetailMobile;
